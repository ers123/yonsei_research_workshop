# 연구자를 위한 AI Agent 실전 — 연세대학교 생활과학대학 워크숍 (2026)

> 맥락 설계 · 대량 자료 처리 · 연구 조수 팀

본 repository는 2026년 4월 연세대학교 생활과학대학에서 진행한 워크숍의 자료 모음입니다.
참가자가 워크숍 이후에도 혼자서 따라 해볼 수 있도록 구성되었습니다.

강사: **이요한** (HarmonyOn) · amazone1@daum.net

---

## 이 repo를 보는 3가지 방법

### 1. 워크숍에 참석하셨다면 — 복기용
- `slides/`에서 당일 슬라이드 다시 보기
- `hands_on/prompts_v2/`에서 본인 트랙 프롬프트 복붙해서 재실행
- `appendix/`에서 심화 주제 (로컬 AI, LLM Wiki) 읽기

### 2. 워크숍을 놓치셨다면 — 자습용
1. `slides/Vibe_Researching_Workshop_2026_v2.pdf` 먼저 훑기
2. `hands_on/SETUP.md`로 환경 준비
3. `hands_on/prompts_v2/`의 트랙 A → B → C 순서대로 실행
4. `demo/qualitative_research/`에서 실제 프로젝트 사례 감 잡기

### 3. 이것을 본인 강의에서 재활용하고 싶다면
- `slides/src/`에 PPTX 생성 소스(pptxgenjs) 전체 공개
- `create_slides_v2.js` 수정 후 `node create_slides_v2.js`로 본인 버전 제작 가능
- CC BY-NC-SA 4.0 라이선스 (비영리 공유 OK, 수정 버전도 같은 조건)

---

## 폴더 안내

```
├── slides/                           — 강의 슬라이드
│   ├── Vibe_Researching_Workshop_2026_v2.pptx
│   ├── Vibe_Researching_Workshop_2026_v2.pdf
│   └── src/                          — 슬라이드 소스 (pptxgenjs)
│
├── appendix/                         — 별첨 자료
│   ├── 01_로컬AI_무료_활용_가이드.md
│   ├── 02_LLM_Wiki_지식베이스_가이드.md
│   └── references.md                 — 워크숍 인용 자료 전체
│
├── hands_on/                         — 실습 자료
│   ├── SETUP.md                      — 사전 환경 설치
│   ├── prompts_v2/                   — 3 트랙 실습 프롬프트
│   │   ├── track_a_맥락문서.md
│   │   ├── track_b_대량처리.md
│   │   └── track_c_연구조수팀.md
│   ├── prompts/                      — V1 프롬프트 (참고용)
│   └── templates/                    — CLAUDE.md, AGENTS.md 템플릿
│
└── demo/
    └── qualitative_research/         — 질적연구 mini 데모
        ├── PLAN.md                   — 데모 생성 계획
        └── (Claude Code로 PLAN.md 따라 생성)
```

---

## 워크숍 구성 (2시간)

| 파트 | 시간 | 내용 |
|---|---|---|
| Part 1 | 13:30–14:00 | **왜, 어떻게 바뀌고 있나** — 3단계 진화 (Prompt → Context → Harness) + 용어 정리 |
| Part 2 | 14:00–14:45 | **강사 실전 사례 3가지** — ① 맥락 문서 ② 대량 자료 처리 ③ 연구 조수 팀 |
| Part 3 | 14:45–15:30 | **스튜디오 실습** — 3 트랙 중 선택, 강사가 돌며 코칭 |

### 3 트랙

- **트랙 A — 맥락 문서 만들기**: 본인 연구에 CLAUDE.md를 적용해보고, 맥락 유/무 차이를 비교
- **트랙 B — 대량 자료 처리**: 샘플 PDF 10건으로 추출 → 구조화 → 조회를 한 사이클
- **트랙 C — 연구 조수 팀 맛보기**: Claude Code + Ollama로 역할별 에이전트 구성

---

## 핵심 메시지

올해의 주제는 **"도구 사용"에서 "에이전트 설계"로의 전환**입니다.

| | 2025 (작년) | 2026 (올해) |
|---|---|---|
| 모델 | 연구자가 조작자 | 연구자가 설계자 |
| 키워드 | Prompt Engineering | Context → Harness Engineering |
| 결과물 | 한 번에 하나 | 반복 가능한 흐름 |
| 맥락 | 매번 새로 | CLAUDE.md에 축적 |

단, **이는 자동화 극단(Sakana AI Scientist)이 아닙니다.** Zhang (2026)의 "Vibe Researching"이 말하는 중도 — 연구자가 의도와 검증을 책임지고, 에이전트가 실행 기술을 맡는 — 가 우리의 포지션입니다.

검증부채(Verification Debt, Kwon 2026), AI Brain Fry (BCG 2026) 같은 리스크도 함께 고려합니다. `slides/` 후반부 참조.

---

## 피드백 / 문의

- 내용 관련: amazone1@daum.net
- 레포 이슈: GitHub Issues

---

## 라이선스

- 코드 (pptxgenjs 스크립트, 프롬프트 템플릿): **MIT**
- 문서 (슬라이드 내용, 별첨, README): **CC BY-NC-SA 4.0**
- 인용된 외부 자료: 각 저자 저작권 유효 (`appendix/references.md` 참조)
