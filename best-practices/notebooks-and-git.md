# Editing Notebooks and Using Git

Notebooks and git do not get along by default. A notebook is a JSON file that stores your code,
your outputs, and an execution count for every cell — so re-running a notebook without changing a
line of code still produces a large, unreadable diff.

This page is about keeping that under control. If what you want is to hand materials to students,
[Loading Files onto the Hub](../files/loading-files.md) covers that instead — students never touch
git.

## Clear outputs before you commit

This single habit removes most of the noise. Outputs are usually the bulk of a notebook's file
size, and they change every run.

**Kernel > Restart Kernel and Clear Outputs of All Cells**, then save, then commit.

Clearing outputs also restarts from a clean state, which catches the classic problem of a notebook
that only runs because of a variable defined in a cell you later deleted. Doing it before every
commit means you find that on your machine rather than in a student's.

:::{warning}
Outputs can contain more than plots — an API key printed while debugging, a student name in a
dataframe, a file path with your username in it. Once committed to a public repository it stays in
the history even after you delete the cell.
:::

## Pair notebooks with a text file

`jupytext` is installed on the hub and solves the diff problem properly. It keeps a `.py` or `.md`
copy of your notebook alongside the `.ipynb`, synchronised on save. You commit the text version,
which diffs and reviews like ordinary code.

In JupyterLab, right-click the notebook and choose **Pair Notebook with percent Script**. From a
terminal:

```
jupytext --set-formats ipynb,py:percent notebook.ipynb
```

Both files stay in step from then on. A reviewer reads the `.py`; anyone who wants to run it opens
the `.ipynb`.

## Working with git on the hub

The `jupyterlab-git` extension is installed, so a repository cloned into your home directory gets a
git panel in the left sidebar — stage, commit, branch and view history without leaving JupyterLab.

To push back to GitHub, authenticate with `gh-scoped-creds`, which is also installed:

```
gh-scoped-creds
```

It prints a code and a URL, you authorise once in the browser, and pushes work for the rest of the
session. This avoids putting a personal access token in a file on a shared hub.

:::{note}
Credentials from `gh-scoped-creds` are temporary and do not survive your server stopping. Running
it again takes a few seconds.
:::

## A .gitignore worth starting from

```
.ipynb_checkpoints/
__pycache__/
.DS_Store
*.csv
```

Ignoring data by default is deliberate. Large files in a repository make every student's
nbgitpuller clone slower, and a dataset that changes is better fetched by the notebook than
committed.

:::{note}
`nbdime`, which renders notebook diffs cell by cell, is **not** installed on the hub. If you want
it locally, `pip install nbdime` on your own machine.
:::
