# Sharing Data and Course Materials

There are two ways to put data in front of a class, and the size of the data decides which one you
want. Small files travel with the assignment. Large files belong in the hub's shared folder, where
one copy serves everyone.

## Files that travel with the assignment

An [nbgitpuller link](loading-files.md) copies the whole repository folder, not just the notebook.
So every file you put next to an assignment in the repository lands next to it on the hub.

:::{figure} ../images/files.png
:alt: The JupyterLab file browser open on an hw05 folder, listing the notebook alongside its CSV and image files, with the notebook open beside it.

Everything in the assignment's repository folder arrives with the notebook.
:::

That means plain relative paths work, with no setup and nothing for students to configure:

```python
from datascience import Table
scores = Table.read_table("roulette_wheel.csv")
```

```python
import pandas as pd
scores = pd.read_csv("roulette_wheel.csv")
```

Every student gets their own copy of those files, which is what you want while they are small.

## When one copy is enough

Per-student copies stop making sense as files grow. A 10 GB dataset in a repository becomes 10 GB in
each student's storage, so a class of 100 is carrying 1000 GB of the same data.

The hub's shared folder holds one copy that everyone reads. The same 10 GB dataset stays 10 GB no
matter how many students are enrolled.

:::{figure} ../images/shared-readwrite.png
:alt: The JupyterLab file browser at the top of a home directory, listing two course folders alongside shared and shared_readwrite.

`shared` and `shared_readwrite` sit at the top of your home directory, beside your course folders.
:::

## shared and shared_readwrite

These are two views of one folder, with different permissions:

| Folder | Who sees it | Access |
|---|---|---|
| `shared` | Everyone on the hub | Read only |
| `shared_readwrite` | Hub admins, which means instructors | Read and write |

Because they are the same folder underneath, a file you write through `shared_readwrite` appears
right away in everyone's `shared`. Nothing writes to `shared` itself, which is what keeps a student
from deleting a dataset the whole class depends on.

If you are teaching and do not see `shared_readwrite`, you do not have admin access on your hub yet.
[Getting help](../getting-help.md) covers how to ask for it.

:::{note}
2i2c's own documentation spells the second folder `shared-readwrite` with a hyphen. CloudBank hubs
use an underscore, so match what your file browser shows.
:::

## Reading from shared in a notebook

The shared folders sit at the top of your home directory, not beside your notebook, so a bare
filename will not find them. Path from your home directory instead:

```python
import pandas as pd
census = pd.read_csv("~/shared/census-2020.csv")
```

If a library does not expand `~`, build the path yourself:

```python
from pathlib import Path
shared = Path.home() / "shared"
census = pd.read_csv(shared / "census-2020.csv")
```

:::{warning}
Write notebooks against `~/shared/`, never `~/shared_readwrite/`. Students have no
`shared_readwrite` folder, so a notebook pointing there runs fine for you and fails for the whole
class.
:::

## Getting data into shared

Put files in `shared_readwrite` and they become readable by everyone. You can upload them through
JupyterLab, or open a terminal on the hub and pull them in with `curl` or `wget`.

For datasets too large for either of those to be practical, talk to CloudBank before the term
starts. [Getting help](../getting-help.md) covers how to reach us.
