You are doing a critical code review of pull request $ARGUMENTS. Be direct and thorough — the goal is to ship clean, correct, maintainable code.

## 1. Understand the PR

Run `gh pr view $ARGUMENTS` to read the title, description, and linked issues. Understand the intent before evaluating the implementation.

## 2. Read the Diff

Run `gh pr diff $ARGUMENTS` to see every changed file. For any file where you need more context, read the full file — a diff alone can miss surrounding logic that affects your assessment.

## 3. Check for Bugs

Look for:
- Logic errors, off-by-one mistakes, incorrect conditionals
- Unhandled edge cases (null/undefined, empty collections, boundary values)
- Race conditions or incorrect async/await usage
- Data mutations that could cause unexpected side effects
- Security issues: injection vulnerabilities, missing input validation, exposed secrets, unsafe deserialization

## 4. Assess Readability and Clarity

Ask whether a new team member could understand this code quickly. Flag:
- Unclear variable, function, or class names
- Functions that do more than one thing
- Deeply nested logic that could be flattened
- Magic numbers or strings that should be named constants
- Missing or misleading comments where the intent is non-obvious

## 5. Evaluate Maintainability

Consider how easy this code will be to change later. Look for:
- Duplicated logic that should be extracted
- Hard-coded values that should be configurable
- Tight coupling between components that should be separate
- Missing or inadequate tests for the changed behavior
- Tests that only test the happy path

## 6. Check Best Practices

Review against standard practices for the language and framework in use:
- Consistent style and formatting with the rest of the codebase
- Proper error handling — errors surfaced, not silently swallowed
- No unnecessary dependencies added
- No dead code, commented-out blocks, or debug statements left in
- Sensible naming conventions followed throughout

## 7. Write the Review

Organize your findings into three tiers:

**Must Fix** — bugs, security issues, or correctness problems that should block merge

**Should Fix** — clarity, maintainability, or best-practice issues that would meaningfully improve the code

**Consider** — minor suggestions, stylistic preferences, or optional improvements

For each finding, include:
- The file and line(s) in question
- What the problem is and why it matters
- A concrete suggestion or example of how to improve it

End with a one-paragraph overall assessment: is this PR ready to merge, does it need changes, or does it need a rethink?
