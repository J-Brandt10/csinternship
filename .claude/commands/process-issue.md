You are processing GitHub issue $ARGUMENTS. Follow these steps in order:

## 1. Read the Issue

Fetch the full issue using `gh issue view $ARGUMENTS` — read the title, body, labels, and any comments. Understand what is being asked before doing anything else.

## 2. Search for Related Previous Work

Search the `scratchpads/` folder for any files related to this issue by topic, keywords, or issue number. Read any relevant files you find — they may contain prior research, partial plans, or context that should inform your approach.

## 3. Review Past Pull Requests

Run `gh pr list --state all --limit 50` and look for PRs that touch similar areas or reference related issues. Read the description and diff of any that seem relevant using `gh pr view <number>` and `gh pr diff <number>`.

## 4. Break the Issue into Tasks

Think hard about what the issue requires. Consider edge cases, dependencies, and the smallest logical units of work. Produce a clear, ordered list of tasks — each task should be something that could be committed independently.

## 5. Write a Plan to a Scratchpad

Create a new file at `scratchpads/issue-$ARGUMENTS.md` with the following sections:

- **Issue Summary** — one paragraph restating the problem in your own words
- **Related Prior Work** — what you found in scratchpads and past PRs
- **Approach** — how you plan to solve it and why
- **Task Breakdown** — the ordered task list from step 4
- **Open Questions** — anything uncertain that might affect implementation

## 6. Write the Code

Work through the task list one item at a time. Edit only the files needed for each task. Do not refactor unrelated code or add unrequested features. Mark each task complete as you finish it.

## 7. Run the Tests

Run the project's test suite. If tests fail, fix the failures before continuing — do not skip or comment out tests. If no test suite exists, note that in the scratchpad.

## 8. Commit and Open a Pull Request

Stage only the files changed for this issue. Write a clear commit message. Then open a PR with:

- **Title**: concise description of what changed
- **Body**: link to the issue (`Closes #$ARGUMENTS`), summary of the approach, and a testing checklist
