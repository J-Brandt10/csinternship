# Issue #1 — Build Homepage Web App

## Issue Summary
Build a minimal Python web app with a single homepage route at `/` that displays "CS Internship Tools - Welcome Jack!". The app must run via `python app.py`, have its dependencies declared in `requirements.txt`, and have tests covering the homepage route.

## Related Prior Work
None — first feature in this repo.

## Approach
Use Flask: it's the lightest Python web framework for a single-route app, widely known, and trivial to test with its built-in test client. No templates needed — return a plain HTML string from the route. Tests will use `pytest` with Flask's test client.

## Task Breakdown
- [ ] Create `requirements.txt` with Flask and pytest
- [ ] Create `app.py` with a `/` route returning the welcome message
- [ ] Create `tests/test_app.py` with a test for the homepage route
- [ ] Verify the app runs and tests pass
- [ ] Commit and open a PR

## Open Questions
None.
