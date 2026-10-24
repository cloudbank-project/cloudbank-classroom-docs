# Setting Up Inference

Running a language model on the hub means a [GPU hub](../environments/gpu.md) and the small-models
workshop image. This page covers choosing a model that fits, where to put the weights, and how a shared GPU can
run out of memory when two people use it at once.

## The thing to know first

A T4 is shared between **two people at a time**, and its 16GB of VRAM is **not partitioned**. Both
sessions allocate from the same pool.

In practice that means a model which loads perfectly when you test it alone can fail for a student
when someone else is also working. The failure is a CUDA out-of-memory error, and it will look like
your code is broken when nothing has changed.

:::{warning}
Size your model so that **two copies fit in 16GB**, not one. A model using 14GB works flawlessly in
testing and breaks the moment a second student loads anything.
:::

`nvidia-smi` in a terminal shows what is actually allocated on the card, including the other
session's usage. [Using the Terminal](../environments/terminal.md) shows how to open one.

## Use GGUF, not full weights

For teaching on a T4, quantised GGUF files are almost always the right choice. A 7–8B model in full
precision does not leave room for a second user; the same model quantised to 4- or 8-bit does,
and loads in a fraction of the time.

The image has `llama-cpp-python` built against CUDA for exactly this, plus `gguf`,
`huggingface_hub`, `transformers`, `sentence-transformers`, `langchain`, `llama-index`, `chromadb`
and `diffusers`.

Start smaller than you think you need. A 1–4B instruct model answers quickly, leaves headroom, and
is usually enough to teach the concept.

## Download weights once, to the shared folder

Do not have thirty students each pull several GB from Hugging Face into their own home directories.
It is slow, it repeats the same download, and it will exhaust the 5 GiB home quota.

Put the weights in the shared folder instead, where instructors can write and everyone can read:

```python
from huggingface_hub import hf_hub_download

hf_hub_download(
    repo_id="google/gemma-3-1b-it-qat-q4_0-gguf",
    filename="gemma-3-1b-it-q4_0.gguf",
    local_dir="/home/jovyan/shared/models/gguf",
)
```

Then point students at the file rather than at the Hub:

```python
from llama_cpp import Llama

llm = Llama(
    model_path="/home/jovyan/shared/models/gguf/gemma-3-1b-it-q4_0.gguf",
    n_gpu_layers=-1,
    n_ctx=2048,
)
```

`n_gpu_layers=-1` puts the whole model on the GPU. Lowering it moves layers to CPU — slower, but a
way to fit a model that is otherwise too large.

[Tuning Llama for a Small Model](tuning-llama.md) covers these settings properly, including
`n_ctx`, which is the usual cause of an out-of-memory error at load.

:::{note}
Shared-folder downloads only work from an account with write access there, normally an
instructor's. Do the download once yourself before class.
:::

## Before you teach with it

Run the notebook end to end on the hub, not just on your laptop. Then, if you can, have a colleague
start a GPU session at the same time and run it again — that is the only way to find out whether
your model leaves room for a second person, and it is the failure students will actually hit.

[Shutting down when you're done](../environments/gpu.md#shutting-down-when-youre-done) matters more
on GPU hubs than anywhere else: an idle GPU session holds VRAM that nobody else can use.
