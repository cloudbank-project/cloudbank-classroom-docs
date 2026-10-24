# GPU Environment

Some hubs offer a GPU profile alongside the standard CPU one, for courses whose work actually
needs one — computer vision, deep learning, and similar. This page covers what it is, who it's
for, how to get it, and what's expected of you once you do.

:::{important}
GPU support is a **pilot service**, not a fixed guarantee. We are still adjusting capacity, cost
limits, and the details on this page as we learn how courses use it. When something changes, we
will update this page and post it to the CloudBank affinity group listed on
[Getting Help](../getting-help.md).
:::

## Who it's for

The GPU profile exists for coursework that genuinely needs GPU compute — training or running
models that are impractical on CPU alone. It is shared, limited, and more expensive to run than the
CPU environment, so it isn't the default choice for a course that doesn't need it. If you're not
sure whether your course qualifies, ask when you request access.

## Getting access

GPU access is arranged with CloudBank before your hub is set up — it isn't something you turn on
yourself from an existing CPU-only hub. If your course needs it:

- A new hub: mention the GPU requirement when you request the hub (see
  [Getting Help](../getting-help.md)).
- An existing hub: reach out asking to add the GPU profile (see
  [Getting Help](../getting-help.md)), and let us know your expected class times so we can plan
  capacity around them.

Once it's set up, everyone with access to your hub can select the GPU profile — there's no separate
per-student approval step.

## Choosing the GPU profile

At the spawn page, pick the GPU profile instead of CPU only. Each GPU is an NVIDIA T4 with 16GB of
VRAM, shared between **two people at a time**.

The 16GB is **not** divided between you. Both sessions draw on the same pool, so a large model
loaded by one person leaves less for the other — see
[Setting Up Inference](../best-practices/inference.md).

Inside the GPU profile you choose an image:

- A small-models workshop image with PyTorch and common LLM tooling (transformers, langchain, a
  local `llama-cpp-python` build) already installed.
- A TensorFlow/JAX image.
- A plain PyTorch image, if you don't need the extra LLM tooling and want a smaller environment.

## If you don't see the profile picker

The picker only appears when you have no server running. If you already have a session going —
most often a CPU one you started earlier and haven't shut down — logging back in drops you straight
into it, with no picker and no chance to switch. It works the same way in reverse: a running GPU
session sends you back to GPU rather than offering you CPU.

To get the picker back, stop the server you already have:

1. In JupyterLab, go to **File > Hub Control Panel**.
2. Select **Stop My Server**, and wait a few seconds for it to respond.
3. Select **Start My Server**.

The picker appears on that second start.

:::{note}
This happens a lot at the start of a GPU lab. Students logged in on CPU earlier in the week, those
servers are still running, and no one sees the GPU option. Stopping the server fixes it; nothing is
wrong with the hub's GPU access.
:::

## Startup time: why it isn't always instant

The GPU profile can start in under 30 seconds, or take several minutes. Both are normal, and the
difference comes down to whether a GPU machine is already running:

- **A machine that's already up** just needs to start your image, which is fast.
- **A brand-new GPU machine** has to start up, install its NVIDIA driver, and download the GPU
  image before your server can run. That takes about 7 to 10 minutes, and almost all of it is the
  image download: the GPU image is about 17 GB. The second student on the same machine usually
  starts much faster, because the image is already there.

:::{note}
If your login is taking a few minutes, a new GPU machine is probably coming online. Give it about
10 minutes before assuming something is wrong.
:::

If you know in advance when your class needs GPUs — a specific lab session, a recurring class
time — tell CloudBank ahead of time (see [Getting Help](../getting-help.md)). We can have a GPU
machine already running and ready before your class starts, which is what gets you the
under-30-second case instead of the cold-start one.

## Cost and capacity

GPU machines cost more than CPU ones

| | Shared by | Approximate cost |
|---|---|---|
| CPU machine | 16 people | ~$0.25/hour |
| GPU machine (NVIDIA T4) | 2 people | ~$1/hour |

A class of 20 students all using the GPU profile at once needs about 10 GPU machines running
simultaneously. It's worth sharing this with your students so they have a sense of what they're
using — asking them to stop their server when they're done, rather than leaving it idle, directly
reduces how many GPU machines need to stay up.

## Shutting down when you're done

A GPU machine you leave running keeps that GPU unavailable to anyone else, even if you're not
actively using it. When you're finished with a session:

1. In JupyterLab, go to **File > Hub Control Panel**.
2. Select **Stop My Server**.

This is worth building into your course's routine — asking students to stop their server at the
end of a lab, not just close the browser tab, is one of the simplest ways to keep GPU capacity
available for everyone sharing it.

You don't have to rely on remembering, though. A GPU hub shuts a server down on its own:

- **one hour** after you close the browser tab, if nothing is running;
- **about two hours** after you stop running code, even with the tab still open. An idle notebook
  kernel is stopped after an hour, and the server shuts down an hour after its last kernel stops;
- after **12 hours total**, even in the middle of a long-running process.

Save your work as you go. If your course needs jobs that run longer than this, CloudBank has other
resources better suited to long-running work. [Contact us](../getting-help.md) and we will help you
find the right one.

## Packages

The GPU image's installed packages are listed in its
[`environment.yml`](https://github.com/cal-icor/workshop-gpu-image/blob/main/environment.yml). The
CPU image's are in its own
[`environment.yml`](https://github.com/cal-icor/base-user-image/blob/main/environment.yml).

To request something be added, see [Requesting Packages](packages.md) — GPU and CPU requests go to
different repos (the GPU image's own
[issue tracker](https://github.com/cal-icor/workshop-gpu-image/issues), separate from the CPU
image's).

If something in the GPU environment isn't behaving the way you expect, [Getting Help](../getting-help.md)
covers where to ask.
