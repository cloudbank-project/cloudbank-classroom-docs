# Requesting Packages

If a package your course needs is not in the image, there are two routes: ask for it to be added
permanently, or install it yourself for right now. Ask for it to be added if your class depends on
it; install it yourself if you need it today.

## Ask for it to be added

This is the right route for anything a class will rely on. The package becomes part of the image,
so every student has it without doing anything.

Open an issue on the repository for the image your course uses:

- the CPU image: [cal-icor/base-user-image](https://github.com/cal-icor/base-user-image/issues/new)
- the GPU small-models workshop image:
  [cal-icor/workshop-gpu-image](https://github.com/cal-icor/workshop-gpu-image/issues/new)

The Pangeo TensorFlow and PyTorch images on GPU hubs come from the Pangeo project, so we cannot add
packages to them; ask for the package in the workshop image instead.

In the issue, say:

- the package name, and the exact version if the course needs one
- which hub and course it is for
- when you need it by

Adding a package means rebuilding and redeploying the image, so it is not instant. Ask with some
runway before a class depends on it — the week before an assignment is comfortable, the morning of
is not.

:::{note}
Check first that it is actually missing. The images already include most of the common teaching
stack; see [CPU Environment](cpu.md) and [GPU Environment](gpu.md).
:::

## Install one yourself, today

When you need something immediately, install it into your own home directory:

```
pip install --user <package>
```

This lands in `~/.local`, which is part of your home directory, so it persists across sessions and
survives your server restarting. Restart the kernel afterwards so the running notebook picks it up.

:::{warning}
A `--user` install belongs to you alone. Your students will not have it, so it is not a way to
distribute a package to a class — if an assignment needs it, it has to go in the image.
:::

:::{note}
Packages installed this way take precedence over the image's own copies, which occasionally breaks
things in confusing ways after the image is updated. If an environment starts behaving oddly,
`pip list --user` shows what you have added, and removing it is usually the fix.
:::
