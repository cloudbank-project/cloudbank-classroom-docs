# GitHub Copilot in VS Code

[GitHub Copilot](https://github.com/features/copilot) is an AI assistant that works inside VS Code.
It completes code as you type and has a Chat window where you can ask questions about your code,
have it explain an error, or ask it to make changes for you. VS Code on the hub already has the
Copilot extension installed. All you need is a GitHub account.

## Sign in to GitHub

1. Open VS Code from the JupyterHub launcher.
2. Click the **Accounts** icon at the bottom-left of the window.
3. Choose **Sign in with GitHub to use GitHub Copilot**.
4. Your browser opens a GitHub page. Sign in and click **Authorize**.

:::{figure} ../images/copilot-sign-in.png
:alt: The VS Code Accounts menu at the bottom-left with the option to sign in with GitHub to use GitHub Copilot.

The Accounts icon is at the bottom-left of VS Code.
:::

Once you are signed in, the Accounts icon shows your GitHub username.

:::{note}
Signing in does not give you more than your GitHub plan allows. A free account works, with the
limits listed in [Plans and pricing](#copilot-plans).
:::

## Open the Chat window

Click the **Chat** icon at the top of the window, or press {kbd}`Ctrl+Alt+I`
({kbd}`Ctrl+Cmd+I` on a Mac). The Chat window opens in the **Secondary Side Bar** on the right.

:::{figure} ../images/copilot-chat-open.png
:alt: VS Code with the Copilot Chat window open on the right-hand side next to a Python file.

Chat opens on the right, next to your code.
:::

## Use Chat

Type a question in the box at the bottom of the Chat window and press {kbd}`Enter`.

- **Ask about your code.** Open a file first and Chat uses it as context. Select a few lines to
  make it focus on those.
- **Explain an error.** Paste the error message, or ask "why did this cell fail?"
- **Ask for changes.** Describe what you want ("add a docstring to this function") and Chat
  proposes an edit you can accept or reject.
- **Pick a mode.** The dropdown beside the input switches between asking questions and letting
  Copilot make edits across your files. Use the question mode if you only want an explanation.

:::{figure} ../images/copilot-chat-answer.png
:alt: A Copilot Chat conversation explaining a Python error, with the suggested fix shown as a code block.

Chat explaining an error and suggesting a fix.
:::

:::{warning}
Copilot can be wrong, and it sometimes states wrong answers confidently. Read what it suggests
and run it before you rely on it. If you are a student, check your course's AI policy before
submitting anything Copilot wrote.
:::

## Move Chat into the main editing area

Chat does not have to stay in the side bar. To get a full-size Chat in an editor tab, the way the
Claude Code extension works:

1. Click the **New Chat (+)** button at the top of the Chat window.
2. Choose **New Chat Editor**.

You can also open the Command Palette ({kbd}`Ctrl+Shift+P`) and run **Chat: New Chat Editor**.
The chat opens as a tab you can drag beside your code, split, or leave full width. **Chat: New
Chat Window** opens it in a separate window instead.

:::{figure} ../images/copilot-chat-editor.png
:alt: Copilot Chat open as a tab in the main editor area, split beside a Python file.

Chat as an editor tab, next to a file.
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
