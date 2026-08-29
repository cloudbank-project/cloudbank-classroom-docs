# GPU Environment

Some hubs offer a GPU profile alongside the standard CPU one, for courses whose work actually
needs one — computer vision, deep learning, and similar. This page covers what it is, who it's
for, how to get it, and what's expected of you once you do.

:::{important}
GPU support is a **pilot service**, not a fixed guarantee. Capacity, cost limits, and the details
on this page are still being tuned as we learn how courses actually use it. If something here
changes, [Getting Help](../getting-help.md) is where you'll hear about it.
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

At the spawn page, pick the GPU profile instead of CPU only. Each GPU is an NVIDIA T4, shared
between **two people at a time**, with 16GB of RAM split between them.

Inside the GPU profile you choose an image:

- A small-models workshop image with PyTorch and common LLM tooling (transformers, langchain, a
  local `llama-cpp-python` build) already installed.
- A TensorFlow/JAX image.
- A plain PyTorch image, if you don't need the extra LLM tooling and want a smaller environment.

## Startup time: why it isn't always instant

The GPU profile can start in under 30 seconds, or take several minutes. Both are normal, and the
difference comes down to whether a GPU machine is already running:

- **A machine that's already up** just needs to start your image, which is fast.
- **A brand-new GPU machine** needs its NVIDIA driver installed before it can run anything — that
  alone can take up to about 10 minutes on a fresh machine. The GPU image itself downloads onto the
  machine in parallel, and that part typically finishes in about 5 minutes, so the driver install is
  usually what you're waiting on, not the image.

:::{note}
If your login is taking a few minutes, it's very likely a new GPU machine coming online, not a
stuck session. Give it up to about 15–20 minutes before assuming something is actually wrong.
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

You don't have to rely on remembering, though: a session shuts down on its own after **one hour
with no activity**, and after **12 hours total**, even if it's in the middle of a long-running
process. Save your work accordingly — a training run or job that needs longer than 12 hours
straight won't be able to finish in one session.

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
