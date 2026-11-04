# Editing Notebooks and Using Git

Notebooks and git don't work well together out of the box. A notebook is a JSON file with your
code, your outputs and a run count for every cell. So running a notebook again without changing any
code still gives you a big, hard-to-read diff.

This page is about keeping that under control. If you want to send materials to students, see
[Loading Files onto the Hub](../files/loading-files.md) instead. Students never need git.

## Clear outputs before you commit

This one habit removes most of the noise. Outputs are usually most of a notebook's file size, and
they change every run.

**Kernel > Restart Kernel and Clear Outputs of All Cells**, then save, then commit.

This also runs the notebook from a clean start. That catches a notebook that only works because of
a variable from a cell you deleted. You want to find that on your machine, not a student's.

:::{warning}
Outputs can hold more than plots: an API key you printed while debugging, a student's name in a
dataframe, a file path with your username. Once you commit that to a public repository, it stays in
the history even after you delete the cell.
:::

## Pair notebooks with a text file

`jupytext` is installed on the hub. It keeps a `.py` or `.md` copy of your notebook next to the
`.ipynb` and updates it every time you save. You commit the text version, which diffs like normal
code.

In JupyterLab, right-click the notebook and choose **Pair Notebook with percent Script**. Or from a
terminal:

```
jupytext --set-formats ipynb,py:percent notebook.ipynb
```

From then on both files stay in sync. Reviewers read the `.py`. Anyone who wants to run it opens
the `.ipynb`.

## Using git on the hub

The `jupyterlab-git` extension is installed. If you clone a repository into your home directory, you
get a git panel in the left sidebar where you can stage, commit, branch and see history.

To push to GitHub, sign in with `gh-scoped-creds`, which is also installed:

```
gh-scoped-creds
```

It prints a code and a link. You approve it once in the browser, and pushing works for the rest of
the session. That way you don't have to save a personal access token on a shared hub.

:::{note}
`gh-scoped-creds` credentials go away when your server stops. Running it again takes a few seconds.
:::

## A starting .gitignore

```
.ipynb_checkpoints/
__pycache__/
.DS_Store
*.csv
```

This ignores data files on purpose. Large files make every student's nbgitpuller download slower,
and data that changes is better downloaded by the notebook than committed.

:::{note}
`nbdime`, which shows notebook diffs cell by cell, is **not** installed on the hub. If you want it,
run `pip install nbdime` on your own computer.
:::
