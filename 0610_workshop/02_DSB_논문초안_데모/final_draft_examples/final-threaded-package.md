# Final Threaded Demo Package

상태: 대학원 연구실 발표용 최종 패키지

## 한 줄 설명

자료를 모으면 AI가 논문 초안을 만들 수 있다. Codex를 쓰면 그 과정을 문헌, 방법, 데이터, 검증, 초안, 리뷰, 패키징 thread로 나누어 연구보조원에게 위임하듯 운영할 수 있다.

## 최종 초안

최종 초안은 세 층으로 둔다.

- thread 반환 원본: `paper-project/threads/revision/return-revised-draft.md`
- 이전 발표용 확장 원고: `paper-project/draft/expanded-revised-draft.md`
- 최신 5-worker compact-run 병합 원고: `paper-project/draft/compact-thread-expanded-draft.md`

thread 반환 원본은 실제 researcher thread가 반환한 초안의 기록이다. 이전 발표용 확장 원고는 그 반환물을 바탕으로 supervisor가 서론, 이론, 방법, 결과, 논의, 표/그림 계획을 더 길게 풀어 쓴 long-form exploratory draft다. 최신 compact-run 병합 원고는 supervisor 하나와 worker 5개만으로 같은 목표를 더 깔끔하게 수행한 최종 시연용 원고다. 세 문서 모두 투고용 완성 원고가 아니다.

## 실제 실행 결과

### Compact 5-worker run

| Role | Result |
|---|---|
| Evidence-Literature | returned |
| Data-Methods | returned |
| Drafting | returned |
| Review-Verification | returned |
| Visual-Assets | returned |

Compact run은 현재 대화를 supervisor로 유지하고 worker thread를 정확히 5개만 만들었다. 각 worker는 자기 반환 파일 하나만 작성했고, supervisor가 `threads/compact-run/supervisor/merge-report.md`에서 병합 원칙을 정리한 뒤 `draft/compact-thread-expanded-draft.md`로 확장 원고를 만들었다.

### Earlier verbose run

| Role | Result |
|---|---|
| literature-review | returned |
| methods-evidence | returned |
| data-readiness | returned |
| figure-table | returned |
| source-verifier | returned |
| outline | returned |
| drafting | returned |
| reviewer | returned |
| revision | returned |
| packaging | completed by fallback generation |

일부 thread는 초기에 지연되어 supervisor checkpoint를 준비했지만, 최종 확인 시 outline, drafting, reviewer, revision 산출물까지 반환되었다. packaging 단계는 반환된 9개 입력 산출물을 기준으로 fallback generation 방식으로 최종 패키지를 완성했다.

## 발표에서 보여줄 핵심 파일

1. `README.md`
2. `threads/compact-run/thread-map.md`
3. `threads/compact-run/supervisor/merge-report.md`
4. `draft/compact-thread-expanded-draft.md`
5. `threads/visual-assets-producer-role.md`
6. `figures/visual-manifest.md`
7. `prompts/compact-parallel-research-lab-prompt-pack.md`
8. `draft/apa7-visual-thread-paper-draft.docx`
9. `draft/apa-word-draft-checklist.md`
10. `threads/parallel-research-lab-framework.md`
11. `threads/compact-thread-model.md`
12. `threads/thread-explosion-postmortem.md`
13. `lab-walkthrough-guide.md`

## 발표 메시지

### 1. AI 초안 작성은 가능하다

자료, 연구질문, 선행연구, 데이터 요약, 인터뷰 메모가 있으면 AI는 논문 초안을 만들 수 있다. 하지만 바로 완성본으로 믿으면 안 된다.

### 2. Codex의 차이는 분산 운영이다

한 chat이 전부 쓰는 방식이 아니라, 여러 thread가 서로 다른 연구 업무를 맡는다. 문헌 담당자는 문헌 위치를 잡고, 데이터 담당자는 수치 claim을 제한하고, verifier는 과장 주장을 막는다.

발표용으로는 thread를 너무 많이 만들지 않는다. 권장 기본값은 supervisor 하나와 worker thread 5개다: Evidence-Literature, Data-Methods, Drafting, Review-Verification, Visual-Assets.

### 3. 총괄 thread는 연구실장 역할이다

총괄 thread는 직접 모든 내용을 만들기보다 지시, 반환 수집, 충돌 조정, gate 관리, 최종 병합을 담당한다.

### 4. 반환 지연도 운영의 일부다

일부 thread가 지연되면 supervisor checkpoint를 준비한다. 이것은 실패가 아니라 실제 연구 운영에서 필요한 rescue pattern이다. 나중에 해당 thread가 반환하면 checkpoint와 비교해 반영하면 된다. 이번 데모에서도 초기에 지연된 단계가 있었고, 최종 패키지는 반환된 산출물과 fallback 기록을 함께 남겼다.

## 학생들에게 강조할 점

- "논문 써줘"보다 "자료를 정리하고 역할을 나눠라"가 중요하다.
- 좋은 초안은 source-gated claim에서 나온다.
- AI가 쓴 문장은 항상 allowed, caveated, blocked claim으로 나눠야 한다.
- raw data, interview quote, participant names는 쉽게 초안에 넣으면 안 된다.
- 그림과 이미지는 Visual-Assets thread에서 먼저 figure specification, prompt, caption, privacy check를 만든 뒤 사용한다.
- 최종 Word/APA draft에는 `figures/approved/` 안의 승인된 figure만 넣고, 각 visual의 위치는 `figures/visual-manifest.md`로 관리한다.
- 최종 판단은 human signoff가 필요하다.

## 다음 단계

이 패키지를 실제 투고용으로 발전시키려면 다음 작업이 필요하다.

1. 최신 문헌 추가 검색과 원문 대조
2. 정량 분석 규칙 확정
3. 결측 처리와 대조군 metadata 확인
4. 정성 인터뷰 formal coding
5. 익명화 quote 승인
6. 통계 분석 또는 적절한 비모수/탐색 분석
7. 학술지 양식에 맞춘 참고문헌 정리
8. 지도교수 및 공동연구자 human signoff
