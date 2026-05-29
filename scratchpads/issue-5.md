# Issue #5 — Fix activity feed text wrapping, scrolling, and error clearing

## Issue Summary
The activity feed in the ES Quote Tracker (`index.html`) has three problems: long text gets cut off or overflows instead of wrapping cleanly inside the feed container; the feed does not scroll when there are many entries, instead overflowing the page; and there is no way for the operator to dismiss or clear error messages from the feed. All fixes must stay inside the activity feed section and must be delivered as a new file in `.aesquote/new/` — existing files outside that folder must not be touched.

## Related Prior Work
- No prior scratchpad files relate to this issue.
- PR #4 (calculator web app) established the Flask + pytest pattern; structure is unrelated to this JS/CSS issue.
- CLAUDE.md session notes from 2026-05-29 document the same three bugs and describe fixes that were applied locally to the original `index.html` but never deployed. Those notes are the primary reference for the correct approach.

## Approach
Create a self-contained standalone HTML file at `.aesquote/new/activity-feed.html` that implements the activity feed component with all three fixes applied. This file:
- Can be opened directly in a browser to verify all three fixes
- Includes demo entries that exercise each fix (long tokens, many entries, clearable errors)
- Serves as the canonical reference for what the fixed component looks like

The three CSS/JS changes that fix the bugs:

**Fix 1 — Text wrapping:**
- `.feed-group-msg` and `.feed-msg`: change `word-break: break-word; overflow-wrap: anywhere` → `word-break: normal; overflow-wrap: break-word`. The `anywhere` value breaks words mid-character even when wrapping at a space would fit, producing ragged text. `break-word` only breaks unbreakable long tokens as a last resort.

**Fix 2 — Scrolling:**
- `.feed-body > * { flex-shrink: 0; }`: prevents flex children from collapsing to fit the visible height (squishing rows to ~18px and clipping text). With this rule, children keep their natural height and the body overflows → vertical scroll engages.
- `.feed-body`: ensure `min-height: 0` (classic flex-child scroll enabler) and `overflow-y: auto; overflow-x: hidden`.

**Fix 3 — Error clearing:**
- `_entryNeedsResponse(e)`: a new predicate that returns true only when there is an open input/confirmation prompt — NOT for bare errors. This is what gates the Clear button and per-entry dismiss.
- `clearDoneGroups()`: rewritten to remove any entry/group that does not have an open prompt, including plain red error notifications (which previously could never be cleared).
- `dismissLogEntry(id)`: per-entry dismiss function, exposed via a ✕ button on each error/resolved entry.
- Auto-clear sweep: resolved entries auto-dismiss after 30 seconds via `_sweepResolvedFeed` on a 3-second interval.

## Task Breakdown
- [x] Research existing CSS/JS (read index.html lines 165–214 and 2305–2533)
- [x] Write scratchpad (this file)
- [ ] Create `.aesquote/new/activity-feed.html` with all three fixes and demo data
- [ ] Run `python -m pytest tests/ -v` (tests cover Flask routes, not JS — note result)
- [ ] Commit new files and open PR

## Open Questions
- The Flask test suite covers Python routes only, not the JS activity feed. There is no JS test suite in this repo. The fix is verified by opening the standalone HTML file in a browser and confirming the three behaviors visually.
- The existing `index.html` in `.aesquote/esquote/j/` already has most of these fixes applied in its source (from prior local sessions documented in CLAUDE.md). The new file in `.aesquote/new/` is the deliverable per the constraint — it does not modify any existing file.
