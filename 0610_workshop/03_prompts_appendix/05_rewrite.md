# 05. Rewrite Prompt

비평 결과를 반영해 개정 초안을 만드는 프롬프트입니다.

```text
review.md의 지적을 반영해 revised draft를 작성해 주세요.

입력:
- first-draft.md
- review.md
- evidence-bindings.md
- draft-risk-report.md
- do-not-claim.md

규칙:
- review.md가 요구한 수정만 반영하세요.
- 새 claim, 새 수치, 새 문헌을 추가하지 마세요.
- evidence boundary를 유지하세요.
- 차단된 claim은 삭제하거나 약화하세요.
- unresolved risk는 본문 또는 checklist에 남기세요.

출력:
## Revised Draft
## What Changed
## Claims Removed Or Weakened
## Remaining Human Decisions
## External Circulation Status

마지막에 반드시 다음 문장을 포함하세요.
"이 초안은 연구자 검토용이며, 외부 배포 또는 투고 가능 상태를 의미하지 않는다."
```
