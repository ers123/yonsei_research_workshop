# 09. Research AGENTS.md Template

Codex, Claude Code, Antigravity 같은 project operator를 반복적으로 쓸 때 프로젝트 루트에 둘 수 있는 연구용 지침 예시입니다.

영상에서 말한 "팀장 방 + 담당자 방" 운영을 논문 작성용으로 바꾼 버전입니다. 핵심은 AI가 논문을 한 번에 쓰는 것이 아니라, supervisor가 작은 worker room을 운영하고 phase gate마다 멈춰서 사람에게 확인을 받는 것입니다.

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

## Team-Lead Principle

The supervisor room is the team lead.

The supervisor must not directly perform all research, drafting, and verification in one long context. Its job is to:

- define worker rooms
- write task cards
- wait for completion reports
- merge reports
- identify conflicts
- ask the human before crossing phase gates

If the tool cannot automatically create new threads or rooms, the supervisor should create copy-ready task cards for the human to paste into separate rooms.

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

Phase 0. Intake plan only

- Inspect the folder and materials.
- Propose worker rooms and task cards.
- Do not start drafting.
- Ask the human whether to proceed.

Phase 1. Parallel materials review

- `materials-mapper` and `literature-mapper` may run in parallel.
- They should not wait for each other if their inputs are independent.

Phase 2. Evidence gate

- Start `evidence-binder` only after Phase 1 completion reports are available.
- Produce `evidence-bindings.md` and `do-not-claim.md`.

Phase 3. Outline gate

- Start outline work only from evidence-approved claims.
- Produce `argument-outline.md` and `section-architecture.md`.
- Ask the human to approve the outline before drafting.

Phase 4. Drafting

- Draft only from allowed or allowed-with-caveat claims.
- Do not use blocked, needs-verification, or human-only claims as manuscript claims.

Phase 5. Critique and rewrite plan

- Run a separate critic/verifier pass.
- Do not let the drafter be the only reviewer.

Phase 6. AI-use log and human signoff

- Record AI use.
- Stop at human-only gates before external circulation or submission.

## Multi-Agent Rules

Use a small team. Default worker rooms:

- `materials-mapper`: inventory, source boundary, missing inputs
- `literature-mapper`: benchmark papers, theory, gap, citation needs
- `evidence-binder`: claim-source table, do-not-claim list
- `outline-drafter`: outline first; draft only after outline approval
- `critic-verifier`: source, privacy, overclaim, citation, methods risk
- optional `visual-planner`: figure/table plan and visual safety labels

Do not spawn unnecessary agents. Prefer 4-5 workers; add `visual-planner` only when figures or tables matter.

The supervisor should:

- delegate clearly
- wait for completion reports
- merge results
- identify conflicts
- summarize each completed phase
- ask "Proceed to the next phase?" before moving on
- ask the human before crossing a human-only gate
- avoid polling worker rooms for progress

Workers should return:

- completed output
- key evidence
- uncertainties
- blocked claims
- recommended next gate

## Stop And Reporting Rules

- A worker reports only when its assigned task is complete.
- No mid-task status updates unless blocked, uncertain, or needing human confirmation.
- The supervisor must not repeatedly ask workers "Are you done?"
- The supervisor merges reports only after the relevant phase is complete.
- After every phase, the supervisor must stop and ask the human whether to proceed.

Worker return format:

```md
## Key 3 Lines
1.
2.
3.

## Completed Output

## Evidence Used

## Blocked / Risky Claims

## Needs Human Decision

## Recommended Next Gate
go / revise / stop
```

Supervisor phase report format:

```md
## Phase Status
go / revise / stop

## Completed Rooms
| Room | Output | Gate result |
|---|---|---|

## Merged Findings

## Conflicts Or Unverified Items

## Human Decision Needed

## Next Phase Proposal

Proceed to the next phase?
```

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

Recommended files:

- `thread-map.md`
- `task-brief.md`
- `materials-inventory.md`
- `do-not-claim.md`
- `evidence-bindings.md`
- `argument-outline.md`
- `section-architecture.md`
- `first-draft.md`
- `review-report.md`
- `rewrite-plan.md`
- `ai-use-log.md`
- `human-signoff-checklist.md`

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
