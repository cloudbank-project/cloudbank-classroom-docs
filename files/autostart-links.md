# Autostart Links

Some hubs offer a choice of server types when a student signs in, such as a CPU-only server and a
GPU server, each with its own images. Only hubs set up this way have the Server Options page below,
and only they can use autostart links.

:::{figure} ../images/server-options.png
:alt: The Server Options page with a CPU only profile selected and a GPU profile below it, each with an Image dropdown, a Copy Permalink link at the top right, and an orange Start button.

The Server Options page. Each profile has its own images, and Copy Permalink sits at the top right.
:::

Normally a student signs in, picks a profile and an image on this page, and presses **Start**. An
autostart link skips the page. The student signs in and their server starts with the profile and
image you chose.

:::{note}
Autostart needs a hub running jupyterhub-fancy-profiles 0.7.0 or newer. A link made for a hub that
does not have it still signs the student in, but they will see the options page as usual.
:::

## Make a link

1. Open your hub, choose the profile and image you want students to get, and select
   **Copy Permalink**.
2. Open the [Autostart Link Builder](https://cloudbank-project.github.io/autostart-link-builder/)
   and paste the permalink into the first box.
3. Optional: to also give students your materials, paste an nbgitpuller link for the same hub into
   the second box. [Loading Files onto the Hub](loading-files.md) covers making one. Leave the box
   empty to start the server only.
4. Choose **Copy link** and share it with your class.

## What each combination does

| You paste | The link does |
|---|---|
| Permalink only | Signs the student in and starts their server with the image your permalink includes |
| Permalink and nbgitpuller link | Signs in, starts the server with the image your permalink includes, then pulls your repository and opens the file you chose |

With the permalink alone you get the same link the hub gave you. The only change is that automatic
start is switched on. The **Copy Permalink** button always writes it with autostart set to false,
and the link builder sets it to true.

## Things to know

- **Both links have to be for the same hub.** The builder refuses a pair that point at different
  hubs.
- **A student who already has a server running** goes straight to the pull, or straight to their
  server, without starting a second one. A student who needs to switch between GPU and CPU
  machines should first choose **File > Hub Control Panel** and press **Stop Server**, then use
  the link.
- **Try it first.** The builder's **Try it** button opens the link in a new tab.

If a link does not behave the way you expect, [getting help](../getting-help.md) covers where to ask.
