# Tuning Llama for a Small Model

[Setting Up Inference](inference.md) covers getting a model running. This page covers the settings
you pass to `Llama(...)` after that: which ones decide if the model fits, and which ones only change
the answers.

They fail in different ways. A memory setting that is too high fails right away, when the model
loads. An output setting that is off just gives you worse answers.

## The memory budget

Three things use GPU memory:

1. **The model weights.** This depends on which file you picked.
2. **The KV cache.** This holds the conversation so far. It is set by `n_ctx` and all of it is
   reserved **when the model loads**. This is the one that surprises people.
3. **Working memory** for reading the prompt, set by `n_batch`.

A shared T4 has 16 GB and [two people using it](../environments/gpu.md). Plan for **7 GB**, not
16.

## `n_ctx`

`n_ctx` is how many tokens the model can keep track of. It uses more memory than you'd expect: the
KV cache grows with it, and all of it is reserved when the model loads.

```python
n_ctx = 512   # the default: small
n_ctx = 0     # use the model's full trained length
```

:::{warning}
`n_ctx=0` means "use everything this model was trained for." On a newer small model that can be
128,000 tokens. The KV cache for that can be bigger than the whole GPU, and you get a CUDA out of
memory error when the model loads.
:::

**Set it to what your prompts need**, plus some extra. Answering questions about a paragraph might
need 2,048. Summarizing a long PDF might need 8,192. Only go up to 32,768 if you've checked that
you need it.

When the model loads, llama.cpp prints how much memory it reserved. Look for the KV cache and
buffer sizes. Cut `n_ctx` in half, reload, and you'll see those numbers drop by half.

## `n_gpu_layers`

```python
n_gpu_layers = 0    # the default: CPU only
n_gpu_layers = -1   # every layer on the GPU
n_gpu_layers = 20   # the first 20 layers on the GPU, the rest on CPU
```

:::{warning}
**The default is `0`, which means the GPU isn't used at all.** If a notebook runs but is very slow
on a GPU hub, this is usually why. There is no error, so nothing tells you.
:::

**Use `-1`** to put everything on the GPU when the model and KV cache fit in your share. For a
quantized 1 to 2B model with a reasonable `n_ctx`, they will, and it is several times faster.

**Use a smaller number** when they don't fit. The rest runs on the CPU, which is a lot slower, but
slow is better than not running. Start high and go down until it loads: try `-1`, then 24, then
16.

A smaller number also leaves more room for the other person on the GPU.

## `n_batch`

How many prompt tokens are read at once (default `512`). It only uses memory while the prompt is
being read, not while the answer is generated. If a model loads fine and then runs out of memory on
a long prompt, lower this first.

## Settings that only change the answers

None of these change whether the model fits.

| Setting | What it does |
|---|---|
| `temperature` | Randomness. `0` gives the same answer every time and can repeat itself, `0.7` to `0.8` sounds natural, above `1.2` tends to drift off topic. |
| `top_p` | Only pick from the most likely tokens that add up to this probability. `0.9` is a common choice. |
| `top_k` | Only pick from the `k` most likely tokens. |
| `repeat_penalty` | Makes repeating less likely. Raise it if the model gets stuck in a loop. |
| `max_tokens` | How long the answer can be. Longer takes more time, not more memory. |
| `seed` | Fixes the randomness, so the same prompt gives the same answer. |

:::{note}
Set `seed` for anything you grade or demo. Without it, two students running the same code get
different answers, and so do you when you run it again in front of the class. `temperature=0` is
even more reliable.
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

Change one thing at a time. If it stops loading, the last thing you changed was almost always
`n_ctx` or `n_gpu_layers`.

## When it fails

| What you see | Usually |
|---|---|
| CUDA out of memory **when it loads** | `n_ctx` is too big, or someone else is using the GPU |
| Out of memory **partway through a long prompt** | `n_batch` is too big |
| Runs, but very slowly | `n_gpu_layers` is still the default `0` |
| Worked yesterday, fails today | The other person on the GPU is using it. Check `nvidia-smi` |
