# 02. Structured First-Draft Package

이 문서는 `vellum-lite`식 접근을 설명합니다. 여기서 중요한 것은 특정 도구가 아니라, 반복 가능한 파일 계약입니다.

## 한 줄 설명

자료를 넣으면 최종 논문이 아니라, 검토 가능한 초안 패키지를 만듭니다.

```text
materials in
  -> intake validation
  -> argument outline
  -> evidence bindings
  -> first-draft preview
  -> risk report
  -> review
  -> revised draft package
  -> human signoff
```

## 이 접근이 좋은 경우

- 연구실에서 학생별 초안 품질을 같은 기준으로 보고 싶다.
- 지도교수에게 "완성본"이 아니라 "비평 가능한 패키지"를 보여주고 싶다.
- source, claim, risk, human decision을 한곳에 남기고 싶다.
- 로컬 모델, cloud model, 수작업을 섞어도 같은 형식의 결과물이 필요하다.

## 오해하지 말 것

이 방식은 로컬 모델 전용이 아닙니다.

| 구성 | 가능 여부 |
|---|---|
| deterministic file checks | 권장 |
| local model inventory/risk scan | 권장 |
| cloud model sanitized drafting | 가능 |
| local-only privacy route | 가능 |
| 원클릭 publication-ready paper | 금지 |

## 기본 폴더 구조

```text
student-project/
  task-brief.md
  materials-inventory.md
  benchmark-papers.md
  findings-summary.md
  evidence-bindings.md
  argument-outline.md
  section-architecture.md
  draft-risk-report.md
  first-draft-preview.md
  review-report.md
  revised-draft.md
  ai-use-log.md
  human-decisions.md
```

## 각 파일이 막아주는 문제

| 파일 | 막아주는 문제 |
|---|---|
| `task-brief.md` | AI가 원고 종류와 독자를 임의로 정하는 문제 |
| `materials-inventory.md` | 자료가 무엇인지 모른 채 초안을 쓰는 문제 |
| `do-not-claim.md` | 과장 주장, 인과 주장, 통계 주장 남발 |
| `evidence-bindings.md` | citation처럼 보이지만 실제 근거가 없는 문장 |
| `section-architecture.md` | 문단은 많지만 논증 흐름이 없는 원고 |
| `draft-risk-report.md` | privacy, quote, statistics, ethics 위험 누락 |
| `review-report.md` | 초안 작성자와 검토자가 같은 관점에 갇히는 문제 |
| `ai-use-log.md` | 심사 때 AI 사용 범위를 설명하지 못하는 문제 |

## 추천 진행

### Step 1. 자료를 작게 묶기

전체 컴퓨터나 전체 Google Drive를 AI에게 열지 않습니다. 먼저 프로젝트용 작업 폴더를 만듭니다.

```text
context/
sources/
notes/
data/
figures/
draft/
```

민감자료가 있으면 `raw-private/`에 두고 외부 모델에는 보내지 않습니다.

### Step 2. task shape 먼저 받기

초안 작성 전에 아래 질문에 답하게 합니다.

- 어떤 원고인가?
- 대상 독자는 누구인가?
- 어떤 claim이 가능한가?
- 어떤 claim은 금지해야 하는가?
- 어떤 자료가 빠져 있는가?
- 어떤 인간 결정이 필요한가?

### Step 3. evidence binding 만들기

AI가 쓰려는 핵심 문장을 source와 연결합니다.

| Draft claim | Evidence | Status |
|---|---|---|
| A may support B | source note, paper, data summary | allowed with caveat |
| A causes B | none or weak | blocked |
| Participant said X | raw quote not approved | human-only |

### Step 4. 초안과 review 분리

같은 thread에서 계속 "더 좋게 고쳐줘"만 하지 않습니다.

```text
drafting pass
  -> separate critique pass
  -> accepted findings only
  -> rewrite pass
  -> risk check
```

### Step 5. draft package로 끝내기

결과는 투고본이 아니라 검토 패키지입니다.

```text
draft-package/
  revised-draft.md
  evidence-bindings.md
  source-verification.md
  review-report.md
  draft-risk-report.md
  ai-use-log.md
  human-decisions.md
```

## 발표용 설명

```text
vellum-lite의 핵심은 로컬 모델 자체가 아니라, 어떤 모델을 쓰더라도 같은 evidence/risk/gate 기록이 남도록 만드는 것입니다. 학생이 ChatGPT를 쓰든, Claude를 쓰든, 로컬 모델을 쓰든, 최종적으로 지도교수가 보고 싶은 것은 이 문장이 어떤 근거에 기대는지와 어디까지 사람이 승인했는지입니다.
```
