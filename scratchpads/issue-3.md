# Issue #3 — Build a Basic Calculator Web App

## Issue Summary
Add a calculator page to the existing Flask app at a `/calculator` route. The calculator must have a display, number buttons (0–9), operation buttons (+ − × ÷), a decimal point button, an equals button, and a clear button. All arithmetic must work correctly client-side via JavaScript. Dividing by zero should display an error message instead of crashing.

## Related Prior Work
- `scratchpads/issue-1.md` + merged PR #2: established the Flask app structure (`app.py`, `templates/`, `tests/`). The calculator follows the same Flask + pytest pattern.

## Approach
Add a `/calculator` route to `app.py` that renders a `templates/calculator.html` page. All calculator logic runs client-side in JavaScript — no server round-trips needed for arithmetic. The Flask route is tested with pytest (status code + page content). The calculator UI uses inline CSS to avoid additional static-file dependencies.

## Task Breakdown
- [ ] Create `templates/` directory if it doesn't exist and add `templates/calculator.html` with full HTML/CSS/JS calculator
- [ ] Add `/calculator` route to `app.py` using `render_template`
- [ ] Add tests in `tests/test_app.py` for the new route (status code + key content)
- [ ] Run `python -m pytest tests/ -v` and confirm all tests pass
- [ ] Commit and open PR

## Open Questions
None.
