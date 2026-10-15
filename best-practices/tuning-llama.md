# Tuning Llama for a Small Model

Getting a model running is covered in [Setting Up Inference](inference.md). This page is about what
you pass to `Llama(...)` afterwards — which settings decide whether it runs at all, which only
change the output, and how to tell them apart.

The distinction matters because they fail differently. A memory setting that is too ambitious fails
loudly, at load, before a single token is generated. A sampling setting that is wrong just gives
you worse answers.

## The memory budget

Three things occupy VRAM:

1. **The model weights** — fixed by which file you chose.
2. **The KV cache** — scratch space for the conversation so far. Set by `n_ctx`, allocated **up
   front**, and the usual surprise.
3. **Working memory** for processing the prompt, influenced by `n_batch`.

On a shared T4 there is 16GB and [two people drawing on it](../environments/gpu.md). Plan around
**7GB**, not 16.

## `n_ctx` — the one that catches people

`n_ctx` is how many tokens the model can hold in view. It looks free. It is not: the KV cache grows
**linearly** with it, and the whole allocation happens when the model loads.

```python
n_ctx = 512   # the default: small
n_ctx = 0     # means "use the model's full trained length"
```

:::{warning}
`n_ctx=0` is not "pick something sensible" — it is "use everything this model was trained for",
which on a modern small model can be 128,000 tokens. The KV cache for that can exceed the whole
card before you generate anything, and it surfaces as a CUDA out-of-memory error at load.
:::

**Set it to what your prompts actually need**, with headroom. Question-answering over a paragraph
might need 2,048. Summarising a long PDF might need 8,192. Reach for 32,768 only after measuring
that you need it.

When the model loads, llama.cpp prints what it allocated — look for the lines reporting KV cache and
buffer sizes. That is the authoritative number, and it moves when you change `n_ctx`. Halve `n_ctx`,
reload, and watch it halve.

## `n_gpu_layers` — everything on the GPU, or split

```python
n_gpu_layers = 0    # the default: CPU only
n_gpu_layers = -1   # every layer on the GPU
n_gpu_layers = 20   # the first 20 layers on the GPU, the rest on CPU
```

:::{warning}
**The default is `0`, which means the GPU is not used at all.** A notebook that runs but feels
inexplicably slow on a GPU hub is usually this. It is not an error, so nothing tells you.
:::

**Put everything on the GPU** — `-1` — when the weights plus the KV cache fit in your share of the
card. For a quantised 1–2B model at a modest `n_ctx` they will, and it is several times faster.
This is the case you want.

**Split the work** when they do not fit. Offloading only some layers runs the remainder on CPU, and
every token crosses that boundary, so it is substantially slower — but it is the difference between
slow and not running at all. Start high and come down until it loads: try `-1`, then 24, then 16.

Splitting is also a considerate choice when someone else is working on the other half of the card
and you would otherwise crowd them out.

## `n_batch`

How many prompt tokens are processed at once (default `512`). It affects memory during the *prompt*
phase, not generation. If a model loads happily and then runs out of memory on a long prompt, lower
this before touching anything else.

## The settings that only change the output

None of these affect whether the model fits.

| Setting | What it does |
|---|---|
| `temperature` | Randomness. `0` is deterministic and repetitive, `0.7`–`0.8` is conversational, above `1.2` tends to wander. |
| `top_p` | Consider only the most likely tokens that together reach this probability. `0.9` pairs conventionally with temperature. |
| `top_k` | Consider only the `k` most likely tokens. Blunter than `top_p`. |
| `repeat_penalty` | Discourages repetition. Raise it if the model loops. |
| `max_tokens` | How long the answer may be. Costs time, not VRAM. |
| `seed` | Fixes the random draw, so the same prompt gives the same answer. |

:::{note}
Set `seed` for anything you will grade or demonstrate. Without it two students running identical
code get different answers, and so do you when you re-run it in front of the class.
`temperature=0` is the stronger guarantee of the two.
:::

## A starting point

```python
from llama_cpp import Llama

llm = Llama(
    model_path="/home/jovyan/shared/models/gguf/your-model.gguf",
    n_gpu_layers=-1,   # all layers on the GPU
    n_ctx=4096,        # raise only if your prompts need it
    n_batch=512,
    seed=42,
)

out = llm.create_chat_completion(
    messages=[{"role": "user", "content": "Explain gradient descent in two sentences."}],
    temperature=0.7,
    max_tokens=256,
)
```

Change one thing at a time. If it stops loading, the last thing you changed was almost certainly
`n_ctx` or `n_gpu_layers`.

## When it fails

| What you see | Usually |
|---|---|
| CUDA out of memory **at load** | `n_ctx` too large, or someone else is using the card |
| Out of memory **partway through a long prompt** | `n_batch` too large |
| Loads and runs, but very slowly | `n_gpu_layers` left at its default of `0` |
| Worked yesterday, fails today | The other half of the shared GPU is in use — check `nvidia-smi` |
