# Autostart Links

A hub normally shows a server options page after sign-in, and a student has to pick settings and
press start. An autostart link skips that page. The student signs in, their server starts with the
settings you chose, and they land where you want them.

:::{note}
Autostart needs a hub running jupyterhub-fancy-profiles 0.7.0 or newer. A link made for a hub that
does not have it still signs the student in, but they will see the options page as usual.
:::

## Make a link

Open the [Autostart Link Builder](https://cloudbank-project.github.io/autostart-link-builder/).

1. On your hub's server options page, pick the settings students should get and choose
   **Copy Permalink**. Paste it into the first box.
2. If you also want students to receive your materials, paste an nbgitpuller link for the same hub
   into the second box. [Loading Files onto the Hub](loading-files.md) covers making one. Leave the
   box empty to start the server only.
3. Choose **Copy link** and share it with your class.

The builder works in your browser and sends nothing anywhere.

## What each combination does

| You paste | The link does |
|---|---|
| Permalink only | Signs the student in and starts their server with your settings |
| Permalink and nbgitpuller link | Signs in, starts the server with your settings, then pulls your repository and opens the file you chose |

With the permalink alone you get the same link the hub gave you. The only change is that automatic
start is switched on. The **Copy Permalink** button always writes it switched off, which is why a
link copied straight from the hub still shows the options page.

## Things to know

- **Both links have to be for the same hub.** The builder refuses a pair that point at different
  hubs.
- **A student who already has a server running** goes straight to the pull, or straight to their
  server, without starting a second one.
- **Profiles with the custom image builder** can skip autostart when the builder needs input from
  the student, and nothing tells them why. The builder warns you when it sees one. Try the link
  yourself before it goes into a syllabus.
- **Try it first.** The builder's **Try it** button opens the link in a new tab.

If a link does not behave the way you expect, [getting help](../getting-help.md) covers where to ask.
