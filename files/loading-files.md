# Loading Files onto the Hub

[nbgitpuller](https://nbgitpuller.readthedocs.io/) gives a whole class a copy of your materials from
one link. A student clicks it, the files land in their own space on the hub, and the notebook you
pointed at opens. Nobody needs to know git.

Setting this up takes two things: your materials in a public GitHub repository, and a link that
points at them.

## Put your materials in a public repo

Go to [GitHub](https://github.com/) and choose **New**.

:::{figure} ../images/new-github.png
:alt: The GitHub dashboard with a green New button next to the Top repositories heading.

Start from the New button on your GitHub dashboard.
:::

Pick an owner, which can be your personal account or an organization your course uses, and name the
repository. Set **Choose visibility** to **Public**, then create it.

:::{figure} ../images/new-github-repo.png
:alt: The Create a new repository form, with owner and repository name filled in and visibility set to Public in the Configuration section.

Visibility has to be Public for students to pull from the repository.
:::

Add your notebooks and data files with **Add file**, then **Upload files**.

:::{figure} ../images/new-github-repo-upload.png
:alt: A newly created public repository with the Add file menu open, showing Create new file and Upload files.

Upload your materials into the repository once it exists.
:::

Give some thought to the layout. The Data 8 materials keep `hw`, `lab`, `lectures`, and `project` at
the top level, with each assignment in its own folder next to the data files it needs.

:::{figure} ../images/public-repo.png
:alt: The materials-fds-v2 repository on GitHub, marked Public, with hw, lab, lectures, and project folders listed at the top level.

[ucb-dsus-adopters/materials-fds-v2](https://github.com/ucb-dsus-adopters/materials-fds-v2) as an
example of a layout that stays predictable across a term.
:::

A consistent layout pays off later, because it makes your links regular enough to edit by hand.

## Generate a link

We recommend the
[DataHub Link Generator](https://chromewebstore.google.com/detail/datahub-link-generator/ijbgangngghdanhcnaliiobbiffocahf)
Chrome extension. nbgitpuller also publishes a
[link generator form](https://nbgitpuller.readthedocs.io/en/latest/link.html) if you would rather not
install anything.

Open the notebook you want students to land on, on GitHub, then click the extension from the puzzle
icon in your browser toolbar. It reads the repository, branch, and file path from the page you are
looking at.

:::{figure} ../images/nbgitpuller.png
:alt: A notebook open on GitHub with the extension popup beside it, showing a JupyterHub URL field, an Open in dropdown, and a Copy nbgitpuller link button.

The extension fills in the repository and file path from whichever page you have open.
:::

Enter your hub address in **JupyterHub URL**. [Hub URL](../getting-started/hub-url.md) covers where
to find yours. Then choose what students should open in.

:::{figure} ../images/nbgitpuller-panel.png
:alt: The extension panel with the Open in dropdown expanded, listing Classic Notebook, JupyterLab, Shiny, RStudio, and VSCode.

Five targets are available. Classic Notebook opens the notebook by itself, and JupyterLab opens it
with the file browser alongside.
:::

Choose **Copy nbgitpuller link** and share it however your course reaches students.

## What the link contains

A generated link looks like this:

```
https://datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fucb-dsus-adopters%2Fmaterials-fds-v2&branch=main&urlpath=tree%2Fmaterials-fds-v2%2Fhw%2Fhw01%2Fhw01.ipynb
```

| Part | What it does |
|---|---|
| `https://datahub.berkeley.edu` | The hub the student is sent to |
| `/hub/user-redirect/git-pull` | Pulls into whichever account is signed in |
| `repo=` | The repository to copy, URL encoded |
| `branch=main` | The branch to pull from |
| `urlpath=` | The file to open once the copy finishes |

:::{warning}
The example above sends students to `datahub.berkeley.edu`, so only people with Berkeley accounts can
sign in to it. Put your own hub address in that position and the same link works for your course.
:::

The `urlpath` records where you were when you generated the link, so a link made from HW01 opens
HW01. If your repository has a consistent layout, you can copy a link and change `hw01` to `hw02`
rather than generating a new one.

## What happens when a student clicks

The whole repository copies into the student's space, and then the file named in `urlpath` opens.
They get everything, not just the one notebook, which is why the data files an assignment needs
should sit in the repository beside it.

:::{figure} ../images/datahub.png
:alt: Homework 1 open in the Classic Notebook interface, at a hub address under the signed-in user's own account showing the materials-fds-v2 repository path.

Where the link above lands. The repository now sits in the student's own space, and HW01 is open in
Classic Notebook, the target chosen when the link was made.
:::

Send the same link again later and nbgitpuller merges rather than overwrites:

- Files a student never touched pick up your changes.
- Where you both edited the same file in different places, both sets of edits survive.
- Where you both changed the same lines, the student's version wins.
- A student who deletes a file gets your copy back on the next click, which is how they start a
  question over.
- If a merge cannot be resolved, their work is copied to a backup folder before the fresh pull, so
  nothing is lost.

If a link does not behave the way you expect, [getting help](../getting-help.md) covers where to ask.
