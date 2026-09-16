# Review Log: <document>

Convergent review loop. Stop when two successive passes agree (no high, no regression, at most one minor new finding). Cap three passes.

## Pass 1 (<date>, <reviewer: self / fresh subagent / Codex>)

the funder: <style gate: clean | N hits> · <figures or citations: pass | N unmatched> · <layout: N warnings>

| Id | Severity | Location | Finding | Fix applied |
|---|---|---|---|---|
| P1-01 | high | | | |
| P1-02 | minor | | | |

## Pass 2 (<date>, <reviewer>)

the funder: ...

Regression check on pass 1 ids: P1-01 closed · P1-02 closed

| Id | Severity | Location | Finding | Fix applied |
|---|---|---|---|---|
| P2-01 | minor | | | |

New issues caused by pass 1 fixes: <none | ids>

## Pass 3 (only if pass 2 disagreed with pass 1)

...

## Verdict

<Converged after pass N: passes N-1 and N agree.> or <Did not converge; unstable areas: ...; decision needed on ...>
