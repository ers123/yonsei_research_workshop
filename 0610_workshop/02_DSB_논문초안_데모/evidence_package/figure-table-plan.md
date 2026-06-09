# Figure and Table Plan

상태: Visual-Assets Producer 기준으로 확장됨

이 파일은 간단한 목록이 아니라, Word/APA draft에 어떤 표와 그림을 어디에 넣을지 정하는 production plan이다. 전체 registry는 `figures/visual-manifest.md`를 따른다.

## Tables

| ID | Title | Purpose | Source | Safety label | Placement |
|---|---|---|---|---|---|
| Table 1 | Compact Multi-Thread Workflow Roles | Codex가 연구 업무를 판단 기능별로 나누는 방식을 보여준다 | README, compact model, compact-run map | workflow documentation only | Appendix A |
| Table 2 | Claim Gate and Evidence Binding Matrix | 각 draft claim이 source gate를 통과했는지 보여준다 | `evidence/evidence-bindings.md`, `context/do-not-claim.md` | source-gate documentation only | Appendix A |
| Table 3 | Aggregate Descriptive Pre/Post Summary | screen time과 step count의 집계 기술통계를 원자료 없이 보여준다 | `data/sanitized-summary.md` | aggregate only; descriptive only | Results Section 5.1 |

## Figures

| ID | Title | Asset path | Purpose | Safety label | Placement |
|---|---|---|---|---|---|
| Figure 1 | Intervention Concept Diagram | `figures/approved/figure-1-intervention-concept.png` | 실제 screenshot 없이 intervention 구조를 설명한다 | illustrative only; no private screenshot | Section 3.2 |
| Figure 2 | Aggregate Pre/Post Descriptive Trend | `figures/approved/figure-2-aggregate-prepost.png` | 집계 평균의 pre/post 방향을 보여준다 | aggregate only; descriptive only; no inferential test | Results Section 5.1, after Table 3 |
| Figure 3 | Interpretive Mechanism Map | `figures/approved/figure-3-interpretive-mechanism.png` | PBC lens와 planning/self-monitoring 가능성을 해석 모델로 보여준다 | interpretive only; not a causal pathway | Discussion Section 6.1 or 6.5 |

## Generation Rule

1. Spec은 `figures/specs/`에 둔다.
2. 생성 초안은 `figures/generated/`에 둔다.
3. 최종 승인본만 `figures/approved/`에 둔다.
4. Word 문서는 `figures/approved/`만 참조한다.
5. rejected visual은 `figures/rejected/`에 두고 manifest에 거절 이유를 기록한다.

## Prohibited Visuals

- 실제 앱 screenshot
- child/family photorealistic generated scene
- participant-level line chart
- raw quote word cloud
- p-value 또는 significance star가 있는 chart
- causal proof처럼 보이는 mechanism diagram
