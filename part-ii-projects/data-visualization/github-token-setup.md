# Setting up a GitHub token for the training scripts

The chapter 17 scripts call the GitHub API. Without a token, GitHub allows 60 requests per hour from your computer. The chapter's exercises can use that up quickly, and then the scripts fail with a `403` status code until the limit resets.

With a token, the limit rises to 5,000 requests per hour. The scripts read the token from an environment variable called `GITHUB_TRAINING_TOKEN`. The token is never written into the code, so it can't end up in version control or in a shared file.

If the variable isn't set, the scripts still run, without authentication.

---

## 1. Create a classic token

GitHub's fine-grained token form doesn't offer the read-only option these scripts need, so create a classic token.

1. Sign in to GitHub, click your avatar, and choose **Settings**.
2. Scroll down and open **Developer settings**, then **Personal access tokens**, then **Tokens (classic)**.
3. Click **Generate new token**, then **Generate new token (classic)**.
4. Enter a name, such as `Python training`, and an expiration date.
5. Leave every scope unchecked. Reading public repositories needs no scopes.
6. Click **Generate token**.
7. Copy the token now. GitHub shows it only once.

A token with no scopes can read public data, and that's all the scripts do.

---

## 2. Set the environment variable

Set a user environment variable, so it's available to every program you run under your account.

**PowerShell (quickest):**

```powershell
[Environment]::SetEnvironmentVariable("GITHUB_TRAINING_TOKEN", "paste-your-token-here", "User")
```

Replace `paste-your-token-here` with the token you copied. Run the command once.

**Windows Settings:**

1. Open **Settings**, then **System**, then **About**, then **Advanced system settings**.
2. Click **Environment Variables**.
3. Under **User variables**, click **New**.
4. Enter `GITHUB_TRAINING_TOKEN` as the name, and paste the token as the value.
5. Click **OK** on each dialog.

---

## 3. Restart anything that reads the variable

Programs read environment variables when they start, so the variable won't reach a program that was already running.

- Close the lesson runner and reopen it.
- Close any open terminals or editors, then reopen them.

---

## 4. Check that it works

Run the 3rd Edition chapter 17 lesson **Checking API Limits** (lesson 1.5). The `limit` for `core` should show `5000`, not `60`. If it still shows `60`, the variable isn't reaching the program. Restart the runner, then check again.

---

## Keeping the token safe

- Don't paste the token into a lesson, a script, or a message.
- Don't commit it to version control.
- If you think someone else has the token, delete it under **Tokens (classic)** and create a new one.
- Set an expiration date, and create a new token when the old one expires.
