# Prompt Library
Use `[brackets]` as variables. Log which tool you ran each in (`14_tool_log.md`).

| ID | Purpose | Prompt |
|---|---|---|
| P-RES-1 | Research (web-enabled tool) | "Act as a research assistant. Find official public advisories from RBI, SEBI, CERT-In, FTC and CISA about crypto/investment scams. For each: title, date, issuer, URL, and a 2-line paraphrase. Mark anything you could not open as UNVERIFIED. Do not invent URLs." |
| P-RES-2 | Scam patterns | "From those sources only, list recurring scam patterns affecting young investors. Cite the source for each pattern." |
| P-SRC-1 | Source-grounded (NotebookLM) | "Using only the uploaded sources, summarise blockchain fundamentals for college students. If a point isn't in the sources, say so." |
| P-WRITE-1 | Explainer | "Write a ~1,000-word plain-language explainer on blockchain and wallets for college students. Use analogies, no jargon without definition, no coin/brand names, no investment advice, include a safety routine and a not-financial-advice note." |
| P-SAMP-1 | Training samples | "Write 6 fictional scam messages labelled TRAINING SAMPLE for education. Use invented token/app names only, `.invalid` links, no real brands or wallet addresses. After each, list red flags and the safe response." |
| P-SOC-1 | Posts | "Create 5 short social posts (hook, body, hashtags) teaching one red flag each. Tone: friendly, non-judgemental. Include 'not financial advice'." |
| P-IMG-1 | Infographic (Leonardo/Canva/Gemini) | "Flat vector infographic, dark navy background, title '8 Red Flags of Crypto & Investment Scams', 8 icon cards (guarantee, key, clock, fee, stranger chat, certificate, giveaway, app link), green footer 'Pause → Verify → Report'. No real logos, no coin symbols." |
| P-DECK-1 | Deck (Gamma) | "Create a 6-slide deck for college students: blockchain basics, wallets, how scams work, red flags, pause-verify-report, takeaways. Minimal text, no brand logos." |
| P-QUIZ-1 | Quiz | "Write 10 multiple-choice questions (A–D) from the explainer and checklist, 1 correct answer each, plus an answer key with a one-line reason citing the source idea." |
| P-AUTO-1 | Weekly tip | "Given red flag [flag], why [why], action [action], write a 60-word friendly tip with a 'Pause → Verify → Report' line and a not-financial-advice footer. No brand names." |
| P-VER-1 | Fact-check | "List every factual claim in the text below. For each, say whether it is supported by [source list], needs checking, or is unsupported. Flag any outdated claims." |
| P-VER-2 | Red-team | "Review this content for unsafe advice (e.g., recommending coins, sharing keys, paying fees, legal/tax claims). List problems and fixes." |
| P-ETH-1 | Ethics review | "Check this content for: promotion of any asset, real brands, real addresses, victim-blaming, financial advice. Suggest edits." |

**Prompting skills shown:** role + constraints, source-grounding ("only these sources"), refusal-to-guess ("mark UNVERIFIED"), structured output, iterative refinement, red-teaming.
