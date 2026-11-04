# Authentication

Most CloudBank Classroom hubs sign you in through CILogon. You don't make an account for the hub.
You use the account your school already gave you, and CILogon sends you to your school's own login:
Google, Microsoft, or a login page your school runs itself.

A few hubs use GitHub instead. If yours does, see
[Hubs that sign in with GitHub](#hubs-that-sign-in-with-github) below. Those hubs need an extra
step.

## Signing in

Go to [your hub's address](hub-url.md). CILogon asks you to pick an identity provider. Most hubs
show Google plus either Microsoft or your school's own login, listed under your school's name. Pick
the one your school uses. If you check "Remember this selection", CILogon skips this step next
time.

:::{figure} ../images/CILogon.png
:alt: The CILogon sign-in page. A Consent to Attribute Release panel sits above a Selected Identity Provider panel, where an open dropdown offers two choices, Microsoft and Google.

Choosing an identity provider on the CILogon sign-in page.
:::

## Use your institutional account

A personal Gmail or Outlook address won't get you into the hub. Use your school email.

:::{note}
If your browser is already signed in to a personal Google or Microsoft account, it may use that
account and you won't get in. Sign out of the personal account first, or open your hub in a
private or incognito window.
:::

If your school account doesn't get you in, see [Getting help](../getting-help.md).

## When Microsoft asks for admin approval

At some schools that use Microsoft, you get a screen saying **"Need admin approval"**, with
CILogon listed as an unverified app.

Your account and the hub are fine. Microsoft needs your school's IT to approve CILogon once for the
whole school. Until they do, nobody at your school can sign in with Microsoft, and students and
instructors can't fix it from their own accounts.

:::{note}
This only happens at schools that use Microsoft. Schools that use Google or their own login never
see this screen.
:::

"Unverified" is just Microsoft's label for apps it hasn't checked the publisher of. It doesn't
mean anything is unsafe. The permissions CILogon asks for are listed on that screen.

### For instructors: what to send IT

Send the text below to whoever manages Microsoft 365 or Entra at your school. Replace
`{Institution}`, `{hub}` and `{domain}`. It answers the questions IT usually asks.

```text
We are asking you to grant admin consent for CILogon in your Microsoft Entra tenant so faculty and
students at {Institution} can sign in to a JupyterHub used for coursework at
{hub}.cloudbank.2i2c.cloud.

What CILogon is. A federated identity service operated by NCSA at the University of Illinois
Urbana-Champaign under NSF funding, used widely across research and higher education.
Documentation: https://www.cilogon.org/faq

Why it says "unverified." That is Microsoft's publisher-verification label, not a security
finding. The permissions being requested are listed on the consent screen itself.

What it actually does:

- Credentials never leave your environment. Users are redirected to your own Microsoft login page
  and authenticate there. Nothing is typed into the hub.
- Your MFA still applies, because your tenant is performing the authentication.
- The only attribute we receive is the email address. It is used as the username, and nothing else
  is read, stored, or transferred.
- No accounts are provisioned on our side. There is no user list to maintain - if an account is
  disabled at the college, that person can no longer sign in.
- Access is limited to @{domain}. Any other domain is rejected by the hub regardless of what Entra
  allows.

To approve: an Entra admin can use the "Have an admin account? Sign in with that account" link on
the screen the user hit, or grant consent for CILogon under Enterprise applications in the Entra
admin center.
```

Once IT approves it, everyone at your school can sign in. They only have to do it once.

If IT has other questions, email us. See [Getting help](../getting-help.md).

## Hubs that sign in with GitHub

**Most hubs don't use this.** Right now 14 hubs sign in with GitHub and the rest use CILogon or
Google. Open your hub to see which one you have. A CILogon hub shows the identity provider page
pictured above. A GitHub hub sends you to github.com.

On a GitHub hub, you get in by being a member of a **GitHub organization**. Being in the course
isn't enough. Someone has to add each person to the organization before they can log in.

### For students

You need a GitHub account, and you need to be a member of the course's organization.

1. Your instructor sends you an invitation. GitHub emails it to you, and it also appears at
   `https://github.com/orgs/<organization>/invitation`.
2. **Accept the invitation.** This is the step people miss. Until you accept, you aren't a
   member, and the hub won't let you in.
3. Go to your hub and sign in with GitHub. The first time, GitHub asks you to authorize the hub's
   application.

Your membership can stay private. The hub only checks that you are a member.

### For instructors: adding someone to the organization

1. Go to `https://github.com/orgs/<your-organization>/people`.
2. Select **Invite member**.
3. Enter their GitHub username, or the email address attached to their GitHub account.
4. Leave the role as **Member**. They don't need Owner.
5. Send the invitation, then tell them to accept it.

:::{note}
Invitations expire after seven days. If a student can't get in, check if their invitation is
still pending or expired. On the **People** page, look under **Pending invitations**.
:::

:::{warning}
Being an owner of the GitHub organization doesn't make you an admin on the hub. We set hub admins
separately. Email us to add someone. See [Getting Help](../getting-help.md).
:::

Two more things about GitHub hubs:

- Usernames come from GitHub, not your school email. If a student renames their GitHub account,
  they show up as a new user with an empty home directory.
- If you remove someone from the organization, they lose access the next time they sign in. Their
  files stay on the hub.

