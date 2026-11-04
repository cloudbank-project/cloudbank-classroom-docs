# GPU Environment

Some hubs have a GPU option next to the standard CPU one. It is for courses that need a GPU, like
computer vision or deep learning.

:::{important}
GPU support is a **pilot**. We are still adjusting capacity, cost limits and the details on this
page. When something changes, we will update this page and post it to the CloudBank affinity group
listed on [Getting Help](../getting-help.md).
:::

## Who it's for

The GPU option is for work that is too slow on a CPU, like training or running models. GPUs are
shared, limited and cost more to run, so if your course doesn't need one, use CPU. If you're not
sure, ask us when you request access.

## Getting access

We set up GPU access with you. You can't turn it on yourself.

- **New hub:** tell us you need GPUs when you request the hub.
- **Existing hub:** email us to add the GPU option, and send your class times so we can plan for
  them.

See [Getting Help](../getting-help.md) for how to reach us. Once it's set up, everyone on your hub
can pick the GPU option. Students don't need separate approval.

## Choosing the GPU option

On the start page, pick the GPU option instead of CPU. Each GPU is an NVIDIA T4 with 16 GB of
memory, shared by **two people at a time**.

The 16 GB is **not** split between you. Both people use the same memory, so a large model loaded by
one person leaves less for the other. See [Setting Up Inference](../best-practices/inference.md).

Inside the GPU option you pick an image:

- A small-models workshop image with PyTorch and LLM tools (transformers, langchain, and
  `llama-cpp-python`) already installed.
- A TensorFlow/JAX image.
- A plain PyTorch image, if you don't need the LLM tools.

## If you don't see the GPU option

The options page only shows up when you don't have a server running. If you started a CPU server
earlier and didn't stop it, logging in takes you straight back to it. The same is true the other
way: a running GPU server takes you back to GPU.

To get the options page back:

1. In JupyterLab, go to **File > Hub Control Panel**.
2. Click **Stop My Server** and wait a few seconds.
3. Click **Start My Server**.

:::{note}
This happens a lot at the start of a GPU lab. Students logged in on CPU earlier in the week, their
servers are still running, and they never see the GPU option. Stopping the server fixes it.
:::

## Startup time

A GPU server can start in under 30 seconds or take several minutes. Both are normal. It depends on
whether a GPU machine is already running:

- **A machine that is already running** only has to start your image, which is fast.
- **A new GPU machine** has to start, install the NVIDIA driver and download the GPU image. That
  takes about 7 to 10 minutes, mostly the download, since the image is about 17 GB. The second
  student on that machine starts much faster.

:::{note}
If your login is taking a few minutes, a new GPU machine is probably starting. Give it about 10
minutes before you email us.
:::

If you know when your class needs GPUs, like a lab day or a regular class time, tell us ahead of
time. We can have GPU machines running before class starts, so students get the fast start.

## Cost and capacity

GPU machines cost more than CPU machines.

| | Shared by | Approximate cost |
|---|---|---|
| CPU machine | 16 people | ~$0.25/hour |
| GPU machine (NVIDIA T4) | 2 people | ~$1/hour |

A class of 20 students all on GPU at once needs about 10 GPU machines. Please share this with your
students. Stopping their server when they're done, instead of leaving it idle, means fewer GPU
machines have to stay running.

## Stopping your server

A GPU server you leave running keeps that GPU from anyone else, even if you aren't using it. When
you're done:

1. In JupyterLab, go to **File > Hub Control Panel**.
2. Click **Stop My Server**.

Ask your students to do this at the end of every lab. Closing the browser tab is not enough.

If someone forgets, a GPU hub stops the server on its own:

- **one hour** after the browser tab is closed, if nothing is running;
- **about two hours** after code stops running, even with the tab open. An idle notebook is stopped
  after an hour, and the server shuts down an hour after that;
- after **12 hours total**, even if something is still running.

Save your work as you go. If your course needs jobs that run longer than this, CloudBank has other
resources for that. [Email us](../getting-help.md) and we will help you find the right one.

## Packages

The GPU image's packages are listed in its
[`environment.yml`](https://github.com/cal-icor/workshop-gpu-image/blob/main/environment.yml). The
CPU image's are in its own
[`environment.yml`](https://github.com/cal-icor/base-user-image/blob/main/environment.yml).

To ask for a package, see [Requesting Packages](packages.md). GPU requests go to the GPU image's
[issue tracker](https://github.com/cal-icor/workshop-gpu-image/issues), not the CPU image's.

Questions? See [Getting help](../getting-help.md).
