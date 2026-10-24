# Git & GitHub Guide for Beginners
Pick **Method 1** (no installs) if you've never used Git.

## Method 1 — Upload in the browser (easiest)
1. Go to https://github.com and sign up / log in.
2. Click **+** (top right) → **New repository**.
3. Name it `crypto-scam-awareness`. Choose **Public**. Don't tick any "Add a README" boxes. Click **Create repository**.
4. Unzip `crypto-scam-awareness.zip` on your computer.
5. On the new repo page click **uploading an existing file**.
6. Open the unzipped folder and **drag all the files and folders** (including `09_automation`, `tests`, `demo`) into the browser window.
7. **Hidden folder warning:** the `.github` folder (it holds the CI workflows) may not upload by drag-and-drop on some computers. If it's missing: click **Add file → Create new file**, type `.github/workflows/ci.yml` as the name, paste the contents of that file, and commit. Repeat for `weekly-tip.yml`.
8. Write a commit message such as `Add project files` and click **Commit changes**.
9. Click the **Actions** tab. You should see "Project checks" running, then a green ✅.

## Method 2 — Command line (when you're ready)
Install Git from https://git-scm.com, then in a terminal:
```bash
cd crypto-scam-awareness
git init
git add .
git commit -m "Initial commit: crypto scam awareness project"
git branch -M main
git remote add origin https://github.com/<your-username>/crypto-scam-awareness.git
git push -u origin main
```
GitHub will ask you to sign in (use a browser login or a Personal Access Token as the password).

## Everyday commands
| What | Command |
|---|---|
| See what changed | `git status` |
| Save changes | `git add .` then `git commit -m "describe change"` |
| Upload | `git push` |
| Download latest | `git pull` |

## Good commit messages
`Fix sample 2 wording`, `Add verification results for Gemini`, `Update quiz key` (short, say what changed).

## If CI fails (red ❌)
1. Open **Actions** → click the failed run → read the red line. It names the check, e.g. `deck has 6 slides`.
2. Fix the file, commit again. CI re-runs automatically.
3. Run `python3 tests/check_project.py` on your computer to test before pushing.

## Manual run of the weekly tip workflow
GitHub → **Actions** → "Weekly scam-tip draft" → **Run workflow**. Download the draft from the run's **Artifacts**. It never posts anything by itself.

## Safety rules
- Never commit passwords, API keys or personal data (`.env` is already in `.gitignore`).
- Never add real wallet addresses, real scam links or victims' details.
- Mention AI help in your README (already included).
