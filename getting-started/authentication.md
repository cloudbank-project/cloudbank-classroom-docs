# Authentication

Most CloudBank Classroom hubs sign you in through CILogon. You do not create an account for the
hub. You use the account your institution already gave you, and CILogon reaches it through either
Google or Microsoft.

A small number of hubs sign in with GitHub instead. If yours does, see
[Hubs that sign in with GitHub](#hubs-that-sign-in-with-github) below — those hubs need a step the
CILogon ones do not.

## Signing in

Go to [your hub's address](hub-url.md). CILogon asks which identity provider to use and offers
Microsoft and Google. Choose the one your institution uses. If you check "Remember this selection",
CILogon skips this step next time.

:::{figure} ../images/CILogon.png
:alt: The CILogon sign-in page. A Consent to Attribute Release panel sits above a Selected Identity Provider panel, where an open dropdown offers two choices, Microsoft and Google.

Choosing an identity provider on the CILogon sign-in page.
:::

## Use your institutional account

A personal Gmail or Outlook address will not get you into the hub. Sign in with the address your institution issued you.

:::{note}
A browser already signed in to a personal Google or Microsoft account can carry that account into
the sign-in and leave you unable to reach the hub. Sign out of the personal account first, or open
your hub in a private or incognito window.
:::

If your institutional account does not get you in, [getting help](../getting-help.md) covers where
to ask.

## Hubs that sign in with GitHub

**Most hubs do not use this.** Of the hubs running today, 14 sign in with GitHub and the rest use
CILogon or Google. You can tell which one you have by opening your hub: a CILogon hub shows the
identity-provider chooser pictured above, and a GitHub hub sends you to github.com instead.

On a GitHub hub, access is controlled by membership of a **GitHub organization**. Being enrolled in
the course is not enough on its own — someone has to add each person to the organization before
they can log in.

### For students

You need a GitHub account, and you need to be a member of the course's organization.

1. Your instructor sends you an invitation. GitHub emails it to you, and it also appears at
   `https://github.com/orgs/<organization>/invitation`.
2. **Accept the invitation.** This is the step people miss. Until you accept, you are not a member,
   and the hub turns you away exactly as though you had never been invited.
3. Go to your hub and sign in with GitHub. The first time, GitHub asks you to authorize the hub's
   application.

Your membership can stay private — the hub asks GitHub only whether you are a member, so you do not
need to show your membership publicly.

### For instructors: adding someone to the organization

1. Go to `https://github.com/orgs/<your-organization>/people`.
2. Select **Invite member**.
3. Enter their GitHub username, or the email address attached to their GitHub account.
4. Leave the role as **Member**. Owner is not needed, and grants far more than hub access.
5. Send the invitation, then tell them to go and accept it.

:::{note}
Organization invitations expire after seven days. If a student says they cannot get in, check
whether their invitation is still pending or has lapsed — on the **People** page, pending invites
are listed separately under **Pending invitations**.
:::

:::{warning}
Being an owner of the GitHub organization does not make you an admin on the hub. Hub admins are set
separately in the hub's configuration — see [Getting Help](../getting-help.md) to have someone
added.
:::

Two things worth knowing on a GitHub hub. Usernames come from GitHub, not from your institutional
email, so a student who renames their GitHub account arrives as a new user with an empty home
directory. And removing someone from the organization removes their access to the hub at their next
sign-in, though their files stay where they are.

