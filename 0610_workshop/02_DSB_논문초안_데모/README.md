# 02. DSB 논문초안 데모

이 폴더는 DSB 연구자료를 바탕으로 만든 논문 초안 패키지입니다.

목표는 "AI가 투고 가능한 논문을 완성했다"가 아닙니다. 목표는 자료가 있을 때 AI를 이용해 검토 가능한 초안, 근거 연결, 위험 메모, 비평 기록, 시각자료 계획을 만들 수 있음을 보여주는 것입니다.

## 먼저 볼 파일

| 순서 | 파일 | 설명 |
|---|---|---|
| 1 | `final_draft_examples/manuscript-draft-ko-v0.2.md` | 한국어 논문 초안 |
| 2 | `final_draft_examples/manuscript-draft-en-v0.2.md` | 영어 논문 초안 |
| 3 | `final_draft_examples/apa7-visual-thread-paper-draft.docx` | 그림/표가 포함된 APA 7-style Word 시연 예시 |
| 4 | `evidence_package/evidence-bindings.md` | 어떤 claim이 어떤 근거에 기대는지 |
| 5 | `risk_and_review/peer-review-risk-memo-v0.2.md` | 동료심사 관점의 위험 메모 |
| 6 | `evidence_package/visual-manifest.md` | figure/table 위치와 caption 관리 |

## 데모 주제

스크린타임과 신체활동을 연결하는 시각적 바 인터페이스가 아동의 지각된 행동 통제와 스마트폰 사용 자기조절을 어떻게 형성할 수 있는지 검토합니다.

현재 초안이 주장할 수 있는 것:

- 시각적 바는 행동 결과를 더 잘 보이게 하는 디자인 요소로 해석될 수 있다.
- DSB 선행 파일럿/학술대회 자료는 디자인 개입의 계보를 설명하는 데 사용할 수 있다.
- 질적 자료는 계획, 부모-자녀 협상, 피드백/피드포워드, 인센티브/페널티 해석에 대한 잠정 주제를 지원한다.
- 정량 데이터는 분석 가능성이 있지만, 정제/통계 규칙 승인 전에는 인과나 효과를 주장할 수 없다.

현재 초안이 주장하면 안 되는 것:

- 임상적 효과
- 보편적 스크린타임 감소
- 검증된 인과효과
- 지속적 습관 형성
- 승인되지 않은 직접 인용
- 투고 가능 또는 publication-ready 상태

## 폴더 구성

```text
final_draft_examples/
  manuscript-draft-ko-v0.2.md
  manuscript-draft-en-v0.2.md
  apa7-visual-thread-paper-draft.docx
  compact-thread-expanded-draft.md
  figures/

evidence_package/
  drafting-brief.md
  materials-inventory.md
  findings-summary.md
  evidence-bindings.md
  section-architecture.md
  argument-outline.md
  visual-manifest.md

risk_and_review/
  draft-risk-report.md
  peer-review-risk-memo-v0.2.md
  review-report.md
  draft-package.md
```

## 강조 사항

이 초안은 원자료를 그대로 외부 모델에 던져 만든 것이 아닙니다. 먼저 자료를 정리하고, claim과 evidence를 묶고, 위험한 주장을 차단한 뒤, 검토 가능한 초안으로 만든 예시입니다.

이 폴더는 원자료 없이 sanitized package를 중심으로 구성되어 있습니다. 따라서 "실제 원자료를 새로 분석하는 장면"을 보여주는 시연이 아니라, 이미 정리된 자료 패키지에서 논문 초안, 근거 연결, 위험 검토, 시각자료 계획을 어떻게 관리하는지 보여주는 시연입니다.

Word 파일은 APA-like 또는 APA 7-style 형식을 보여주는 데모용 문서입니다. 실제 투고용 APA final manuscript라고 설명하면 안 됩니다.

참고문헌, conference paper metadata, internal technical disclosure, 특허/앱 관련 서술은 외부 배포 전 human verification이 필요합니다.

```text
초안보다 중요한 것은 이 초안이 어떤 자료에 기대고, 어떤 주장을 아직 하지 않으며, 어떤 human review가 남았는지를 설명할 수 있다는 점입니다.
```
