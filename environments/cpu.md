# CPU Environment

Most CloudBank Classroom hubs start you in the same standard image, so a notebook that runs on one
hub generally runs on another. It is built from
[cal-icor/base-user-image](https://github.com/cal-icor/base-user-image).

## What is installed

**Python**, with the usual teaching and analysis stack: `datascience`, `pandas`, `numpy`, `scipy`,
`matplotlib`, `seaborn`, `plotly`, `scikit-learn`, `statsmodels`, `sympy`, `geopandas` and
`openpyxl`. `pytorch`, `transformers` and `tokenizers` are there too, which is enough for small
models on CPU.

**JupyterLab**, with `jupyterlab-git`, `jupytext`, `jupyterlab_rise` for presenting notebooks,
`jupyter-archive` for downloading folders, and the resource indicator described in
[Memory and Storage Limits](limits.md).

**Course tooling**: `nbgitpuller` for distributing materials, and `otter-grader`.

**Other languages and editors.** R and RStudio are available through the launcher, as is VS Code
via `code-server`. `xeus-cling` provides a C++ kernel.

**Command-line tools** for terminal work: `git`, `curl`, `wget`, `vim`, `nano`, `htop`, `tree`,
`rsync`, build tools (`build-essential`, `cmake`), debuggers (`gdb`, `valgrind`), and `pandoc`
plus a TeX installation so notebooks export to PDF.

:::{note}
Some hubs use a different image because their course needs one — a Java image, or one with GPU
libraries. If your hub offers a choice when you log in, the options page names what each one is
for. See [GPU Environment](gpu.md).
:::

## Checking what you have

The surest answer comes from the environment itself rather than from this page. In a notebook:

```python
import pandas as pd
pd.__version__
```

Or in a terminal, to see everything at once:

```
pip list
```

If something you need is missing, [Requesting Packages](packages.md) covers both the quick fix and
the permanent one.
