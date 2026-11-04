# Sharing Data and Course Materials

There are two ways to give data to a class. Small files go with the assignment. Large files go in
the hub's shared folder, where one copy is enough for everyone.

## Files that go with the assignment

An [nbgitpuller link](loading-files.md) copies the whole repository, not just the notebook. So every
file you put next to an assignment in the repository ends up next to it on the hub.

:::{figure} ../images/files.png
:alt: The JupyterLab file browser open on an hw05 folder, listing the notebook alongside its CSV and image files, with the notebook open beside it.

Everything in the assignment's folder comes along with the notebook.
:::

So plain file names work, and students don't have to set anything up:

```python
from datascience import Table
scores = Table.read_table("roulette_wheel.csv")
```

```python
import pandas as pd
scores = pd.read_csv("roulette_wheel.csv")
```

Every student gets their own copy of those files. That is fine while they are small.

## When one copy is enough

For big files, a copy per student is too much. A 10 GB dataset in a repository becomes 10 GB in
each student's storage, so a class of 100 has 1000 GB of the same data.

The hub's shared folder holds one copy that everyone reads. The 10 GB dataset stays 10 GB no matter
how many students you have.

:::{figure} ../images/shared-readwrite.png
:alt: The JupyterLab file browser at the top of a home directory, listing two course folders alongside shared and shared_readwrite.

`shared` and `shared_readwrite` are at the top of your home directory, next to your course folders.
:::

## shared and shared_readwrite

These are the same folder with different permissions:

| Folder | Who sees it | Access |
|---|---|---|
| `shared` | Everyone on the hub | Read only |
| `shared_readwrite` | Hub admins (instructors) | Read and write |

A file you save in `shared_readwrite` shows up right away in everyone's `shared`. Students can only
read `shared`, so they can't delete a dataset the whole class needs.

If you are teaching and don't see `shared_readwrite`, you don't have admin access on your hub yet.
Email us to get it. See [Getting help](../getting-help.md).

:::{note}
2i2c's own docs spell the second folder `shared-readwrite` with a hyphen. CloudBank hubs use an
underscore, so go by what your file browser shows.
:::

## Reading from shared in a notebook

The shared folders are at the top of your home directory, not next to your notebook, so a plain file
name won't find them. Start the path from your home directory:

```python
import pandas as pd
census = pd.read_csv("~/shared/census-2020.csv")
```

If a library doesn't understand `~`, build the path yourself:

```python
from pathlib import Path
shared = Path.home() / "shared"
census = pd.read_csv(shared / "census-2020.csv")
```

:::{warning}
In notebooks, use `~/shared/`, never `~/shared_readwrite/`. Students don't have a
`shared_readwrite` folder, so a notebook that uses it works for you and fails for the whole class.
:::

## Getting data into shared

Put files in `shared_readwrite` and everyone can read them. You can upload them in JupyterLab, or
open a terminal on the hub and download them with `curl` or `wget`.

If your dataset is too big for that, talk to us before the term starts.

Questions? See [Getting help](../getting-help.md).
