# Compact Codex Thread Model

상태: 발표용 권장 모델

## 왜 compact model이 필요한가

이번 실행에서는 역할을 매우 세밀하게 나누어 thread가 많이 생성되었다. 이 방식은 "업무를 연구보조원에게 나누어 맡긴다"는 구조를 검증하기에는 좋지만, 연구실 발표 화면에서는 thread 목록이 복잡해 보일 수 있다.

따라서 실제 수업 시연에서는 5-6개 역할로 줄이는 편이 낫다. 핵심은 역할 수를 많이 만드는 것이 아니라, 서로 다른 판단 기능을 분리하는 것이다.

자세한 원인 분석은 `paper-project/threads/thread-explosion-postmortem.md`에 남겼다. 이 파일은 기존 verbose thread들을 삭제하지 않고, 왜 목록이 길어졌는지와 다음 프로젝트에서 어떻게 피할지를 설명하는 수업용 실패 사례다.

## 권장 thread 구성

| Thread | 역할 | 반환 파일 |
|---|---|---|
| Supervisor | 전체 지휘, phase gate, 병합, 최종 판단 | `threads/supervisor/merge-report.md` |
| Evidence-Literature | 연구 질문, 문헌 위치, 이론 렌즈, 선행연구 gap | `threads/evidence-literature/return-report.md` |
| Data-Methods | 데이터 readiness, 분석 가능 범위, 방법 한계 | `threads/data-methods/return-report.md` |
| Drafting | outline, 1차 초안, 확장 초안 | `threads/drafting/return-draft.md` |
| Review-Verification | source gate, privacy gate, overclaim review | `threads/review-verification/return-review.md` |
| Visual-Assets Producer | 표/그림 식별, spec, 생성, approved asset, caption, Word placement, visual privacy check | `figures/visual-manifest.md` |

## 추천 운영 방식

1. Supervisor thread는 현재 대화 하나로 유지한다.
2. Worker thread는 5개만 만든다.
3. 각 worker thread는 자기 반환 파일 하나만 작성한다.
4. Supervisor만 모든 반환 파일을 읽고 병합한다.
5. Visual-Assets Producer thread는 실제 이미지 생성보다 먼저 figure/table specification과 manifest를 만든다.
6. 이미지 생성이 필요하면 Visual-Assets Producer가 안전한 prompt와 caption을 만들고, 생성 초안을 `figures/generated/`에 둔다.
7. Supervisor 승인 후에만 최종본을 `figures/approved/`로 옮기고 Word 문서에 삽입한다.

## Thread Explosion 방지 규칙

새 thread를 만들기 전에는 아래 기준을 확인한다.

| 질문 | 새 thread 생성 기준 |
|---|---|
| 기존 worker가 처리할 수 없는 새 전문성인가? | 예일 때만 생성 |
| 병렬로 독립 수행 가능한가? | 예일 때만 생성 |
| 반환 파일이 하나로 명확한가? | 예일 때만 생성 |
| phase가 아니라 판단 기능인가? | 예일 때만 생성 |
| 목록이 발표 화면에서 관리 가능한가? | 예일 때만 생성 |

outline, drafting, revision은 새 thread 3개가 아니라 Drafting thread 하나로 묶는다. source verification과 reviewer도 Review-Verification thread 하나로 묶는다. packaging은 별도 worker thread보다 supervisor의 최종 병합 업무로 둔다.

## 왜 Visual-Assets Producer thread가 필요한가

논문 작성에서 이미지는 장식이 아니라 주장 구조를 바꾸는 산출물이다. 특히 연구실 시연에서는 다음 위험이 있다.

- 실제 앱 screenshot에 private information이 들어갈 수 있다.
- participant-level trend chart가 개인 패턴을 노출할 수 있다.
- causal arrow가 효과 입증처럼 보일 수 있다.
- image prompt가 원자료에 없는 장면을 사실처럼 만들 수 있다.

Visual-Assets Producer thread는 이 위험을 막기 위해 다음을 담당한다.

- 어떤 표와 그림이 필요한지 결정한다.
- 각 그림이 어떤 claim을 보조하는지 표시한다.
- 집계값만 사용하는지 확인한다.
- 실제 screenshot 대신 concept diagram으로 충분한지 판단한다.
- generated image를 쓸 경우 "illustrative only" 라벨과 caption을 준비한다.
- 생성 파일을 `figures/generated/`와 `figures/approved/`로 분리한다.
- `figures/visual-manifest.md`에 원고 삽입 위치를 정확히 기록한다.

## 발표용 한 문장

> 실제 운영에서는 thread를 많이 만드는 것이 목표가 아닙니다. Supervisor 하나와 5개 worker thread 정도면 충분합니다. 중요한 것은 문헌, 데이터, 초안, 검증, 시각화 판단을 서로 다른 눈으로 보게 만드는 것입니다.

## Visual-Assets Producer 산출물

| Output | Path |
|---|---|
| Role definition | `04_Codex_multi_thread_고급예시/compact-parallel-research-lab-prompt-pack.md` |
| Visual registry | `02_DSB_논문초안_데모/evidence_package/visual-manifest.md` |
| Approved demo assets | `02_DSB_논문초안_데모/final_draft_examples/figures/` |
| Optional generated drafts | `02_DSB_논문초안_데모/final_draft_examples/figures/` or a separate temporary workspace |

## Compact prompt template

```text
당신은 [역할명] thread다.

목표:
- supervisor가 제공한 자료만 사용한다.
- 자기 역할에 해당하는 판단만 수행한다.
- 확정할 수 없는 내용은 human-only 또는 needs-verification으로 표시한다.
- 원자료, 실명, raw quote, private link, participant-level detail은 포함하지 않는다.
- 결과는 지정된 반환 파일 하나에만 작성한다.

반환 형식:
# [Role] Return
## 핵심 3줄
## 사용한 입력
## 허용 가능한 주장
## 제한해야 할 주장
## 초안에 반영할 문장
## 다음 thread에 넘길 질문
```

## 언제 더 잘게 나눌 것인가

5-6개 모델로 충분하지 않은 경우만 역할을 더 나눈다.

- 데이터가 여러 종류라서 정량/정성을 분리해야 할 때
- figure가 실제 제출용 품질까지 필요할 때
- reviewer를 방법론 reviewer와 writing reviewer로 분리해야 할 때
- 참고문헌 원문 대조가 많아 별도 citation auditor가 필요할 때
- IRB, 개인정보, 익명화 검토가 별도 책임으로 필요한 때

그 외에는 compact model을 기본으로 둔다.
