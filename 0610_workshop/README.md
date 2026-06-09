# 0610 DSB Workshop: AI로 논문 초안 패키지 만들기

이 폴더는 2026년 6월 10일 연세대학교 DSB 연구실 워크숍용 정리본입니다.

핵심 메시지는 단순합니다.

> AI에게 "논문 써줘"라고 맡기지 말고, 연구자가 director가 되어 자료, 주장, 근거, 위험, 초안, 비평, 개정, AI 사용 기록을 관리한다.

## 먼저 열어볼 것

1. [01_학생용_핵심가이드.md](01_학생용_핵심가이드.md)
2. [02_DSB_논문초안_데모/README.md](02_DSB_논문초안_데모/README.md)
3. [02_DSB_논문초안_데모/final_draft_examples/manuscript-draft-ko-v0.2.md](02_DSB_논문초안_데모/final_draft_examples/manuscript-draft-ko-v0.2.md)
4. [02_DSB_논문초안_데모/evidence_package/evidence-bindings.md](02_DSB_논문초안_데모/evidence_package/evidence-bindings.md)
5. [02_DSB_논문초안_데모/risk_and_review/peer-review-risk-memo-v0.2.md](02_DSB_논문초안_데모/risk_and_review/peer-review-risk-memo-v0.2.md)

## 이 폴더의 구성

| 폴더 | 용도 |
|---|---|
| `01_학생용_핵심가이드.md` | 학생 입장에서 따라 하는 기본 workflow |
| `02_DSB_논문초안_데모/` | DSB 자료를 바탕으로 만든 논문 초안 예시와 검토 패키지 |
| `03_prompts_appendix/` | 바로 복사할 수 있는 상세 프롬프트 모음 |
| `04_Codex_multi_thread_고급예시/` | Codex multi-thread, Claude Code subagents, Antigravity workflow 확장 |
| `05_장문논문_workflow/` | 긴 학위논문을 목차와 문단 단위로 확장하는 방법 |
| `reference_notes/` | 원자료 사용 경계와 공개 범위 설명 |
| `presentation.html` | Claude Code subagents 참고용 기존 HTML 자료 |

## 1시간 워크숍에서의 추천 흐름

1. 학생용 핵심가이드에서 "AI에게 바로 쓰게 하지 않는다"는 원칙을 설명한다.
2. DSB 최종 초안 예시를 먼저 보여준다.
3. 그 초안이 어떤 evidence package와 risk memo에서 나왔는지 보여준다.
4. 기본 경로는 유료 LLM 하나로도 가능하다고 설명한다.
5. Codex multi-thread는 고급 예시로 짧게 보여준다.
6. 장문논문 workflow는 학위논문처럼 분량이 길어야 할 때의 별도 전략으로 소개한다.
7. prompts appendix는 수업 후 참고자료로 안내한다.

## 무엇을 소개하지 않는가

`vellum-lite`, `hermes`, `paperclip`은 이 워크숍의 주제가 아닙니다. 이들은 내부적으로 파일 계약과 자동화 가능성을 실험한 흔적이지만, 학생들에게 필요한 것은 설치형 엔진이 아니라 다음의 재현 가능한 작업 방식입니다.

```text
자료 정리
  -> task shape
  -> evidence binding
  -> do-not-claim
  -> first draft
  -> critique
  -> rewrite
  -> AI-use log
  -> human signoff
```

## 원자료와 공개 경계

DSB 논문 초안은 교수님이 공유한 연구자료를 참고해 만든 데모입니다. 다만 이 폴더에는 원자료 자체를 포함하지 않습니다.

포함하지 않는 것:

- raw interview
- participant-level data
- 실명 또는 식별 가능한 파일명
- raw CSV row
- private link
- quote approval 전 원문

포함하는 것:

- 익명화/요약된 초안 패키지
- evidence binding
- risk memo
- review report
- visual planning
- 학생용 prompt와 workflow

따라서 이 폴더는 "원자료에서 새롭게 분석을 실행한 live analysis demo"가 아니라, 교수님이 공유한 자료를 바탕으로 정리한 sanitized draft package를 어떻게 검토하고 확장할 수 있는지 보여주는 자료입니다.

Word 예시는 APA-like / APA 7-style 시연용입니다. 실제 투고용 APA final manuscript로 설명하면 안 됩니다. 참고문헌, conference paper metadata, internal technical disclosure, 특허/앱 관련 서술은 외부 배포 전 human verification이 필요합니다.
