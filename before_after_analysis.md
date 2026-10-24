# Before / After Analysis (AI-assisted vs. unassisted, and draft vs. verified)

## 1. Prompt improvement
| | **Before (weak prompt)** | **After (engineered prompt)** |
|---|---|---|
| Prompt | "Tell me about crypto scams in India." | P-RES-1 (see prompt library): role, named sources, "mark UNVERIFIED", paraphrase only |
| Typical output | Generic list, no dates, no links, possible invented statistics | Source table with issuer/date/URL and verification status |
| Risk | Hallucinated laws/numbers | Gaps are visible and flagged |

## 2. Content changes after verification (this project)
| Item | First-pass idea | Final version | Reason |
|---|---|---|---|
| CERT-In | Cite a crypto-specific advisory | Removed claim; flagged ⚠️ | Could not find primary source |
| Legal/tax status | Summarise India's current rules | Removed; "check current sources" | Rules change; RBI items are dated |
| Helpline | State number as fact | "Verify current number" | Not retrieved from official page |
| Stats | Use as current | Labelled with year/source type | Old, secondary |
| Samples | Mention a well-known platform | Fully fictional names + `.invalid` | Ethics: no real brands |

## 3. Time and quality (qualitative; no timings were measured)
| Task | Without AI (typical) | With AI | Quality notes |
|---|---|---|---|
| Source discovery | Several hours of searching regulator sites | Minutes to collect leads | Results were often news copies of regulator text; needed primary-source checking |
| 1,000-word explainer | Hours | Minutes for a draft | Needed edits for accuracy and brand-free wording |
| Quiz drafting | An hour or more | Minutes | Answer key tied back to sources |
| Verification | Same either way | Slowest step | AI cannot be trusted to verify itself; humans must open sources |

## 4. Reflection (DRAFT written with AI help; edit it so it reflects your own experience)
AI made it much faster to collect leads, draft the explainer and build the quiz, but it was weakest where facts mattered most. In my verification I found that the first draft named a real regulator inside a fake scam message, stated a helpline without a source, and could easily have cited a CERT-In crypto advisory that I could not find. Asking the tool to mark unverified items, and checking claims against RBI, FTC, CISA and Ministry of Home Affairs pages, made the final version safer. I would never automate posting scam-alert tips without a human review, and I would not let AI state legal, tax or helpline details without checking an official page. The biggest lesson is that AI is a good first drafter and a poor fact-checker.
