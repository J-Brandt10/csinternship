# Issue #9 — Build a Hello Mother Webpage

## Issue Summary
Add a webpage at `/hello-mother` in the existing Flask app that displays "Hello Mother" in large bold text, centered on the screen, with a fun large font and a colorful animated background that makes it look awesome.

## Related Prior Work
- `scratchpads/issue-1.md` + PR #2: established Flask app (`app.py`, `templates/`, `tests/`).
- `scratchpads/issue-3.md` + PR #4: added `/calculator` route via `render_template` — exact pattern to follow.
- `scratchpads/issue-8.md` + current branch: added `/flappy` route the same way.
- Existing templates are self-contained HTML/CSS/JS files with inline styles.

## Approach
Add a `/hello-mother` route to `app.py` that renders `templates/hello_mother.html`. The page uses a Google Font (Pacifico) for the large fun text, CSS flexbox to center the content, and a CSS keyframe animation cycling through a rainbow gradient background. No JavaScript or external dependencies beyond the Google Fonts CDN.

## Task Breakdown
- [x] Create `templates/hello_mother.html` with centered text and animated background
- [x] Add `/hello-mother` route to `app.py`
- [x] Add pytest tests for the new route (status code + key content)
- [x] Run `python -m pytest tests/ -v` and confirm all tests pass
- [x] Commit and open PR

## Open Questions
- None — scope is clear from the issue.
