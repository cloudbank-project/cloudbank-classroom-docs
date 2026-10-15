# RStudio

Every hub running the standard image has RStudio available alongside JupyterLab. You do not need a
separate account or a different hub address.

## Opening it

Start your server as usual, then from the JupyterLab launcher choose **RStudio**. It opens in a new
browser tab, served from the same session.

:::{note}
RStudio runs inside your hub server, so stopping your server stops RStudio too. Your files are
unaffected — they live in your home directory either way.
:::

## It is the same home directory

This is the part worth understanding. JupyterLab and RStudio are two windows onto the **same**
files. A CSV you upload in JupyterLab is immediately visible to RStudio, and an `.Rmd` you write in
RStudio appears in the JupyterLab file browser.

The same limits apply to both — one 5 GiB home directory, one memory ceiling shared by everything
in your session. See [Memory and Storage Limits](../environments/limits.md).

## R packages

About 65 R packages are pre-installed, including `tidyverse`, `tidymodels`, `ggplot2` and the wider
`gg*` family (`ggpubr`, `ggrepel`, `ggridges`, `ggthemes`, `GGally`), `mosaic`, `infer`, `car`,
`janitor`, `lubridate`, `forecast`, `leaflet`, `sf`, `terra`, `stars`, `quarto`, `rmarkdown`,
`knitr`, and teaching datasets such as `palmerpenguins`, `nycflights13`, `openintro` and
`Lock5Data`.

The authoritative list, with versions, is
[install.R](https://github.com/cal-icor/base-user-image/blob/main/install.R) in the image
repository.

`IRkernel` is installed too, so you can work in R from a Jupyter notebook instead if you prefer.

## Installing a package yourself

```r
install.packages("<package>")
```

It installs into your home directory and persists across sessions. As with Python packages, it is
yours alone — your students will not have it. Anything a class depends on should go in the image
instead; see [Requesting Packages](../environments/packages.md).

:::{warning}
R packages that compile from source can be slow and memory-hungry, and a large install can push a
1–1.5 GB session into a memory kill. If `install.packages()` dies partway with no error, that is
usually what happened.
:::

## Shiny

Shiny apps run on the hub through the launcher. Quarto and R Markdown are installed, so documents
knit to HTML and PDF without extra setup.
