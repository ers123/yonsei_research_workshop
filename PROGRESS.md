# Workshop Progress — 2026-04-15

## 워크숍 개요
- **일시**: 2026-04-24 (금) 13:30-15:30
- **장소**: 연세대학교 생활과학대학
- **주제**: 연구자를 위한 AI Agent 실전 — 맥락 설계 · 대량 자료 처리 · 연구 조수 팀
- **Repo**: github.com/ers123/yonsei_research_workshop

---

## 완료 (2026-04-15)

### 질적연구 데모 (`demo/qualitative_research/`)
- [x] PLAN.md 익명화 (실명/기관명 제거, grep 검증 0 hits)
- [x] codebook.md — 분석 체계 전체 보존
- [x] deliverables — final_report_excerpt.md, policy_memo_excerpt.md
- [x] visualizations — viz_institutional_heatmap.html (Plotly 인터랙티브)
- [x] README.md, CLAUDE.md — 데모 개요 + 에이전트 맥락 문서

### RA 팀 구성 (`hands_on/`)
- [x] ra_team_setup.md — Claude Code + Ollama 연결, 모델 선택 가이드
- [x] ra_team_tiers.md — Free($0)/Standard($20)/Full($220-420) 비용 비교, 웹검색으로 가격 검증
- [x] reference_setup_m4_32gb.md — 강사 환경 (M4 32GB) 레퍼런스

### 모델 구성
- [x] Ollama 모델 설치: qwen3.5:9b, deepseek-r1:14b, gemma4:26b, nomic-embed-text
- [x] Claude Code + Ollama 연결 방법 확인 (ANTHROPIC_AUTH_TOKEN=ollama)
- [x] Codex CLI, Gemini CLI 동작 확인
- [x] 로컬 모델 속도 테스트: gemma4 E4B가 가장 현실적 (qwen3.5 thinking 모드 과도하게 느림)

### Scenario B 파이프라인 (`hands_on/scenario_comparison/scenario_b/`)
- [x] CLAUDE.md — 프로젝트 맥락 문서
- [x] 01_topic_candidates.md — 주제 후보 5개 (웹검색 기반)
- [x] 02_literature_review.md — 선행연구 14건 (URL 5건 직접 방문 검증)
- [x] 03_verification.md — DeepSeek R1 14B 교차검증
- [x] 04_research_questions.md — RQ 도출 (검증 반영)
- [x] 05_cross_validation_4models.md — **4모델 교차검증** (DeepSeek, Gemma4, Codex, Gemini)

### 실습 가이드 (`hands_on/prompts_v2/`)
- [x] track_a_맥락문서.md — harness 관점 업데이트
- [x] track_b_대량처리.md — /loop 팁 + harness 프레이밍 추가
- [x] track_c_연구조수팀.md — **전면 재작성** (4모델 교차검증, 반증가능성, Codex/Gemini 호출법)

### 기타
- [x] SETUP.md — 사전 설치 가이드
- [x] templates/ — CLAUDE.md.example, AGENTS.md.example
- [x] appendix/ — 로컬AI 가이드, LLM Wiki 가이드, references
- [x] .gitignore

---

## 미완료 — 내일 작업 예정

### 슬라이드 디자인
- [ ] v3 MARP 디자인 교체 (Tesla 제거 → professional + scholarly)
- [ ] 작년 recap 2장 통합
- [ ] 4모델 교차검증 하이라이트 슬라이드 추가
- [ ] harness engineering 데모 흐름 시각화
- [ ] 최종 PPTX 생성

### 내용 보완
- [ ] appendix/01 로컬AI 가이드에 DeepSeek R1 / Gemma4 E4B 비교 결과 반영
- [ ] NTIS 검색 방법 안내 (API vs 웹검색 우회)

---

## 핵심 발견 (오늘)

### 워크숍 하이라이트: 4모델 교차검증 = 반증가능성
- 같은 연구 설계를 4개 계열 모델(DeepSeek, Gemma4, Codex, Gemini)이 각각 공격
- 모델마다 다른 문제를 잡음 — 하나만 썼으면 놓쳤을 것
- 3/4 이상 공통 지적: "사회문제에 기술적 해결책 과도 적용"
- Popper의 반증가능성 원칙이 AI 연구 파이프라인에 내장

### 로컬 모델 현실
- qwen3.5:9b: thinking 모드 때문에 "안녕"에 3분 29초 → 파이프라인 비현실적
- gemma4:26b (MoE): 빠르지만 32GB 전용
- gemma4 E4B (4B): 16GB 노트북에서 현실적, **4B가 14B보다 더 깊은 비판 제공** (크기≠품질)
- 로컬 모델의 킬러 유스케이스 = IRB 민감자료 처리 (무료 대안이 아님)

### 비용 구조
- 검증은 로컬 → $0, 무한 반복 가능
- 판단(검색, 글쓰기)은 클라우드 → $20 Pro면 충분
- $0→$20 점프가 가장 큰 품질 향상

---

## 커밋 히스토리 (15 commits)

```
99e96ce Update all three tracks with harness engineering framing
d386702 Add remaining workshop materials: appendix, setup, prompts, templates
af6120f Rewrite Track C with 4-model cross-validation as highlight
eee89ea Add 4-model cross-validation results with falsifiability analysis
e93b726 Add RA team tier guide (Free/Standard/Full) with verified pricing
ce1f5e6 Add Scenario B research pipeline results (Claude Pro + local verifier)
45b0af6 Add model loading time guidance to RA team setup
742c8c0 Update TODO.md with correct Ollama connection steps
931a875 Fix Claude Code + Ollama connection method
4b8d207 Add A/B scenario comparison exercise for RA team pipeline
fc87960 Add instructor reference setup for M4 32GB environment
f3e5ba1 Update RA team guide with DeepSeek R1 14B and 3-family cross-validation
46f521a Add RA team setup guide for local model research workflow
57ad398 Add anonymized qualitative research demo deliverables
817bcda Add anonymized qualitative research demo plan
```
