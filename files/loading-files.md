# Loading Files onto the Hub

[nbgitpuller](https://nbgitpuller.readthedocs.io/) gives a whole class a copy of your materials from
one link. A student clicks it, the files are copied into their own storage on the hub's disk, and
the notebook you picked opens. Nobody needs to know git. The easiest way to make the link is the
[DataHub Link Generator](https://chromewebstore.google.com/detail/datahub-link-generator/ijbgangngghdanhcnaliiobbiffocahf)
Chrome extension. See [Generate a link](#generate-a-link).

You need two things: your materials in a public GitHub repository, and a link to them.

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

Plan your folders. The Data 8 materials keep `hw`, `lab`, `lectures`, and `project` at the top
level, with each assignment in its own folder next to the data files it needs.

:::{figure} ../images/public-repo.png
:alt: The materials-fds-v2 repository on GitHub, marked Public, with hw, lab, lectures, and project folders listed at the top level.

[ucb-dsus-adopters/materials-fds-v2](https://github.com/ucb-dsus-adopters/materials-fds-v2) as an
example of a layout that stays predictable across a term.
:::

If your folders follow a pattern, you can edit your links by hand later.

## Generate a link

We recommend the
[DataHub Link Generator](https://chromewebstore.google.com/detail/datahub-link-generator/ijbgangngghdanhcnaliiobbiffocahf)
Chrome extension. If you don't want to install anything, nbgitpuller also has a
[link generator form](https://nbgitpuller.readthedocs.io/en/latest/link.html).

Open the notebook you want students to land on, on GitHub, then click the extension from the puzzle
icon in your browser toolbar. It reads the repository, branch, and file path from the page you are
looking at.

:::{figure} ../images/nbgitpuller.png
:alt: A notebook open on GitHub with the extension popup beside it, showing a JupyterHub URL field, an Open in dropdown, and a Copy nbgitpuller link button.

The extension fills in the repository and file path from whichever page you have open.
:::

Enter your hub address in **JupyterHub URL**. See [Hub URL](../getting-started/hub-url.md) to find
yours. Then choose what students should open in.

:::{figure} ../images/nbgitpuller-panel.png
:alt: The extension panel with the Open in dropdown expanded, listing Classic Notebook, JupyterLab, Shiny, RStudio, and VSCode.

Five targets are available. Classic Notebook opens the notebook by itself, and JupyterLab opens it
with the file browser alongside.
:::

Click **Copy nbgitpuller link** and send it to your students.

### Landing students in a folder instead of a notebook

A link made from a notebook page opens that notebook. Sometimes you want students to land in a
folder instead, like a lab folder with its data files, and pick the file themselves.

Open the **folder** on GitHub instead of a notebook, then use the extension the same way. A folder
page gives you a folder link.

If you already have a notebook link, you can shorten it by hand. Delete the file name from the end
of `urlpath`, leaving the folder:

```
...&urlpath=tree%2Fmaterials-fds-v2%2Fhw%2Fhw01%2Fhw01.ipynb    opens hw01.ipynb
...&urlpath=tree%2Fmaterials-fds-v2%2Fhw%2Fhw01                 opens the hw01 folder
```

What students see on arrival depends on the target you picked in **Open in**: JupyterLab shows the
folder in the file browser, and Classic Notebook shows a directory listing.

:::{note}
The whole repository is copied either way. `urlpath` only decides where the student lands, so a
folder link doesn't give students just part of a repository.
:::

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
The example above goes to `datahub.berkeley.edu`, so only people with Berkeley accounts can sign
in. Put your own hub address there and the same link works for your course.
:::

The `urlpath` is the page you were on when you made the link, so a link made from HW01 opens HW01.
If your folders follow a pattern, you can copy a link and change `hw01` to `hw02` instead of making
a new one.

## What happens when a student clicks

The whole repository copies into the student's storage, then the file in `urlpath` opens. They
get everything, not just one notebook, so put an assignment's data files next to it in the
repository.

:::{figure} ../images/datahub.png
:alt: Homework 1 open in the Classic Notebook interface, at a hub address under the signed-in user's own account showing the materials-fds-v2 repository path.

Where the link above lands. The repository now sits in the student's own space, and HW01 is open in
Classic Notebook, the target chosen when the link was made.
:::

If you send the same link again later, nbgitpuller merges your changes. It doesn't overwrite the
student's work:

- Files a student never touched pick up your changes.
- Where you both edited the same file in different places, both sets of edits survive.
- Where you both changed the same lines, the student's version wins.
- A student who deletes a file gets your copy back on the next click. That is how they start a
  question over.
- If a merge can't be worked out, their work is copied to a backup folder first, so nothing is
  lost.

If your hub has server options, students see a Server Options page (CPU or GPU, and an image)
before the link runs. To skip that page too, see [Autostart Links](autostart-links.md).

Questions? See [Getting help](../getting-help.md).
