# 0610 Workshop: AI-Assisted Research Writing Guide

연세대학교 대학원 연구실 워크숍용 보충 자료입니다.

이 폴더의 목적은 슬라이드를 대체하는 것입니다. 발표자가 한 번에 설명할 수 있는 큰 그림, 학생이 워크숍 이후 혼자 따라 할 수 있는 절차, 바로 복사해서 쓸 수 있는 프롬프트와 템플릿을 함께 둡니다.

## 한 줄 메시지

좋은 AI 논문 작성은 "논문 써줘"가 아니라, 연구자가 director가 되어 자료, 근거, 초안, 검증, 비평, 개정, 인간 승인을 역할별로 운영하는 일입니다.

## 이 자료가 다루는 다섯 가지 접근

| 접근 | 언제 쓰나 | 핵심 산출물 |
|---|---|---|
| Structured first-draft package | 자료가 있고 검토 가능한 초안 패키지가 필요할 때 | brief, evidence binding, risk report, draft package |
| Codex thread 연구실 | 여러 연구보조 역할을 나누어 병렬/순차 운영하고 싶을 때 | supervisor report, worker returns, source gate, revised draft |
| 장문 논문 workflow | 학위논문처럼 긴 글을 문헌 흐름 기반으로 확장해야 할 때 | literature-flow reports, outline, paragraph-unit draft |
| Local/hybrid model 운용 | 민감자료, 업로드 제한, 비용, 모델 정책 이슈가 있을 때 | local triage, sanitized cloud draft, human-only gates |
| Claude Code / Antigravity harness | Codex가 아닌 agentic coding 도구에서도 같은 연구실 구조를 쓰고 싶을 때 | role agents, project rules, workflows, return-file contract |

다섯 접근은 경쟁 관계가 아닙니다. 같은 연구 프로젝트 안에서도 함께 쓸 수 있습니다.

## 추천 읽기 순서

1. [01_전체_운영지도.md](01_전체_운영지도.md)
2. [02_vellum_lite_구조화_초안패키지.md](02_vellum_lite_구조화_초안패키지.md)
3. [03_codex_thread_논문작성연구실.md](03_codex_thread_논문작성연구실.md)
4. [04_장문논문_workflow.md](04_장문논문_workflow.md)
5. [05_local_hybrid_model_운용.md](05_local_hybrid_model_운용.md)
6. [06_claude_antigravity_harness.md](06_claude_antigravity_harness.md)
7. [prompts/README.md](prompts/README.md)
8. [templates/README.md](templates/README.md)
9. [live_demo_guide.md](live_demo_guide.md)

## 90분 운영 흐름

| 시간 | 설명할 내용 | 열어볼 파일 |
|---|---|---|
| 0-10분 | AI 시대 논문 심사는 결과물보다 과정, 근거, AI 사용 기록을 더 묻는다 | `01_전체_운영지도.md` |
| 10-25분 | 학생 상황별 다섯 가지 접근법 선택 | `01_전체_운영지도.md` |
| 25-40분 | Structured package: 자료를 초안 패키지로 바꾸는 파일 계약 | `02_vellum_lite_구조화_초안패키지.md` |
| 40-60분 | Codex thread 연구실: supervisor + 5 worker model | `03_codex_thread_논문작성연구실.md`, `case_study/` |
| 60-75분 | 장문 논문: 학습 먼저, 답변은 나중, 문단 단위 작성 | `04_장문논문_workflow.md` |
| 75-85분 | Local/hybrid 모델: 무엇을 로컬에 두고 무엇을 cloud로 보낼지 | `05_local_hybrid_model_운용.md` |
| 85-90분 | Claude Code/Antigravity 확장과 prompt/template 안내 | `06_claude_antigravity_harness.md`, `prompts/`, `templates/` |

## 학생에게 줄 실행 과제

워크숍 후 7일 안에 다음 파일만 만들어도 충분합니다.

1. `task-brief.md`
2. `do-not-claim.md`
3. `materials-inventory.md`
4. `evidence-bindings.md`
5. `ai-use-log.md`
6. `outline.md`
7. `one-section-draft.md`
8. `review-report.md`

완성 논문이 아니라, 지도교수와 동료가 바로 비평할 수 있는 검토 패키지가 목표입니다.

## 공개 자료 경계

이 폴더는 공개 저장소에 둘 수 있는 자료만 포함합니다.

- 원자료, 인터뷰 원문, 참여자 단위 자료, private link는 넣지 않습니다.
- 프롬프트는 워크숍용으로 재작성한 adapted prompt입니다.
- 외부 영상이나 README의 긴 원문 프롬프트/자막을 그대로 복제하지 않습니다.
- 로컬 모델은 정책 우회만을 목적으로 쓰는 것이 아니라, privacy와 비용, 검증 가능성을 위한 선택지로 설명합니다.
