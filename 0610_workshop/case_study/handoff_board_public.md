# Public Handoff Board

각 phase가 끝날 때 supervisor가 보는 상태판입니다.

| Phase | Thread | Status | Output |
|---|---|---|---|
| 0 | Supervisor | done | scope, privacy rule, thread budget |
| 1 | Evidence-Literature | done | literature position, theory lens, gap |
| 1 | Data-Methods | done | claim boundary, data readiness |
| 1 | Visual-Assets | done | table/figure plan, safety labels |
| 2 | Review-Verification | done | allowed/blocked/human-only claims |
| 3 | Drafting | done | source-gated outline and draft |
| 4 | Review-Verification | done | overclaim/citation/privacy review |
| 5 | Supervisor | done | merge report and draft package |
| 6 | Human | pending | quote/statistics/ethics/external circulation |

## Gate Rule

```text
Blocked claim은 draft로 넘어가지 않는다.
Human-only claim은 AI가 승인하지 않는다.
Needs verification은 citation/source 확인 전까지 보류한다.
```

## Supervisor가 확인할 것

- 반환 파일이 실제로 존재하는가?
- worker가 자기 역할 밖의 판단을 하지 않았는가?
- blocked claim이 draft에 들어가지 않았는가?
- figure/table caption이 evidence보다 강한 주장을 하지 않는가?
- human-only decision이 체크리스트로 남았는가?
