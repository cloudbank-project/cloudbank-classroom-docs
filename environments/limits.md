# Memory and Storage Limits

Every server on a CloudBank Classroom hub runs with a fixed ceiling on memory, CPU and disk. The
limits are deliberately modest so that a full class can work at once on shared machines.

## What you get

**Storage.** Your home directory has a **5 GiB** quota. Files there persist between sessions and
survive your server being stopped or restarted.

**CPU.** Up to **2 cores**. This is a ceiling, not a reservation — you get more or less of it
depending on how busy the machine is, and a notebook that is mostly waiting for you uses almost
none.

**Memory.** This is the one that varies, because it is set per hub to suit the course. Most hubs
give each student **1–1.5 GB**, and some are configured higher.

:::{note}
To see your hub's actual memory limit, look at the resource indicator in the JupyterLab status bar
at the bottom of the window. It shows memory in use against your limit, and updates as you work.
:::

## When you run out of memory

A notebook that exceeds its memory limit does not raise a normal Python error. The kernel is killed
outright, and JupyterLab reports that the kernel has restarted or died.

The tell is what you **do not** see: there is no traceback, no `MemoryError`, and no line number.
A cell that fails with an ordinary exception is a bug in the code; a cell that kills the kernel
with no message is almost always the memory limit.

All variables are lost when the kernel restarts, so you have to re-run the notebook from the top.

Common causes, roughly in order:

- Reading a large file with `pandas.read_csv()` without limiting columns or rows
- Holding several copies of the same data because each step assigns a new variable
- A loop that appends to a list or DataFrame and is never cleared
- Loading a model whose weights are larger than the limit

## Working inside the limit

Read only the columns you need with `usecols=`, and sample large files with `nrows=` while you are
still developing. Delete large intermediates with `del` once you are finished with them. Restart
the kernel before a final run so you are not carrying objects from earlier experiments.

If a dataset genuinely does not fit, that is worth raising rather than working around — see below.

## Asking for more

Memory and storage are set per hub, not per person, so a change applies to everyone on it. If the
limit is wrong for the course, your instructor should ask rather than each student asking
individually.

Instructors: it helps a great deal to say what you actually ran and what happened, because the
limit is chosen from real workloads. [Getting help](../getting-help.md) covers where to ask.

:::{note}
This is worth checking **before** a class needs it. Running your heaviest assignment once on the
hub, early, is the quickest way to find out whether the sizing is right.
:::
