# Compact Furthering Run Supervisor Merge Report

상태: 5-worker 반환 병합 완료

## 한 줄 요약

이번 compact run은 기존 verbose 실행과 달리 worker thread를 정확히 5개로 제한했고, 각 thread가 자기 전문 관점에서 기존 확장 원고를 furthering한 뒤 하나의 반환 파일만 작성했다.

## 반환 상태

| Worker | Return file | Status | Supervisor decision |
|---|---|---|---|
| Evidence-Literature | `evidence-literature/return.md` | returned | 서론 gap, 이론 연결, PBC lens, design mechanism 문단을 채택 |
| Data-Methods | `data-methods/return.md` | returned | analysis-ready but not inference-ready framing, missing/zero-step caveat, future analysis plan을 채택 |
| Drafting | `drafting/return.md` | returned | 섹션 간 transition, 반복 caveat 조정, workflow 축소, appendix 분리 지시를 채택 |
| Review-Verification | `review-verification/return.md` | returned | allowed/caveated/blocked/human-only gate를 최종 claim 기준으로 채택 |
| Visual-Assets | `visual-assets/return.md` | returned | 표 3개와 그림 3개의 source, caption, safety label, safe prompt를 채택 |

## 병합 원칙

1. 새 주장을 늘리지 않는다.
2. 기존 expanded draft를 처음부터 버리지 않는다.
3. 문헌은 확인되지 않은 저자명/연도/효과 크기를 만들지 않는다.
4. 정량 결과는 18명의 pre/post 기술통계로만 제한한다.
5. 정성 결과는 researcher memo-based theme으로만 제한한다.
6. PBC는 measured outcome이 아니라 interpretive lens로만 쓴다.
7. Visual assets는 aggregate, descriptive, illustrative, interpretive label을 붙인다.
8. Codex workflow는 empirical finding이 아니라 writing/verification workflow demonstration으로 둔다.

## 채택한 핵심 변경

### Evidence-Literature

- 연구 gap을 "screen time을 줄일 것인가"가 아니라 "screen time과 physical activity의 관계를 아동이 실시간 시각 상태로 읽고 자기조절 판단에 연결할 수 있는가"로 좁힌다.
- feedback/feedforward는 상태 이해와 미래 선택으로, incentive/penalty는 단기 조절과 자율성 긴장으로 paired explanation을 만든다.
- discussion은 effect claim이 아니라 design mechanism과 evidence limitation을 분리한다.

### Data-Methods

- 방법 section에서 전체 2,341개 일별 기록/19명 자료와 pre/post 비교 가능한 18명 subset을 명확히 분리한다.
- missing screen-time 555행, missing steps 67행, zero-step 211행을 결과와 한계 양쪽에 둔다.
- "analysis-ready exploratory summary, not inference-ready evidence" 문장을 새 framing으로 채택한다.

### Drafting

- 이론적 배경에서 개입 설명으로 넘어가는 bridge 문장을 추가한다.
- 결과 section은 "정량 기술통계 -> theme-level interpretation" 순서로 연결한다.
- AI workflow와 visual safety는 본문에서 과도하게 길어지지 않게 하고, 상세 내용은 appendix와 README로 분리한다.

### Review-Verification

- 모든 결과 문장은 "분석 가능한 18명", "pre/post 기술통계", "관찰 경향", "통계 검정/인과 추론/일반화 아님"으로 묶는다.
- 실명, raw quote, private link, participant-level trajectory, credential-like string은 계속 금지한다.
- "지원", "가능성", "기여" 같은 표현도 가까운 곳에 caveat를 둔다.

### Visual-Assets

- Appendix A를 `Classroom-Safe Table and Figure Plan`으로 재구성한다.
- Table 1, Table 2, Table 3과 Figure 1, Figure 2, Figure 3의 source, 포함 필드, caption, safety label을 명확히 한다.
- Figure 1은 concept diagram, Figure 2는 aggregate chart, Figure 3은 interpretive mechanism map으로 제한한다.

## 최종 산출물

- Compact-run merged draft: `paper-project/draft/compact-thread-expanded-draft.md`
- This merge report: `paper-project/threads/compact-run/supervisor/merge-report.md`
- Thread map: `paper-project/threads/compact-run/thread-map.md`

## 발표에서 설명할 점

이번 run은 기존 verbose run의 문제를 바로잡은 사례다. 기존에는 role thread, execution thread, phase-level thread, fallback thread가 겹쳐 thread list가 길어졌다. 이번에는 supervisor를 현재 대화로 유지하고 worker를 정확히 5개만 만들었다. 각 worker는 자기 return file 하나만 남겼고, supervisor가 병합했다.
