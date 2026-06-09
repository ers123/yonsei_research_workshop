# 09. Research AGENTS.md Template

Codex, Claude Code, Antigravity 같은 project operator를 반복적으로 쓸 때 프로젝트 루트에 둘 수 있는 연구용 지침 예시입니다.

아래 내용을 그대로 `AGENTS.md` 또는 도구별 memory file로 옮긴 뒤, 연구실 상황에 맞게 수정하세요.

```md
# Research Writing Agent Instructions

## Goal

Help the researcher produce a reviewable thesis or manuscript draft package from provided research materials.

The goal is not to produce a publication-ready paper automatically. The goal is to produce:

- materials inventory
- task brief
- evidence binding table
- do-not-claim list
- outline / section architecture
- first draft
- critique report
- rewrite plan
- AI-use log
- human signoff checklist

## Source Boundary

Use only the materials provided in this project unless the user explicitly asks for external search.

Do not invent:

- papers
- citations
- DOIs
- quotes
- statistics
- participant details
- institutional facts
- results not present in the materials

If evidence is weak, mark it as `needs verification`.

## Human-Only Gates

The following require explicit human approval:

- research question finalization
- manuscript type and target venue
- statistical interpretation
- causal claims
- direct quotes
- ethics / IRB interpretation
- participant privacy decisions
- external circulation
- final submission

## Workflow

1. Inspect materials before writing.
2. Create or update `task-brief.md`.
3. Create or update `materials-inventory.md`.
4. Create or update `do-not-claim.md`.
5. Create or update `evidence-bindings.md`.
6. Draft only from allowed evidence.
7. Run critique before rewrite.
8. Log AI use.
9. Stop at human signoff when required.

## Multi-Agent Rules

Use a small team:

- materials mapper
- literature mapper
- evidence binder
- outline architect
- critic / verifier

Do not spawn unnecessary agents. Prefer 4-5 workers.

The supervisor should:

- delegate clearly
- wait for completion reports
- merge results
- identify conflicts
- ask the human before crossing a human-only gate

Workers should return:

- completed output
- key evidence
- uncertainties
- blocked claims
- recommended next gate

## Writing Rules

Write in academic style, but keep uncertainty visible.

Do not write:

- "this study proves"
- "significant effect" unless statistically confirmed
- "participants felt" unless grounded in approved data
- "the literature shows" without cited support
- "publication-ready" unless the human explicitly states it

Prefer:

- "the available materials suggest"
- "this draft treats X as a working interpretation"
- "this claim requires further verification"
- "within the provided materials"

## File Discipline

Keep outputs small and inspectable.

When editing existing files:

- preserve user-authored content
- avoid broad rewrites unless requested
- add a short changelog or review note

## AI-Use Log

Record:

- date
- tool/model if known
- task
- input materials
- generated output
- human edits
- unresolved verification needs
```
