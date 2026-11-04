# Memory and Storage Limits

Every server on a CloudBank Classroom hub has a limit on memory, CPU and disk. We keep the limits
modest so a whole class can work at the same time on shared machines.

## What you get

**Storage.** Your home directory has **5 GiB**. Files there are kept between sessions, even when
your server stops or restarts.

**CPU.** Up to **2 cores**. You get more or less depending on how busy the machine is. A notebook
that is waiting on you uses almost none.

**Memory.** This one is set per hub to fit the course. Most hubs give each student **1 to 1.5 GB**,
and some get more.

:::{note}
To see your hub's memory limit, look at the memory indicator in the bar at the bottom of
JupyterLab. It shows how much you are using and your limit.
:::

## When you run out of memory

When a notebook goes over its memory limit, the kernel is stopped and JupyterLab says the kernel
restarted or died. You don't get a Python error.

So if a cell fails with an error message, it is a bug in the code. If the kernel dies with no
message, no traceback and no `MemoryError`, it is almost always the memory limit.

Everything in memory is lost when the kernel restarts, so you have to run the notebook again from
the top.

Common causes:

- Reading a large file with `pandas.read_csv()` without limiting columns or rows
- Keeping several copies of the same data because each step makes a new variable
- A loop that keeps adding to a list or DataFrame
- Loading a model that is bigger than the limit

## Staying under the limit

Read only the columns you need with `usecols=`:

```python
import pandas as pd

trips = pd.read_csv("trips.csv", usecols=["start_time", "duration", "station"])
```

Read part of a large file with `nrows=` while you are still writing the code, and remove it when
the code works:

```python
sample = pd.read_csv("trips.csv", nrows=10_000)
```

Delete large variables with `del` when you are done with them:

```python
merged = trips.merge(stations, on="station")
summary = merged.groupby("station")["duration"].mean()
del merged
```

Restart the kernel (**Kernel > Restart Kernel**) before a final run so you start clean.

If your data still doesn't fit, ask us for more. See below.

## Asking for more

Memory and storage are set per hub, so a change applies to everyone on it. If the limit is wrong
for your course, the instructor should ask, not each student.

Instructors: tell us what you ran and what happened. We set the limit from real workloads.

:::{note}
Check this **before** your class needs it. Run your heaviest assignment on the hub early in the
term so we can fix the limit if it's too low.
:::

Questions? See [Getting help](../getting-help.md).
