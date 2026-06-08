# Visual-Assets Workflow

## 왜 별도 역할이 필요한가

논문에서 figure/table은 장식이 아닙니다. 주장을 보조하거나 과장할 수 있는 위험한 산출물입니다.

Visual-Assets worker는 다음을 관리합니다.

- 어떤 표/그림이 필요한가?
- 그 visual은 어떤 claim을 지원하는가?
- source가 무엇인가?
- empirical chart인가, conceptual diagram인가?
- generated image가 실제 연구 결과처럼 보이지 않는가?
- caption이 evidence보다 강한 주장을 하지 않는가?
- Word/APA manuscript의 어느 위치에 들어가는가?

## Folder Map

```text
figures/
  specs/
  generated/
  approved/
  rejected/
  visual-manifest.md
```

## Rule

Word 문서나 제출용 초안에는 `approved/` 안의 파일만 삽입합니다.

`generated/`는 실험 초안입니다.

`rejected/`에는 왜 사용하지 않았는지를 남깁니다.

## Visual Manifest Template

| Figure/Table | Type | Claim supported | Source | Status | Caption safety |
|---|---|---|---|---|---|
| Figure 1 | conceptual diagram | candidate mechanism | evidence map | approved / partial / blocked | does not imply causal proof |
| Table 1 | evidence table | claim-source mapping | source verification | approved | no private details |

## Safe Figure Prompt

```text
Create a clean academic conceptual diagram.
Use only the provided claim map and approved labels.
Do not include numerical data, causal effect sizes, participant quotes, private screenshots, or claims of validated efficacy.
The figure should communicate candidate mechanisms and boundary conditions, not proven effects.
Use a white background and readable labels.
```
