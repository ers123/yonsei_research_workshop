# 03. First Draft Prompt

근거 연결표를 통과한 claim만으로 첫 초안을 작성하는 프롬프트입니다.

```text
검토 가능한 first draft를 작성해 주세요.

사용 가능한 입력:
- task-brief.md
- argument-outline.md
- section-architecture.md
- evidence-bindings.md
- findings-summary.md
- draft-risk-report.md
- figure-table-image-plan.md

규칙:
- evidence-bindings.md에서 allowed 또는 allowed with caveat인 claim만 사용하세요.
- blocked, human-only, needs verification claim은 본문에 넣지 마세요.
- raw quote, 실명, private link, participant-level detail은 넣지 마세요.
- 통계적 유의성, 인과효과, 일반화 표현은 승인된 근거가 없으면 쓰지 마세요.
- figure/table callout은 visual plan에 있는 것만 사용하세요.

출력:
1. 제목
2. 초록 또는 요약
3. section별 본문
4. figure/table callout
5. citation needs
6. unresolved risks
7. human review checklist

문체:
- 학술적으로 쓰되, publication-ready라고 주장하지 마세요.
- 불확실한 부분은 자연스럽게 caveat로 남기세요.
- 새 문헌이나 새 데이터를 만들지 마세요.
```
