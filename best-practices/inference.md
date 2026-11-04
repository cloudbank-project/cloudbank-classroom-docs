# Setting Up Inference

To run a language model on the hub, you need a [GPU hub](../environments/gpu.md) and the
small-models workshop image. This page covers picking a model that fits, where to put the files,
and why a shared GPU can run out of memory when two people use it.

## Read this first

A T4 is shared by **two people at a time**, and its 16 GB of memory is **not split** between them.
Both people use the same memory.

So a model that loads fine when you test it alone can fail for a student when someone else is
using the same GPU. The error is CUDA out of memory, and it looks like the code is broken even
though nothing changed.

:::{warning}
Pick a model small enough that **two copies fit in 16 GB**. A model that uses 14 GB works when you
test it and breaks as soon as a second student loads anything.
:::

Run `nvidia-smi` in a terminal to see what is using the GPU, including the other person's session.
See [Using the Terminal](../environments/terminal.md) for how to open one.

## Use GGUF files

On a T4, use quantized GGUF files. A 7 to 8B model at full precision doesn't leave room for a
second person. The same model quantized to 4 or 8 bits does, and it loads much faster.

The image has `llama-cpp-python` built for CUDA, plus `gguf`, `huggingface_hub`, `transformers`,
`sentence-transformers`, `langchain`, `llama-index`, `chromadb` and `diffusers`.

Start smaller than you think. A 1 to 4B instruct model answers quickly, leaves room for the other
person, and is usually enough to teach the idea.

## Download the model once, to the shared folder

Don't have 30 students each download several GB from Hugging Face into their home directories. It
is slow and it will fill up their 5 GiB.

Put the model in the shared folder instead. Instructors can write there and everyone can read it:

```python
from huggingface_hub import hf_hub_download

hf_hub_download(
    repo_id="google/gemma-3-1b-it-qat-q4_0-gguf",
    filename="gemma-3-1b-it-q4_0.gguf",
    local_dir="/home/jovyan/shared/models/gguf",
)
```

Then have students load it from that file:

```python
from llama_cpp import Llama

llm = Llama(
    model_path="/home/jovyan/shared/models/gguf/gemma-3-1b-it-q4_0.gguf",
    n_gpu_layers=-1,
    n_ctx=2048,
)
```

`n_gpu_layers=-1` puts the whole model on the GPU. A lower number moves some of it to the CPU. That
is slower, but it lets a bigger model fit.

See [Tuning Llama for a Small Model](tuning-llama.md) for these settings, including `n_ctx`, which
is the usual cause of running out of memory when the model loads.

:::{note}
Only accounts that can write to the shared folder can download there, which is usually instructors.
Do the download yourself once before class.
:::

## Before you teach with it

Run the notebook all the way through on the hub, not just on your laptop. If you can, have a
colleague start a GPU session at the same time and run it again. That is how you find out if your
model leaves room for a second person, which is the problem students will run into.

On GPU hubs, [stop your server](../environments/gpu.md#stopping-your-server) when you're done. An
idle GPU session holds memory nobody else can use.
