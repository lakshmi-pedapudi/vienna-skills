# Review Log: <document>

Convergent review loop (`references/review.md`). Stop when two successive passes agree (no high, no regression, at most one minor new finding). Cap at three passes.

## Pass 1 (<date>, <reviewer: self / fresh subagent / second model>)

Gate: <check_html.py: N failures, M warnings> · Render: <all sections render | issues> · Numbers: <all traced | N unresolved>

| Id | Severity | Location | Finding | Fix applied |
|---|---|---|---|---|
| P1-01 | high | | | |
| P1-02 | minor | | | |

## Pass 2 (<date>, <reviewer>)

Gate: ...

Regression check on pass 1 ids: P1-01 closed · P1-02 closed

| Id | Severity | Location | Finding | Fix applied |
|---|---|---|---|---|
| P2-01 | minor | | | |

New issues caused by pass 1 fixes: <none | ids>

## Pass 3 (only if pass 2 disagreed with pass 1)

...

## Outcome

<Converged after pass N: passes N-1 and N agree.> or <Did not converge; unstable areas: ...; decision needed on ...>
