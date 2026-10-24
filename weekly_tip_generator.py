#!/usr/bin/env python3
"""Weekly scam-alert tip drafter.

Reads red flags from checklist_flags.json and drafts a social-media tip for the
current ISO week (rotates through the list). Works offline with templates.
Optional: set ANTHROPIC_API_KEY / OPENAI_API_KEY and adapt `polish_with_llm`
to have an AI tool rewrite the draft. ALWAYS human-review before posting.
"""
import json, datetime, pathlib, sys

HERE = pathlib.Path(__file__).parent
FOOTER = "Education only, not financial advice. Verify with official sources (SEBI, RBI, CERT-In, FTC, CISA)."

def load_flags():
    return json.loads((HERE / "checklist_flags.json").read_text(encoding="utf-8"))

def pick(flags, date=None):
    date = date or datetime.date.today()
    week = date.isocalendar()[1]
    return flags[week % len(flags)], week

def draft(flag, week):
    return (f"🚩 Scam Alert Tip — Week {week}\n\n"
            f"Red flag: {flag['flag']}\n"
            f"Why it matters: {flag['why']}\n"
            f"Do this: {flag['action']}\n\n"
            f"Remember: Pause → Verify → Report.\n{FOOTER}\n"
            f"#ScamAwareness #InvestSmart\n\n"
            f"[STATUS: DRAFT — needs human approval]")

def main():
    flags = load_flags()
    flag, week = pick(flags)
    text = draft(flag, week)
    out = HERE / f"draft_week_{week}.txt"
    out.write_text(text, encoding="utf-8")
    print(text)
    print(f"\nSaved to {out}", file=sys.stderr)

if __name__ == "__main__":
    main()
