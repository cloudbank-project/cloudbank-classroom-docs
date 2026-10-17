# GitHub Copilot in VS Code

[GitHub Copilot](https://github.com/features/copilot) is an AI assistant that works inside VS Code.
It completes code as you type and has a Chat window where you can ask questions about your code,
have it explain an error, or ask it to make changes for you. VS Code on the hub already has the
Copilot extension installed. All you need is a GitHub account.

## Sign in to GitHub

1. Open VS Code from the JupyterHub launcher.
2. Look for the sign-in in both of these places. Which one you see depends on your VS Code
   version, and either works:
   - the **Copilot** icon labeled **Sign In** at the bottom-right of the window
   - the **Accounts** icon at the bottom-left of the window

:::{figure} ../images/copilot-sign-in-status-bar.png
:alt: The VS Code status bar at the bottom-right showing a Copilot icon with the label Sign In.

The **Sign In** button next to the Copilot icon in the bottom-right status bar.
:::

:::{figure} ../images/copilot-sign-in-accounts.png
:alt: The Accounts icon, a person in a circle, above the gear icon at the bottom-left of VS Code.

The **Accounts** icon, the person above the gear at the bottom-left.
:::

3. Choose the option to sign in with GitHub. VS Code shows a one-time code. Click
   **Copy & Continue to Browser**.

:::{figure} ../images/copilot-sign-in-code.png
:alt: A VS Code dialog showing a one-time code and a Copy & Continue to Browser button.

VS Code shows a one-time code and copies it for you.
:::

4. VS Code asks whether to open an external website. Click **Open**.

:::{figure} ../images/copilot-sign-in-open-site.png
:alt: A dialog asking whether code-server may open the GitHub device login page, with an Open button.

Allow the GitHub login page to open.
:::

5. On the GitHub page, check that it says you are signed in as the right account, then click
   **Continue**.

:::{figure} ../images/copilot-sign-in-continue.png
:alt: The GitHub Device Activation page showing the signed-in username and a green Continue button.

Confirm the GitHub account and click **Continue**.
:::

6. Paste the one-time code that VS Code copied, then click **Continue**.

:::{figure} ../images/copilot-sign-in-enter-code.png
:alt: The GitHub page with eight boxes for the one-time device code and a green Continue button.

Paste the code into the boxes.
:::

7. Click **Authorize Visual-Studio-Code**. Return to the VS Code tab.

:::{figure} ../images/copilot-sign-in-authorize.png
:alt: The GitHub authorization page with a Cancel button and a green Authorize Visual-Studio-Code button.

Authorize VS Code to use your GitHub account.
:::

Once you are signed in, Copilot shows as ready and Chat accepts questions.

:::{note}
Signing in does not give you more than your GitHub plan allows. A free account works, with the
limits listed in [Plans and pricing](#copilot-plans).
:::

## Open the Chat window

Press {kbd}`Ctrl+Alt+I` ({kbd}`Ctrl+Cmd+I` on a Mac), or open the Command Palette and run
**Chat: Open Chat**. The Chat window opens in the **Secondary Side Bar** on the right, with your
earlier conversations listed under **Sessions**.

:::{figure} ../images/copilot-chat-open.png
:alt: VS Code with the Chat window open on the right-hand side, listing two earlier sessions above an input box that reads Describe what to build.

Chat opens on the right, with past sessions listed above the input box.
:::

## Use Chat

Type a question in the box at the bottom of the Chat window and press {kbd}`Enter`.

- **Ask about your code.** Open a file first and Chat uses it as context. Select a few lines to
  make it focus on those.
- **Explain an error.** Paste the error message, or ask "why did this cell fail?"
- **Ask for changes.** Describe what you want ("add a docstring to this function") and Chat
  proposes an edit you can accept or reject.
- **Pick a mode.** The mode picker below the input box, labeled **Agent** by default, controls how
  Copilot works. Agent mode can make edits across your files, so switch to a question-only mode
  if you just want an explanation.

:::{figure} ../images/copilot-chat-answer.png
:alt: A Chat conversation in which the question "I am working on learning datascience - what is the first step" is answered with a five-step numbered list, followed by thumbs up, thumbs down and copy buttons.

A question and Copilot's answer. The buttons under the answer let you copy it, rate it, or regenerate it.
:::

:::{warning}
Copilot can be wrong, and it sometimes states wrong answers confidently. Read what it suggests
and run it before you rely on it. If you are a student, check your course's AI policy before
submitting anything Copilot wrote.
:::

## Move Chat into the main editing area

Chat does not have to stay in the side bar. To get a full-size Chat in an editor tab, the way the
Claude Code extension works:

1. Open the Command Palette with {kbd}`Ctrl+Shift+P` ({kbd}`Cmd+Shift+P` on a Mac).
2. Type `New Chat`.
3. Choose one of the Chat commands:
   - **Chat: New Chat Editor** opens Chat as a tab in the main editing area.
   - **Chat: New Chat Editor to the Side** opens it as a tab beside the file you are editing.
   - **Chat: New Chat Window** opens it in a separate window.

:::{figure} ../images/copilot-new-chat-palette.png
:alt: The VS Code Command Palette filtered to New Chat, listing New Chat Editor, New Chat Editor to the Side and New Chat Window.

The New Chat commands in the Command Palette.
:::

The chat opens as a tab you can drag, split, or leave full width. The **New Chat (+)** button at
the top of the Chat window has the same options.

**New Chat Window** opens Chat in its own window, which you can move to a second screen.

:::{figure} ../images/copilot-chat-window.png
:alt: A small separate window titled Chat showing the Copilot Chat input box, floating over VS Code.

Chat in its own window.
:::

:::{figure} ../images/copilot-chat-editor.png
:alt: Copilot Chat open as a tab named Chat in the main editor area, next to the Explorer file list.

Chat as a tab in the main editing area, with the file Explorer still on the left.
:::

(copilot-plans)=
## Plans and pricing

Copilot is free to start and has paid tiers for heavier use. These are the individual plans listed
on [GitHub's plans page](https://github.com/features/copilot/plans) as of October 2026. Prices
and allowances change, so check that page before you buy anything.

| Plan | Price per month | Included usage | What you get |
|---|---|---|---|
| **Free** | $0 | 2,000 inline completions and 50 chat requests | Chat and agent mode with limited use. No code review or cloud agent. |
| **Pro** | $10 | $15 in GitHub AI Credits ($10 base + $5 flex) | Unlimited inline completions, agent mode, code review, cloud agent, Copilot CLI, MCP servers. You can buy more credits. |
| **Pro+** | $39 | $70 in credits ($39 base + $31 flex) | Everything in Pro, plus delegating tasks to third-party agents such as Claude and OpenAI Codex (Preview). |
| **Max** | $100 | $200 in credits ($100 base + $100 flex) | Same features as Pro+, for heavy and sustained agent-driven use. |

How usage is counted:

- Chat and agent requests use **GitHub AI Credits**. One credit is $0.01.
- Inline completions are unlimited on paid plans and do not use credits.
- All four plans can use the same set of models.
- **Business and Enterprise** plans are for organizations and are sold through GitHub sales. The
  plans page does not list a price for them.

:::{tip}
Students and teachers can often get Copilot at no cost through
[GitHub Education](https://github.com/education). Apply there before paying for a plan.
:::
