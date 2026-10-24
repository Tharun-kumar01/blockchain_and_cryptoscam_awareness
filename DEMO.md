# Final Demo Script (5–7 minutes)
**Goal:** show that AI helped you *teach* blockchain and scam awareness safely, and that you verified it.

## Setup (before you start)
- Open: the GitHub repo page, `07_presentation_slides.pptx`, `06_infographic_red_flags.svg`, the repo's **Actions** tab, and a terminal in the project folder.

## Timeline
| Time | What you do | What you say |
|---|---|---|
| 0:00 | Show repo README | "This project uses AI to explain blockchain and teach scam recognition to college students. Education only, not financial advice." |
| 0:45 | Slides 1–2 | "A blockchain is a shared notebook; a wallet holds keys, not coins. Never share the seed phrase." |
| 1:45 | Open `04_scam_samples.md`, pick Sample 3 | "These are fictional training samples. Let's spot the red flags: wrong-number opener, profits shown, fee to withdraw." |
| 2:45 | Show infographic + checklist | "Two or more flags: stop. Pause, Verify, Report." |
| 3:30 | Quiz: ask the audience Q3 and Q9 live | "Answers are in the key with reasons." |
| 4:15 | Terminal: `python3 09_automation/weekly_tip_generator.py` | "This drafts a weekly tip from the checklist. A human reviews before posting, so nothing is auto-posted." |
| 5:00 | Actions tab: green "Project checks" | "CI checks 6 samples, 5 posts, 10 questions, 6 slides, no real brands or wallet addresses." |
| 5:30 | Open `11_verification_report.md` | "AI made mistakes: it put a real regulator name in a fake scam, stated a helpline without a source, and I could not find a CERT-In crypto advisory. I fixed or flagged each." |
| 6:15 | Ethics statement | "No coin promotion, no real brands, no financial advice, and I disclosed AI use." |

## Sample terminal output (from `demo/sample_run.txt`)
See `demo/sample_run.txt` for what the tip generator prints.

## Likely questions & answers
- **Did AI do all the work?** "AI drafted; I verified sources, tested errors, and edited." (Make this true: do the ☐ items in `SUBMISSION_CHECKLIST.md`.)
- **Is crypto legal in India?** "I didn't make legal claims. RBI's statements I used are cautions from 2013-2017, and rules change, so check current official sources."
- **What if the AI hallucinates?** "I used source-grounded prompts, 'mark UNVERIFIED', and a verification report."
- **Why not auto-post?** "Scam-awareness content must be accurate; a human approves."
