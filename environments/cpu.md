# CPU Environment

Most CloudBank Classroom hubs use the same standard image, so a notebook that runs on one hub
usually runs on another. It is built from
[cal-icor/base-user-image](https://github.com/cal-icor/base-user-image).

## What is installed

**Python**, with the usual teaching and analysis packages: `datascience`, `pandas`, `numpy`,
`scipy`, `matplotlib`, `seaborn`, `plotly`, `scikit-learn`, `statsmodels`, `sympy`, `geopandas`
and `openpyxl`. `pytorch`, `transformers` and `tokenizers` are there too, which is enough for small
models on CPU.

**JupyterLab**, with `jupyterlab-git`, `jupytext`, `jupyterlab_rise` for presenting notebooks,
`jupyter-archive` for downloading folders, and the memory indicator described in
[Memory and Storage Limits](limits.md).

**Course tools**: `nbgitpuller` for sending out materials, and `otter-grader`.

**Other languages and editors.** R and RStudio are in the launcher, and so is VS Code
(`code-server`). `xeus-cling` gives you a C++ kernel.

**Command-line tools**: `git`, `curl`, `wget`, `vim`, `nano`, `htop`, `tree`, `rsync`, build tools
(`build-essential`, `cmake`), debuggers (`gdb`, `valgrind`), and `pandoc` plus TeX so notebooks
export to PDF.

:::{note}
Some hubs use a different image because their course needs one, like a Java image or one with GPU
libraries. If your hub gives you a choice when you log in, the options page says what each one is
for. See [GPU Environment](gpu.md).
:::

## Checking what you have

To check a package, run this in a notebook:

```python
import pandas as pd
pd.__version__
```

Or run this in a terminal to see everything:

```
pip list
```

If something is missing, see [Requesting Packages](packages.md).
