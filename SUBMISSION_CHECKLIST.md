# Final Submission Checklist
Tick each box before you submit. ✅ = already done in this repo, ☐ = you must do it.

## A. The 12 required tasks
| # | Task | Where | Status |
|---|---|---|---|
| 1 | Target audience chosen (college students & young investors) | `01_research_report.md` §1 | ✅ |
| 2 | ≥2 AI research tools used | `14_tool_log.md` | ☐ Only Claude so far. Add ≥1 more (Perplexity / NotebookLM) |
| 3 | Reliable sources collected & verified (RBI, SEBI, CERT-In, FTC, CISA) | `01_research_report.md` §3, §7 | ✅ except CERT-In crypto advisory (not found; flagged) and a browser check ☐ |
| 4 | Research summary + red-flag checklist | `01_…`, `02_…` | ✅ |
| 5 | ~1,000-word explainer | `03_…` | ✅ |
| 6 | 6 fictional "training sample" scams | `04_…` | ✅ |
| 7 | 5 social posts + infographic | `05_…`, `06_….svg` | ✅ (optional ☐ redo in Canva/Leonardo) |
| 8 | 6-slide deck + 10-question quiz & key | `07_….pptx`, `08_…` | ✅ |
| 9 | One automation | `09_automation/`, `.github/workflows/weekly-tip.yml` | ✅ |
| 10 | Tested for hallucinations / unsafe / outdated info | `11_verification_report.md` | ✅ on Claude; ☐ add other tools' rows |
| 11 | Prompts documented | `10_prompt_library.md` | ✅ |
| 12 | Ethics explained | `13_ethics_statement.md` | ✅ |

## B. Required tools (≥4 free AI tools)
- [ ] Claude (done)
- [ ] Tool 2: ______ (logged in `14_tool_log.md`)
- [ ] Tool 3: ______
- [ ] Tool 4: ______
Only list tools you really used.

## C. Personalise (5 minutes)
- [ ] Replace `[YOUR NAME]`, `[COLLEGE]`, `[DATE]` in `README.md`, `LICENSE`, `07_presentation_slides.md`, and on the title slide of `07_presentation_slides.pptx`
- [ ] Edit the reflection in `12_before_after_analysis.md` so it reflects your own experience
- [ ] Open every link in `01_research_report.md` in your browser

## D. Quality gate
- [ ] Run `python3 tests/check_project.py` → must print `PASSED` with no `FAILED`
- [ ] GitHub **Actions** tab shows a green ✅ for "Project checks"

## E. Submit
- [ ] Repo is **Public** (or shared with your teacher)
- [ ] Copy the repo link (https://github.com/<you>/<repo>) and submit it
- [ ] Be ready to present using `DEMO.md`
