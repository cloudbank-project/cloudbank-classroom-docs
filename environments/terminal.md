# Using the Terminal

Every server comes with a terminal: a command line running on the same machine as your notebooks,
in the same home directory. Use it for things a notebook is awkward at, like `git`, installing a
package, checking what is on the GPU, or compiling a program.

## Opening one

Open the Launcher with the **+** button above the file browser, or **File > New Launcher**, and
choose **Terminal** under **Other**.

:::{figure} ../images/launcher-terminal.png
:alt: The JupyterLab Launcher with Notebook, Console, and Other sections; Terminal is the first tile under Other.

The Launcher. Terminal is the first tile under **Other**.
:::

The terminal opens as a new tab, starting in your home directory, the same place the file browser
shows.

:::{figure} ../images/terminal.png
:alt: A terminal tab in JupyterLab showing the prompt jovyan@jupyter-student, an ls listing a materials-fds-v2 folder, and python --version printing Python 3.13.

A terminal tab. Files you see in the file browser are the files you see with `ls`.
:::

You can also use **File > New > Terminal**.

## Things to try

```
ls                      # list the files in your home directory
python --version        # which Python the notebooks use
pip list                # every Python package installed
nvidia-smi              # on a GPU server: what is using the GPU right now
```

Your username in the terminal is always `jovyan`, whatever you signed in as. That is normal; it is
the same account your notebooks run as.

## Things to know

- **Files you make here are in your home directory** and are kept between sessions, the same as
  files you make in a notebook. Anything outside your home directory is reset when your server
  restarts.
- **A terminal is part of your server.** Stopping your server closes every terminal, and anything
  still running in it stops too.
- **Closing the tab does not stop the terminal.** Reopen it from the **Running Terminals and
  Kernels** panel (the square stop icon on the far left) or end it there when you are done.
