# Workshop Progress

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
- [x] ra_team_tiers.md — Free($0)/Standard($20)/Full($220-420) 비용 비교
- [x] reference_setup_m4_32gb.md — 강사 환경 (M4 32GB) 레퍼런스

### Scenario B 파이프라인 (`hands_on/scenario_comparison/scenario_b/`)
- [x] 01~05 전체 파이프라인 + 4모델 교차검증

### 실습 가이드 (`hands_on/prompts_v2/`)
- [x] track_a, track_b, track_c — harness 프레이밍 완료

### 기타
- [x] SETUP.md, templates/, appendix/01~02, references, .gitignore

---

## 완료 (2026-04-16)

### 슬라이드
- [x] v4 PPTX 빌드 (light background, Pretendard, 30 slides)
- [x] Recap (작년 워크숍 요약) 2장 통합 (slides 5-6)
- [x] 4모델 교차검증 하이라이트 슬라이드 (slide 23)
- [x] Harness Engineering 전체 데모 흐름 시각화 (slide 24)
- [x] 출처 슬라이드 3장 추가 (repo 구조 + 논문/기술 + 도구) → 33 slides
- [x] draft PPTX에 출처 페이지 반영 (사용자 최종 편집 중)

### 내용 보완
- [x] appendix/01 — DeepSeek R1 / Gemma4 E4B 비교 결과 반영
- [x] appendix/03 — NTIS 차별성검토 가이드 신규 작성
- [x] appendix/01 — Gemma 4 31B (Dense) 추가, Gemma 3 참조 제거

### 나만의 연구팀 Streamlit 앱 (`demo/streamlit_research_team/`)
- [x] app.py — 3-agent 파이프라인 (수연→준호→지은), academic UI 디자인
- [x] agents.py — 시스템 프롬프트 (법무팀→연구팀 변환)
- [x] templates.py — 연구 분야/단계 템플릿
- [x] PROMPTS.md — 법무팀↔연구팀 프롬프트 비교 문서
- [x] README.md — Mac/Windows 설치 + 트러블슈팅
- [x] 모델 자동감지 (plug & play) — `ollama pull <아무거나>` → 앱에서 바로 선택
- [x] E2E 테스트 통과 — gemma4 E4B로 3단계 파이프라인 완주 확인

### Hands-on 자료 보강
- [x] 전 트랙 "황금 규칙" (모르면 모델에게 물어보세요) 삽입
- [x] Track C 대폭 확장 — 설치부터 인증까지 단계별, FAQ 추가
- [x] Track C 심화 섹션 — Streamlit 앱 연결
- [x] SETUP.md 전면 개정 — OS별 표 (Mac/Windows/Linux), gemma4 통일, /loop 설명
- [x] sample_data/ 10건 가상 연구 논문 생성 (Track B 실습용)

### 리뷰 + 수정 (16개 이슈)
- [x] C1: sample_data/ 생성 (10 files + README)
- [x] C2: @openai/codex 패키지명 검증 (npmjs.com 확인)
- [x] C3: @google/gemini-cli 패키지명 검증 (npmjs.com 확인)
- [x] C4: README.md 폴더 구조 현행화 (draft PPTX, streamlit 앱 반영)
- [x] H1: Track A Windows 경로 안내
- [x] H2: Track A "결과를 저장" 구체화
- [x] H3: Track B mkdir 안내 추가
- [x] H4: ANTHROPIC env vars 일관성 검증
- [x] H5: claude --model 문법 검증
- [x] M1: Track B 출처 매핑 체크리스트 추가
- [x] M2: SETUP.md에 /loop 설명 추가
- [x] M3: Track A Step 5 축소 (선택 + 핵심 3줄)
- [x] M4: Track B demo 참조 명확화
- [x] M5: appendix→hands_on 역참조 추가
- [x] L1: AAR → 사후 회의
- [x] L4: scenario_a/ 삭제

---

## 완료 (2026-04-17)

### 폴더 정합성 점검 + 정리 (슬라이드 ↔ 폴더 cross-check)
- [x] Step 1 — PDF↔TXT 문구 통일
  - Track B 8곳, README.md 2곳, SETUP.md 1곳 수정
  - "샘플 문헌 10건(.txt)" + "본인 PDF 가져오면 동일 흐름" 명시
- [x] Step 2 — 루트 파일 정리
  - `.gitignore`에 `intereim_research.md`, `.omx/` 추가
  - `DESIGN.md` → `_working/` 이동 (Tesla 디자인 문서, Streamlit 앱은 academic로 확정)
  - `three-era-timeline.png` (slides/src/assets/와 중복), `package.json` (placeholder) 삭제
- [x] Step 3 — 구버전 아카이브
  - `slides/archive/` 생성 — original, v2, v3(.md/.pptx/.html), v4 (5 files) + README.md
  - `hands_on/prompts_archive/` 생성 — v1 4 files + README.md
  - 최종본 `slides/Vibe_Researching_Workshop_2026_draft.pptx` 단독 노출
- [x] Step 4 — README 폴더 안내 보강
  - 누락 3건 추가: `hands_on/references/`, `hands_on/scenario_comparison/`, appendix/01~03 설명 강화

---

### 슬라이드 최종 손질 (사용자 직접 — 완료)
- [x] Slide 24: `gemma3:4b` → `gemma4`, `qwen2.5:14b` → `deepseek-r1:14b`
- [x] Slide 28: "샘플 PDF 10건" → "샘플 문헌 10건(.txt)"
- [x] PROJECT.md 언급 → CLAUDE.md로 통일

---

## 완료 (2026-04-18) — 워크숍 구조 재설계 + Track 재작성

### 구조 재설계: A+B 전원 / C는 강사 데모
**배경**: 3 트랙 선택식이 평등해 보이나 실제 성공률 격차 큼 (A/B 85-95% vs C 30-50%, 비-IT 대학원생 Windows/Mac 혼합 기준). 리스크 분산 잘못됨.

**변경**:
- Part 3 실습: **Track A + B 전원 진행** (45-50분)
- Track C: **Part 2 사례 3 라이브 데모** (12-15분) + **홈스터디 가이드** (리포)

### Track B 전면 재작성 — AI Index 2026 기반
- **AI Index Report 2026** (37MB, 423 pages, Stanford HAI 공개) 실습 자료 채택
- **Naive vs Harness** 4-part 구조 (30-35분):
  1. Naive 시도 (7분) — 37MB 업로드, 난이도별 질문 3개 (쉬움/중간/어려움)
  2. 중간 산출물 추출 (10분) — Claude Code / 웹 / 백업 3옵션
  3. 추출본에 같은 질문 재질의 (8분) — 비교표
  4. 재사용성 증명 (8분) — 같은 추출본으로 다른 질문 N개
- **Counterfactual 반영**: "Naive는 나쁘다" → "Naive는 1회 소비용, Harness는 자산화"
- `hands_on/sample_data/ai_index/` 생성 — 원본 PDF + `ai_index_extracted_backup.md` (13KB 큐레이션 추출본)

### Track A 압축 (45→20-25분)
- Step 1에 **"CLAUDE.md 파일로 저장"** 단계 명시 추가 (기존 구멍)
- Windows 메모장 / macOS 텍스트편집기 / VS Code 저장 가이드 분리
- Step 3(이식성 테스트), Step 5(AGENTS.md)를 심화로 이동

### Track C 재구성 — 강사 데모 스크립트 + 홈스터디
- **Part A**: 강사용 12-15분 데모 스크립트 (Scene 1-5, 사전 준비 체크리스트, 문제 발생 대응표)
- **Part B**: 홈스터디 가이드 (Step 1-5, Windows/macOS 2-블록)

### Windows 호환성 전면 보강
- **SETUP.md 신설 섹션**:
  - Section 0: 리포 받기 (ZIP 다운로드 / GitHub Desktop / git CLI 3-옵션)
  - 전날 밤 10분 체크리스트
  - 로그인 사전 확인 가이드 (OAuth callback, 한국 가입 이슈 포함)
- **모든 bash 명령 2-블록화**: macOS/Linux + Windows (PowerShell) 분리
  - `mkdir -p ~/` → `New-Item -ItemType Directory -Path "$HOME\..." -Force`
  - `$(cat ...)` 위험 → `cat file | cmd` (또는 `Get-Content file | cmd`) 파이프 방식
  - `cp` → `Copy-Item`
- `.ps1` 실행 권한 안내 (`Set-ExecutionPolicy RemoteSigned`)

### Streamlit 앱 README 정합성
- `qwen2.5:14b` → `deepseek-r1:14b` (SETUP.md와 통일)
- **venv 권장 섹션** 추가 (macOS/Windows 분리)
- Ollama 서버 실행 케이스 OS별 구분 (Windows 자동 실행 명시)
- 트러블슈팅에 `pip not found`, `.ps1 권한`, 첫 호출 시간 추가

### 파일 배치
- `hands_on/sample_data/ai_index/` 신규 — AI Index PDF + 백업 추출본 + README
- 기존 `sample_01~10.txt`는 "심화 자습용"으로 재포지셔닝
- README.md 폴더 안내 업데이트 (A+B 필수 / C 데모 구조 반영)

### Seamless/airtight 실습을 위한 보강 자료 3종 신규
모든 트랙을 **외부 도움 없이 완주**할 수 있도록, 실제 응답·터미널 화면·기대 출력을 수록한 참조 문서 추가:

- **Track A**: `templates/CLAUDE.md.filled_example` — 가상 석사생 김연구의 완성된 CLAUDE.md (적정 밀도 예시) + `templates/A_vs_B_response_examples.md` — 같은 프롬프트의 A 세션 vs B 세션 실제 응답 + 판정 체크리스트
- **Track B**: `sample_data/ai_index/naive_vs_harness_examples.md` — 질문 A/B/C 각각의 Naive 응답 vs Harness 응답 side-by-side (환각 패턴 포함) + 재사용 질문 3개의 예상 응답 구조
- **Track C**: `prompts_v2/track_c_홈스터디_완주예시.md` — Part 1-5 각 단계의 실제 터미널 화면, 기대 출력, 자주 막히는 지점(OS별 대응표). "본문이 무엇을 하라면, 예시는 어떻게 보일 것인가"

각 Track 본문에서 해당 참조 문서로 링크 연결. 학생이 혼자 결과를 대조하고 문제 지점을 식별할 수 있도록 설계.

---

## 남은 작업

### 슬라이드 수정 (사용자 직접)
- [ ] **Slide 28** 재구성 — "3 트랙 선택" → "A+B 전원 + C는 홈스터디"
  - 2등분 카드: Track A (20-25분) | Track B (30-35분)
  - 하단 박스: Track C는 Part 2 데모 + 홈스터디 가이드
- [ ] Part 2 사례 3 슬라이드 (22-26 근방) — 라이브 데모 12-15분 시간 배정 표시
- [ ] Part 2 / 어젠다 — Part 3 시간 "A(20-25분) + B(30-35분)"로 갱신

### 커밋 (사용자가 파일 선택)
커밋 대기 중 파일 (.gitignore 반영 완료):
- 수정: `.gitignore`, `PROGRESS.md`, `README.md`, `appendix/01·02·references`, `demo/streamlit_research_team/README.md`, `hands_on/SETUP.md`, Track A/B/C 본문
- 삭제: `hands_on/prompts/` v1 4개 (archive로 이동)
- 신규: `appendix/03_NTIS_차별성검토_가이드.md`, `hands_on/prompts_archive/`, `hands_on/prompts_v2/track_c_홈스터디_완주예시.md`, `hands_on/references/`, `hands_on/sample_data/` (ai_index/ + sample_01~10), `hands_on/templates/A_vs_B_response_examples.md`, `hands_on/templates/CLAUDE.md.filled_example`, `slides/`

---

## 📍 2026-04-18 End-of-Day 상태

**오늘 완료한 것 (크게 3 덩어리)**:

1. **워크숍 구조 재설계** (A+B 전원 / C 데모)
   - 3 트랙 선택식 → 리스크 분산 재배치
   - Track A (20-25분 압축), Track B (AI Index 기반 Naive vs Harness 전면 재작성), Track C (실습 → 강사 데모 스크립트 + 홈스터디)

2. **Windows 호환성 전면 보강**
   - 모든 bash 명령 macOS/Linux + Windows (PowerShell) 2-블록
   - SETUP.md에 리포 받기 섹션 신설 (ZIP / GitHub Desktop / git CLI)
   - 로그인 사전 확인·OAuth callback·한국 가입 이슈 문서화

3. **Seamless/airtight 보강 — 실제 응답 예시 3종**
   - `naive_vs_harness_examples.md` (Track B 실제 비교)
   - `CLAUDE.md.filled_example` + `A_vs_B_response_examples.md` (Track A 기준점)
   - `track_c_홈스터디_완주예시.md` (Track C 외부 도움 없이 완주 가능)

**파일 시스템 상태**: 전부 저장됨. 커밋은 사용자 판단으로 선택. `.gitignore`에 `Vibe_Researching_Workshop (1).pptx`, `Yonsei/` 추가 완료.

**다음 세션 복귀 시**:
1. 슬라이드 3건 수정 (위 "남은 작업")
2. 커밋 파일 선택 및 커밋
3. 당일 전 최종 드라이런 (Track A·B 실제 돌려보기)

---

## 핵심 발견

### 4모델 교차검증 = 반증가능성
- 4개 계열 모델이 각각 공격 → 모델마다 다른 문제를 잡음
- 3/4 공통 지적: "사회문제에 기술적 해결책 과도 적용"
- 크기 ≠ 품질: Gemma4 E4B(4B)가 DeepSeek R1(14B)보다 깊은 비판

### 나만의 연구팀 = Harness Engineering 시각적 증명
- 법무팀 Streamlit 앱에서 프롬프트만 바꿔 연구팀으로 변환
- 파이프라인(입력→작성→검증→총괄→출력) 100% 동일
- Ollama 모델 자동감지 → plug & play

### 비용 구조
- 검증 = 로컬 $0, 무한 반복
- 판단 = $20 Pro면 충분
- $0→$20 점프가 가장 큰 품질 향상
