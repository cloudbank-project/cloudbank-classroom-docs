# cloudbank-classroom-docs

Documentation for [CloudBank Classroom](https://www.cloudbank.org/), built with
[Jupyter Book 2](https://next.jupyterbook.org/) (MyST).

**Published site:** https://cloudbank-project.github.io/cloudbank-classroom-docs/

Every push to `main` rebuilds and redeploys the site via
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml).

## Building locally

```bash
pip install -r requirements-build.txt

# live preview with hot reload
myst start

# one-off static build into _build/html
jupyter book build --html
```

## Adding a page

Create the Markdown or notebook file, then add it to the `project.toc` list in
[`myst.yml`](myst.yml).
