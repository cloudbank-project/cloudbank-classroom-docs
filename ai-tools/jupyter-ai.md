# Jupyter AI

[Jupyter AI](https://jupyter.org/ai) is a JupyterLab extension that connects AI agents to your
notebooks. It adds a chat panel beside your work, and the agent you talk to can read and write
files, run terminal commands, and edit notebooks for you. Before an agent writes a file or runs a
command, it asks you to approve the action.

Jupyter AI connects to agents through the [Agent Client Protocol](https://agentclientprotocol.com),
so it works with tools like Claude, Codex, and OpenCode. We can install these on your hub, but we
don't provide accounts for them. Each one needs your own API key or subscription.

## Getting it on your hub

Jupyter AI isn't in the standard environment. Ask for it like any other package. See
[Requesting Packages](../environments/packages.md).

Tell us how you want model access to work. Some hubs have a shared API key everyone in the course
can use. On others, each person adds their own. Agents like Claude or Codex still need your own key
or subscription either way.

:::{warning}
Jupyter AI is new and changes quickly, so what you see may not match its docs. Model usage is
billed per token, and we can't promise unlimited use.
:::

## Using the chat

Open the chat panel from the left sidebar, click **New chat**, and give it a name. Type in the box
at the bottom. The agent answers in the panel, and your notebook stays open next to it.

:::{figure} ../images/JupyterAI.png
:alt: JupyterLab with the Jupyter AI chat panel docked on the left. A short exchange ends in a reply from OpenCode, and a notebook running a print statement is open on the right.

The chat panel sits beside your notebook, so you can work and ask questions in the same window.
:::

Each chat is saved as a `.chat` file. Logging out doesn't lose your chats. Open the file to pick up
where you left off.

## Models and API keys

Jupyternaut is an optional agent you can add to Jupyter AI. It uses
[LiteLLM](https://docs.litellm.ai/), which works with many providers. Pick one under **Settings**,
then **Jupyternaut settings**. Add the provider's API key on the same page with **Add secret**.

:::{figure} ../images/Jupyternaut.png
:alt: The Settings menu open over the Jupyternaut settings page, showing a Jupyternaut settings entry in the menu and a secrets section listing OPENAI_API_KEY below.

Model selection and API keys both live under Settings, then Jupyternaut settings.
:::

If your hub has a shared key, it is already in the secrets list. You can't change it from this
page. Email us if it needs to change.

## Personas

A persona is another assistant in the same chat, like a bot in Slack. Each one has its own
instructions and model, and it only answers when you mention it. Type `@` in the message box to see
your hub's personas, then pick one and type your question.

:::{figure} ../images/Personas.png
:alt: A Jupyter AI chat with the at-mention picker open, listing Jupyternaut, Claude, Codex, and a custom Otter Grader Helper. The Python source for that custom persona is open in an editor tab alongside.

One example. Along with the built-in personas, this hub has a custom Otter Grader Helper, defined
in the Python file open on the right.

:::

To write your own, you define a persona class and install it on the hub. The
[jupyter-ai-personas](https://github.com/jupyter-ai-contrib/jupyter-ai-personas) repository shows
how and has several examples.

See the [Jupyter AI docs](https://github.com/jupyterlab/jupyter-ai) for more. Questions? See
[Getting help](../getting-help.md).
