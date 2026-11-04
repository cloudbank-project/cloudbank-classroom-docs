# RStudio

Every hub with the standard image has RStudio next to JupyterLab. You don't need a separate account
or a different hub address.

## Opening it

Start your server as usual, then choose **RStudio** in the JupyterLab launcher. It opens in a new
browser tab.

:::{note}
RStudio runs inside your hub server, so stopping your server stops RStudio too. Your files stay in
your home directory.
:::

## Same files as JupyterLab

JupyterLab and RStudio use the **same** home directory. A CSV you upload in JupyterLab shows up in
RStudio right away, and an `.Rmd` you write in RStudio shows up in the JupyterLab file browser.

The same limits apply to both: one 5 GiB home directory and one memory limit for everything you
have running. See [Memory and Storage Limits](../environments/limits.md).

## R packages

About 65 R packages are installed, including `tidyverse`, `tidymodels`, `ggplot2` and related
packages (`ggpubr`, `ggrepel`, `ggridges`, `ggthemes`, `GGally`), `mosaic`, `infer`, `car`,
`janitor`, `lubridate`, `forecast`, `leaflet`, `sf`, `terra`, `stars`, `quarto`, `rmarkdown`,
`knitr`, and teaching datasets like `palmerpenguins`, `nycflights13`, `openintro` and `Lock5Data`.

The full list, with versions, is in
[install.R](https://github.com/cal-icor/base-user-image/blob/main/install.R) in the image
repository.

`IRkernel` is installed too, so you can also use R in a Jupyter notebook.

## Installing a package yourself

```r
install.packages("<package>")
```

It installs into your home directory and stays between sessions. Like Python packages, it is only
for you. Your students won't have it. If your class needs a package, ask us to add it to the image.
See [Requesting Packages](../environments/packages.md).

:::{warning}
R packages that build from source can be slow and use a lot of memory. A big install can go over a
1 to 1.5 GB limit. If `install.packages()` stops partway with no error, that is usually why.
:::

## Shiny

Shiny apps run on the hub from the launcher. Quarto and R Markdown are installed, so documents knit
to HTML and PDF with no extra setup.
