# 연구자를 위한 AI Agent 실전 — 연세대학교 생활과학대학 워크숍 (2026)

> 맥락 설계 · 대량 자료 처리 · 연구 조수 팀

본 repository는 2026년 4월 연세대학교 생활과학대학에서 진행한 워크숍의 자료 모음입니다.
참가자가 워크숍 이후에도 혼자서 따라 해볼 수 있도록 구성되었습니다.

강사: **이요한** (HarmonyOn) · yohan.harmony@gmail.com

---

## 이 repo를 보는 3가지 방법

### 1. 워크숍에 참석하셨다면 — 복기용
- 슬라이드는 Google Drive 링크(강사에게 요청)로 다시 보기
- `hands_on/prompts/`에서 본인 트랙 프롬프트 복붙해서 재실행
- `appendix/`에서 심화 주제 (로컬 AI, LLM Wiki) 읽기

### 2. 워크숍을 놓치셨다면 — 자습용
1. Google Drive 의 슬라이드 먼저 훑기 (강사 이메일로 링크 요청)
2. `hands_on/SETUP.md`로 환경 준비
3. `hands_on/prompts/`의 트랙 A → B → C 순서대로 실행
4. `demo/qualitative_research/`에서 실제 프로젝트 사례 감 잡기

### 3. 이것을 본인 강의에서 재활용하고 싶다면
- 프롬프트/템플릿/핸즈온 자료는 전부 공개 (CC BY-NC-SA 4.0)
- 비영리 공유 OK, 수정 버전도 같은 조건

---

## 폴더 안내

```
├── (슬라이드는 Google Drive 로 별도 공유 — 강사에게 링크 요청)
│
├── appendix/                         — 별첨 자료
│   ├── 01_로컬AI_무료_활용_가이드.md  — Ollama, 모델 비교, 비용
│   ├── 02_LLM_Wiki_지식베이스_가이드.md — 개인 지식 축적 구조
│   └── 04_Uncensored_로컬모델_연구활용_가이드.md — 민감 코퍼스·합성 데이터 심화 가이드
│
├── hands_on/                         — 실습 자료
│   ├── SETUP.md                      — 사전 환경 설치 (Mac/Windows/Linux)
│   ├── prompts/                      — 트랙 실습 프롬프트 + 예시
│   │   ├── track_a_맥락문서.md
│   │   ├── track_b_대량처리.md
│   │   ├── track_c_연구조수팀.md      — 강사 데모 스크립트 + 홈스터디
│   │   └── track_c_홈스터디_완주예시.md — 외부 도움 없이 완주 가능한 단계별
│   ├── templates/                    — CLAUDE.md, AGENTS.md 템플릿 + 비교 예시
│   │   ├── CLAUDE.md.example
│   │   ├── CLAUDE.md.filled_example  — 완성된 맥락 문서 사례
│   │   ├── AGENTS.md.example
│   │   └── A_vs_B_response_examples.md — Track A 비교 응답 예시
│   ├── references/                   — Claude Code 퀵가이드 + AI Index 2026 원본/추출백업/비교예시
│   │   ├── claude_code_퀵가이드.md
│   │   └── ai_index/                 — Track B 실습 자료 (PDF 37MB + 백업 + Naive vs Harness 예시)
│   ├── scenario_comparison/          — 4모델 교차검증 실제 결과 (Scenario B)
│   ├── ra_team_setup.md              — RA 팀 상세 구성 가이드
│   └── ra_team_tiers.md              — Free/Standard/Full 비용 비교
│
└── demo/
    └── qualitative_research/         — 질적연구 데모 (PDF→코드북→분석)
```

> **슬라이드(.pptx)**: 공개 repo 에는 포함하지 않고 Google Drive 로 별도 공유. 링크는 yohan.harmony@gmail.com 로 요청.
> **Streamlit "나만의 연구팀" 앱**: 강사 라이브 데모 전용 소스로 공개 repo 에서 제외. 같은 개념을 **Claude Code + Ollama** 터미널 기반으로 재현하는 가이드는 `hands_on/ra_team_setup.md` 와 `hands_on/prompts/track_c_연구조수팀.md` 에 있음.

---

## 워크숍 구성 (2시간)

| 파트 | 시간 | 내용 |
|---|---|---|
| Part 1 | 13:30–14:00 | **왜, 어떻게 바뀌고 있나** — 3단계 진화 (Prompt → Context → Harness) + 용어 정리 |
| Part 2 | 14:00–14:45 | **강사 실전 사례 3가지** — ① 맥락 문서 ② 대량 자료 처리 ③ 연구 조수 팀 (라이브 데모) |
| Part 3 | 14:45–15:30 | **스튜디오 실습** — Track A + B **전원 진행**, 강사가 돌며 코칭 |

### 실습 구조 (2026-04-18 개편)

```
Part 3 실습 (45-50분)
├─ Track A — 맥락 문서 만들기 (20-25분)
│   본인 CLAUDE.md 작성 + 맥락 유/무 비교
│
└─ Track B — 대량 자료 처리 (30-35분)
    AI Index 2026 PDF로 Naive vs Harness 비교
```

- **트랙 A**: 브라우저만 있으면 OK. 본인 연구 주제에 맞는 `CLAUDE.md`를 만들고, 맥락 유/무에서 같은 질문이 얼마나 달라지는지 체감
- **트랙 B**: 강사 제공 AI Index Report 2026 (37MB 공개 리포트)로 "Naive 접근 vs 중간 산출물 추출" 대비 실습. Claude Code 있으면 직접 추출, 없으면 미리 준비된 추출본 사용

### Track C는?

**Part 2 라이브 데모** (강사 시연 12-15분, "나만의 연구팀" 앱 시연 중심) + **홈스터디 가이드** (리포에서 단계별 재현 가능).

로컬 모델 설치는 노트북 편차가 커서 45분 안에 전원 성공 보장이 어려움. 대신 시연으로 전체 구조를 보여주고, 관심 있는 분은 집에서 차분히 따라 하실 수 있도록 했습니다. 상세: `hands_on/prompts/track_c_연구조수팀.md`

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

검증부채(Verification Debt, Kwon 2026), AI Brain Fry (BCG 2026) 같은 리스크도 함께 고려합니다. 슬라이드 후반부 참조.

---

## 피드백 / 문의

- 내용 관련: yohan.harmony@gmail.com

---

## 라이선스

- 코드 (pptxgenjs 스크립트, 프롬프트 템플릿): **MIT**
- 문서 (슬라이드 내용, 별첨, README): **CC BY-NC-SA 4.0**
- 인용된 외부 자료: 각 저자 저작권 유효
