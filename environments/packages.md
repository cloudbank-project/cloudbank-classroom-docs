# Requesting Packages

If your course needs a package that isn't in the image, you can ask us to add it, or install it
yourself right away. Ask us if your class depends on it. Install it yourself if you need it today.

## Ask us to add it

Do this for anything your class will use. The package goes into the image, so every student has it.

Open an issue on the repository for your course's image:

- CPU image: [cal-icor/base-user-image](https://github.com/cal-icor/base-user-image/issues/new)
- GPU small-models workshop image:
  [cal-icor/workshop-gpu-image](https://github.com/cal-icor/workshop-gpu-image/issues/new)

The TensorFlow and PyTorch images on GPU hubs come from the Pangeo project, so we can't add packages
to them. Ask for the package in the workshop image instead.

In the issue, include:

- the package name, and the version if you need a specific one
- your hub and course
- when you need it

We have to rebuild and redeploy the image, so it takes some time. Ask at least a week before the
assignment that needs it.

:::{note}
Check that it's really missing first. Most common packages are already there. See
[CPU Environment](cpu.md) and [GPU Environment](gpu.md).
:::

## Install it yourself

If you need something now, install it in your home directory:

```
pip install --user <package>
```

It goes into `~/.local`, which is in your home directory, so it stays after your server restarts.
Restart the kernel afterwards so your notebook can use it.

:::{warning}
A `--user` install is only for you. Your students won't have it. If an assignment needs a package,
it has to go in the image.
:::

:::{note}
Packages you install this way are used instead of the image's copies. After we update the image,
this can break things. If your environment starts acting strange, run `pip list --user` to see what
you added. Removing it usually fixes the problem.
:::

Questions? See [Getting help](../getting-help.md).
