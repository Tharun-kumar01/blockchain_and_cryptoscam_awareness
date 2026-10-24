#!/usr/bin/env python3
"""
09_automation.py  -  Weekly scam-alert tip drafter (single file)

WHAT IT DOES
  Picks one red flag from the checklist (rotating by ISO week) and writes a
  ready-to-edit social-media tip as a DRAFT. It never posts anything.
  A human must review and approve every tip (see 13_ethics_statement.md).

HOW TO RUN
  python3 09_automation.py                 # draft for this week
  python3 09_automation.py --week 10       # draft for a specific week number
  python3 09_automation.py --all           # print drafts for every red flag
  python3 09_automation.py --out tips.txt  # also save to a file

RUN ON A SCHEDULE
  GitHub: .github/workflows/weekly-tip.yml runs it every Monday and saves the draft.
  Cron:   0 9 * * 1  python3 /path/to/09_automation.py --out /path/to/tip.txt

NO-CODE VERSION (Zapier / Make free tier)
  1. Trigger: Schedule, every Monday 09:00.
  2. Google Sheets: "Get row" from a sheet with columns flag, why, action
     (copy the RED_FLAGS list below into the sheet).
  3. AI step (ChatGPT/Claude/Gemini): use prompt P-AUTO-1 from 10_prompt_library.md.
  4. Send the result to yourself by email/Slack as "DRAFT - approve before posting".
  5. Do NOT auto-post. Review facts, then post manually.
"""
import argparse
import datetime
import sys

RED_FLAGS = [
    {"flag": "Guaranteed or risk-free returns",
     "why": "No legitimate investment can promise profit (FTC).",
     "action": "Walk away; verify the firm on the official regulator register."},
    {"flag": "Requests for your seed phrase, OTP or PIN",
     "why": "These give full control of your assets/accounts.",
     "action": "Never share. Open the official app yourself instead of clicking links."},
    {"flag": "Urgency and secrecy",
     "why": "Pressure stops you from checking facts.",
     "action": "Pause 24 hours and talk to someone you trust."},
    {"flag": "Fee required before withdrawal",
     "why": "A classic advance-fee trap; more fees follow.",
     "action": "Stop paying; contact your bank and report."},
    {"flag": "Investment tips from a new online 'friend'",
     "why": "Relationship-investment scams build trust before asking for money.",
     "action": "Never mix online relationships and investing."},
    {"flag": "'Registered advisor' with only a screenshot certificate",
     "why": "Fake certificates are common; a screenshot proves nothing.",
     "action": "Check the name on the official regulator list."},
    {"flag": "Send 1, get 2 back giveaways",
     "why": "Doubling promises are giveaway scams; crypto payments are hard to reverse.",
     "action": "Ignore and report the account."},
    {"flag": "Apps installed from links or files",
     "why": "Fake apps can show fake profits or steal data.",
     "action": "Use official app stores and check the developer."},
    {"flag": "Fake 'recovery agents'",
     "why": "They target past victims and ask advance fees.",
     "action": "Report via your bank and official portals only."},
]

FOOTER = ("Education only, not financial advice. "
          "Verify with official sources (SEBI, RBI, CERT-In, FTC, CISA).")


def draft(flag, week):
    return (f"🚩 Scam Alert Tip - Week {week}\n\n"
            f"Red flag: {flag['flag']}\n"
            f"Why it matters: {flag['why']}\n"
            f"Do this: {flag['action']}\n\n"
            f"Remember: Pause → Verify → Report.\n{FOOTER}\n"
            f"#ScamAwareness #InvestSmart\n\n"
            f"[STATUS: DRAFT - needs human approval]")


def main():
    ap = argparse.ArgumentParser(description="Draft a weekly scam-alert tip.")
    ap.add_argument("--week", type=int, help="ISO week number (default: this week)")
    ap.add_argument("--all", action="store_true", help="print a draft for every red flag")
    ap.add_argument("--out", help="also save the output to this file")
    a = ap.parse_args()

    if a.all:
        text = "\n\n----------\n\n".join(draft(f, i + 1) for i, f in enumerate(RED_FLAGS))
    else:
        week = a.week or datetime.date.today().isocalendar()[1]
        text = draft(RED_FLAGS[week % len(RED_FLAGS)], week)

    print(text)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
        print(f"\nSaved to {a.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
