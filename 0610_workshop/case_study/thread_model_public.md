# Public Thread Model

## Compact Model

| Thread | Role | Return |
|---|---|---|
| Supervisor | 전체 지휘, gate, 병합 | `threads/supervisor/merge-report.md` |
| Evidence-Literature | 문헌 위치, 이론 렌즈, 연구 gap, citation 후보 | `threads/evidence-literature/return.md` |
| Data-Methods | 데이터 readiness, 분석 가능 범위, 방법 한계 | `threads/data-methods/return.md` |
| Visual-Assets | table/figure spec, caption, safety label | `figures/visual-manifest.md` |
| Review-Verification | source gate, privacy gate, overclaim review | `threads/review-verification/return.md` |
| Drafting | outline, draft, revision | `threads/drafting/return.md` |

## Phase Flow

```text
Supervisor intake
  -> Evidence-Literature + Data-Methods + Visual-Assets
  -> Review-Verification
  -> Drafting
  -> Review-Verification second pass
  -> Supervisor merge
  -> Human signoff
```

## Why Not More Threads?

더 많은 thread가 항상 더 좋은 결과를 만들지는 않습니다.

| Too many threads | Compact alternative |
|---|---|
| literature-review + source-context + citation-auditor | Evidence-Literature |
| methods-evidence + data-readiness | Data-Methods |
| source-verifier + reviewer | Review-Verification |
| outline + drafting + revision | Drafting |
| figure-table + image prompt + caption checker | Visual-Assets |
| packaging worker | Supervisor merge |

## Presenter Line

```text
실제 운영에서는 thread 수를 늘리는 것이 목표가 아닙니다. 서로 다른 판단 기능을 분리하면서도 상태 추적이 가능한 수준으로 유지하는 것이 목표입니다.
```
