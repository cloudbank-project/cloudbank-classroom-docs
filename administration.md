# Admin Dashboard

If you have admin access on your hub, JupyterHub gives you a dashboard with everyone on the hub.
You can restart a stuck server or open a student's environment to see what they see.

## Reaching the dashboard

Add `/hub/admin` to your hub address:

```
https://<campus>.cloudbank.2i2c.cloud/hub/admin
```

See [Hub URL](getting-started/hub-url.md) to find your address.

If the dashboard doesn't load, you don't have admin access yet. Email us and we will add you. See
[Getting help](getting-help.md).

## The user list

The dashboard lists every account on the hub. For each one you can see whether it is an admin,
whether its server is running, and when the person was last active.

:::{figure} images/admin.png
:alt: The JupyterHub admin dashboard, with a username typed into the search box and one matching account below it, showing admin status, a last activity of Never, and Start Server, Spawn Page, and Edit User buttons.

Searching for one student and the buttons for their account.
:::

Use the search box to find a student, and check **only active servers** to see who is working
right now.

Usernames are the first part of the student's school email, so `jedwin321@berkeley.edu` shows up
as `jedwin321`.

## Starting and stopping servers

**Start Server** and **Stop Server** work on one student. If a student's session is stuck, stop it
and start it again. Their files are not affected.

:::{warning}
**Start All**, **Stop All**, and **Shutdown Hub** are in the same row as the single-student
buttons, but they affect everyone. **Shutdown Hub** takes down the whole hub, even in the middle of
a lab.
:::

## Opening a student's server

**Access Server** opens the student's environment as that student. You see their files and
notebooks as they left them, so you can see the problem yourself.

The button only shows up while the student's server is running. If you see **Start Server**
instead, start the server first.

:::{note}
Access Server shows the student's own work. Follow your institution's policy about looking at
student files.
:::

Questions? See [Getting help](getting-help.md).
