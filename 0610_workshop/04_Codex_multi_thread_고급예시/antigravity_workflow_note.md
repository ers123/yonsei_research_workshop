# Antigravity Workflow Note

Antigravity를 쓰는 경우에도 핵심은 같습니다. 도구 이름은 달라도 연구 workflow는 다음 구조를 유지해야 합니다.

```text
자료 감사
  -> evidence binding
  -> outline
  -> first draft
  -> critique
  -> rewrite plan
  -> human signoff
```

## Antigravity로 옮길 때의 사고방식

Antigravity의 workflow 또는 agent 기능을 쓴다면, 하나의 "논문 작성 자동화" workflow를 크게 만들기보다 작은 workflow를 단계별로 나누는 편이 안전합니다.

권장 workflow:

1. `research-materials-audit`
2. `evidence-binding`
3. `outline-architecture`
4. `first-draft-from-evidence`
5. `critique-and-risk-review`
6. `rewrite-plan-and-ai-log`

각 workflow는 이전 workflow의 산출물을 입력으로 받아야 합니다.

## Workflow instruction 예시

```text
Workflow name:
research-materials-audit

Goal:
Inspect the provided research materials and produce a materials inventory, allowed claims, blocked claims, missing sources, and human-only decisions.

Rules:
- Do not draft manuscript text.
- Do not invent citations or statistics.
- Do not expose participant-level details.
- Mark uncertain items as needs verification.
- Return a concise gate decision: go / revise / stop.
```

## Agent별 역할

| Agent 또는 workflow | 산출물 |
|---|---|
| materials audit | `materials-inventory.md`, `do-not-claim.md` |
| evidence binding | `evidence-bindings.md` |
| outline architecture | `argument-outline.md`, `section-architecture.md` |
| draft from evidence | `first-draft.md` |
| critique and risk review | `review-report.md`, `draft-risk-report.md` |
| rewrite and log | `rewrite-plan.md`, `ai-use-log.md` |

## 안전장치

- terminal command 자동 실행 권한은 연구자료 폴더에서 보수적으로 둔다.
- raw data나 participant-level 자료가 있는 폴더는 workflow 입력에서 제외하거나 read-only로 제한한다.
- agent가 생성한 reference는 실제 DOI/논문 정보 확인 전까지 `needs verification`으로 둔다.
- 외부 공유나 제출은 workflow 마지막이 아니라 human signoff 이후에만 가능하다.

## 참고

- Google Antigravity IDE workflows 문서: https://antigravity.google/docs/ide-workflows?app=cli
- Google Antigravity overview 문서: https://antigravity.google/docs/overview?app=antigravity
- Google Antigravity features 문서: https://antigravity.google/docs/features?app=antigravity
- Google Antigravity agent settings 문서: https://antigravity.google/docs/agent-settings
