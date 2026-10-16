# Grading with Otter

[Otter](https://otter-grader.readthedocs.io/) grades Jupyter notebook assignments by running each
student's notebook against a set of tests and reporting a score per question. You give it two
things: the student notebooks, and the assignment's `autograder.zip`, which holds the tests and the
solutions. It gives you back a CSV of grades to upload to your LMS.

You do not need to install anything. There are two ways to run it:

- **In your browser.** [Otter Service In-Browser](https://ucb-dsus-adopters.github.io/tools/otter-grader/)
  runs the grading on your own computer. There is no login and no access to request, and nothing
  leaves your machine.
- **The hosted grader** at [grader.datahub.berkeley.edu](https://grader.datahub.berkeley.edu/). It runs
  the same grading on a server. You sign in with GitHub, so it needs a one-time authorization.

Both produce the same grades. The in-browser version is the quickest place to start.

## Get access

What you need depends on where your assignments come from.

**If you teach Data 8 from the shared materials**, complete the
[Instructor Interest Form](https://docs.google.com/forms/d/e/1FAIpQLSdvwtCh3Pog_vWhYOxlvcVLw6mBp6-tetZmLm4vAMGU0hHmkw/viewform)
and include your GitHub username. You will get two GitHub invitations. Accept both:

- the private solutions repository,
  [ucb-dsus-adopters/materials-fds-private-v2](https://github.com/ucb-dsus-adopters/materials-fds-private-v2),
  where each assignment's `autograder.zip` lives
- the [otter-service-stdalone](https://github.com/orgs/otter-service-stdalone) organization, which is
  what lets you sign in to the hosted grader

**If you wrote your own assignments with Otter**, you already have an `autograder.zip` from
`otter assign`. To use the hosted grader, email <help@cloudbank.org> with your GitHub username and we
will add you to the otter-service-stdalone organization. The in-browser version needs no access.

:::{warning} Please do not distribute solutions
Access to the private solutions repository is granted on the condition that solutions are not
shared or reposted. This protects the course materials for every institution that uses them.
:::

## Grade in your browser

1. Open [Otter Service In-Browser](https://ucb-dsus-adopters.github.io/tools/otter-grader/).
2. Upload the assignment's `autograder.zip`.
3. Upload the student submissions: individual notebooks, or the zip your LMS exports.
4. Add a batch for each assignment you are grading, and download the grades CSV for each batch.

## Grade with the hosted grader

This [five-minute screen recording](https://drive.google.com/file/d/1-r1kuUutn7ZXl3lSUgBbZAxLFuHoeFPp/view)
walks through the same steps.

1. **Sign in.** Once you have accepted the otter-service-stdalone invitation, sign in to
   [grader.datahub.berkeley.edu](https://grader.datahub.berkeley.edu/) with your GitHub account.
2. **Download the student submissions.** Export them from your LMS. You can grade a whole folder by
   zipping it and uploading the zip, or grade one notebook at a time by uploading the notebook itself.
3. **Download the `autograder.zip`.** For Data 8, open the
   [private solutions repository](https://github.com/ucb-dsus-adopters/materials-fds-private-v2),
   browse to the `autograder_zips` folder, and download the zip for the assignment you are grading.
4. **Upload and grade.** In the **Grade** section, upload the `autograder.zip` and the submissions,
   then select **Grade Notebooks**. A download code appears under the button. Keep it.
5. **Download the results.** Grading takes about a minute per ten notebooks. When it finishes, enter
   the code in the **Results** section. A folder downloads with a CSV of grades by notebook and a log
   file. If anything failed, check the log file first.

## Grading checklist

- [ ] Export all submissions from your LMS.
- [ ] Download the `autograder.zip` for the assignment.
- [ ] Grade, in your browser or on the hosted grader.
- [ ] Upload the grades CSV back to your LMS.

## Things to know

- **Students submit the notebook file.** Students run the export cell at the bottom of the notebook
  and upload the file it downloads. A screenshot or a PDF cannot be graded.
- **Use the zip that matches the assignment.** An `autograder.zip` from a different assignment, or
  from an older version of the materials, grades against the wrong tests.
- **Data 8 materials.** The full adoption guide, including Canvas setup and the student workflow, is
  on the [Data 8 adoption page](https://ucb-dsus-adopters.github.io/courses/data8/adoption/).
