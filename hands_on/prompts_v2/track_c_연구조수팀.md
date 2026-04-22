# Track C — 연구 조수 팀 (강사 데모 + 홈스터디)

**변경 안내 (2026-04-18)**: Part 3 실습은 Track A + B로 단일화되었습니다. Track C는 **Part 2의 라이브 데모**(강사 시연 10-15분) + **홈스터디 가이드**(본인이 집에서 재현) 두 가지로 재구성됩니다.

**왜 바뀌었나**: 로컬 모델 설치·터미널 셸·운영체제 편차가 45분 안에 전원 성공을 보장하기 어려움. 데모로 보여주고, 리포로 가져가서 집에서 하는 편이 학습 효과·성공률 모두 더 높다는 판단.

---

## 이 문서의 두 부분

1. **Part A — 강사 데모 스크립트** (Part 2 "사례 3" 자리, 약 12-15분): 강사가 시연할 때 참고하는 스크립트
2. **Part B — 홈스터디 가이드**: 학생이 워크숍 이후 본인 환경에서 동일한 흐름을 재현할 수 있도록 하는 단계별 안내

---

# Part A — 강사 데모 스크립트 (12-15분)

## 데모 목적

"**같은 하네스, 다른 프롬프트**"를 눈으로 보여준다. Track A (맥락 문서) + Track B (중간 산출물)가 **여러 에이전트가 협업하는 구조**로 확장되는 지점을 시각적으로 증명.

### 전하려는 3가지 메시지

1. **Claude Code가 CLAUDE.md를 자동 로드**한다 — Track A에서 만든 파일이 바로 쓰인다
2. **같은 파이프라인 코드가 도메인만 바꿔 재사용된다** — 법무팀 Streamlit 앱 → 연구팀 (프롬프트만 교체)
3. **여러 모델이 교차검증하면 한 모델이 놓친 문제가 드러난다** — 4모델 실제 실험 결과

---

## 사전 준비 (데모 시작 10분 전)

- [ ] Claude Code 실행 상태, 시연용 `~/workshop_demo/` 폴더 + CLAUDE.md 준비
- [ ] Streamlit 앱 실행 상태: `cd demo/streamlit_research_team && streamlit run app.py`
  → 브라우저에 http://localhost:8501 띄워둠
- [ ] Ollama `gemma4` 모델 **미리 로드** (`ollama run gemma4 "hi"` 한 번 실행 → 메모리 점유)
- [ ] `hands_on/scenario_comparison/scenario_b/05_cross_validation_4models.md` 탭에서 열어둠
- [ ] 법무팀 앱 스크린샷 (비교용 1컷) 준비 — 슬라이드에 이미 포함되어 있으면 그걸로 OK

---

## 스크립트

### 🎬 Scene 1 — 연결 (1분)

> "여러분은 방금 Track B에서 AI Index PDF를 마크다운으로 추출했죠. 그 추출본이 하나의 **중간 산출물**, 즉 자산입니다. 그런데 이 자산을 여러 모델이 각자 공격하면 어떻게 될까요? 이게 Track C — **연구 조수 팀**입니다."

[Part 2 슬라이드에서 사례 3 (연구 팀 만들기) 표시]

### 🎬 Scene 2 — Claude Code + CLAUDE.md 자동 로드 (2-3분)

터미널 전환 → Claude Code 실행:

```bash
cd ~/workshop_demo
claude
```

화면에서 `CLAUDE.md loaded` 메시지 보여주며:

> "보시다시피 `CLAUDE.md` 파일이 자동으로 로드됐습니다. Track A에서 만든 그 파일이에요. 이 프로젝트에 들어오는 모든 대화가 이 문서를 기본 맥락으로 씁니다."

간단한 질문 1개 시연:
```
내 분야에서 2026년 기준 유망한 석사 논문 주제 3개를 제안해줘.
각각 시의성 한 줄 + 예상 방법론. output/topics.md 에 저장.
```

결과가 파일로 저장되는 것 보여줌 (30초 기다리기).

> "지금 이 과정은 CLI에서 일어났습니다. 하지만 연구실에서 쓸 때 CLI가 부담스러우면?"

### 🎬 Scene 3 — Streamlit 앱 전환 (하이라이트, 5분)

브라우저 탭으로 전환 → 이미 띄워둔 Streamlit 앱.

> "이건 제가 만든 '나만의 연구팀' 앱입니다. **원본은 유튜브에서 본 '나만의 로컬 법무팀' 앱**이고요 — Sam(초고 작성) → Jenny(검토) → Will(최종 QA)이라는 3-agent 파이프라인. 저는 **시스템 프롬프트만 3개 바꿔서** 연구팀으로 만들었어요: 수연(탐색) → 준호(검증) → 지은(총괄)."

[슬라이드 또는 화면 분할로 법무팀 vs 연구팀 비교 1컷 보여주면 극적]

> "바꾼 것과 안 바꾼 것을 보세요."

| 바꾼 것 | 안 바꾼 것 |
|---|---|
| 시스템 프롬프트 (에이전트 역할) | 파이프라인 구조 (순차 실행) |
| 출력 템플릿 (법률 메모 → 연구 설계) | Ollama + Streamlit 기반 |
| UI 라벨 | 코드 거의 그대로 |

> "이게 **harness engineering**의 핵심입니다. 하네스(실행 구조)는 유지하고, 프롬프트만 교체."

**실제 시연** (3분):
1. 앱에서 분야 선택 (예: "식품영양") + 키워드 (예: "독거노인 영양")
2. "연구팀 실행" 클릭
3. 수연(탐색) 단계 진행되는 것 보여주기 — 스트리밍 출력
4. 준호(검증) 단계 — "기존 주장에 동의하지 마세요" 프롬프트가 어떻게 작동하는지
5. 지은(총괄) 단계 — 최종 연구 설계 요약

> "지금 돌아간 모델은 노트북에 설치한 Gemma 4 E4B (4B 파라미터)입니다. 인터넷 없어도 되고, 비용 0원이고, 민감 자료도 밖으로 안 나갑니다."

### 🎬 Scene 4 — 4모델 교차검증 (2-3분)

`scenario_b/05_cross_validation_4models.md` 파일 또는 슬라이드 23으로 전환.

> "에이전트 하나만으로는 부족할 수 있어요. 그래서 같은 연구 설계를 **4개 계열 모델**(DeepSeek R1, Gemma 4, Codex, Gemini)에 각각 공격시켜봤어요."

핵심 표 보여주기:

| 지적 사항 | DeepSeek | Gemma4 | Codex | Gemini |
|---|---|---|---|---|
| 사회문제에 기술적 해결책 과도 적용 | ✅ | ✅ | ✅ | — |
| 선택편향 | — | — | — | ✅ |
| 개념 중복 | — | — | ✅ | — |
| Gap 모호 | ✅ | — | — | — |

> "세 가지 관찰 포인트:
> 1. **모델마다 다른 걸 잡는다** — 하나만 썼으면 놓쳤을 문제가 4개를 합치면 거의 다 드러남
> 2. **3개 이상이 공통 지적한 게 가장 신뢰할 만하다** — '사회문제에 기술적 해결책 과도 적용' = 진짜 약점
> 3. **크기 ≠ 품질** — Gemma 4 E4B(4B)가 DeepSeek R1(14B)보다 더 깊은 개념적 비판을 했어요

> Popper의 반증가능성 원칙을 AI 연구 파이프라인에 내장한 거죠."

### 🎬 Scene 5 — 마무리 + 홈스터디 안내 (1-2분)

> "오늘 실습에서는 Track A, B까지 했어요. 이 Track C는 **집에서 해보는 것**을 추천합니다. 이유:
> - 로컬 모델 설치는 노트북 사양·네트워크 편차가 커서 시간 보장이 어렵다
> - 여러분이 혼자 차분히 할 때 성공률이 훨씬 높다
> - 그래서 대신 **이 시연**으로 전체 구조를 보여드린 거예요

> 리포지토리 `hands_on/prompts_v2/track_c_연구조수팀.md` 의 **Part B — 홈스터디 가이드**를 따라가면 오늘 본 시연과 동일한 3-agent 구조를 Claude Code + Ollama 로 직접 만들 수 있습니다. Streamlit 앱은 강사 시연 전용으로 repo 에 포함되지 않지만, 개념은 프롬프트만 바꿔서 여러분 분야로 재설계 가능합니다."

[슬라이드로 돌아가며 다음 섹션(실습 안내)으로 전환]

---

## 🚨 데모 중 문제 발생 시 대응

| 상황 | 대응 |
|---|---|
| Streamlit 앱이 멈춤 | 페이지 새로고침. 그래도 안 되면 미리 준비한 **스크린 녹화 1분 클립**으로 전환 |
| Ollama 첫 로딩이 길어짐 | "첫 호출은 모델을 RAM에 올리는 시간입니다. 정상입니다" 멘트 + 그 사이 4모델 교차검증 표 설명으로 전환 |
| Claude Code 네트워크 문제 | CLI 시연 스킵, Streamlit 앱으로 바로 이동 |
| 프로젝터 텍스트가 작게 보임 | 미리 zoom 레벨을 150%로 설정해둘 것 |

---

# Part B — 홈스터디 가이드

> 워크숍에서 본 데모를 **본인 환경에서 재현**하는 가이드. 혼자 차분히 따라 하면 1시간 이내 가능. Windows / macOS 모두 지원.
>
> **📎 외부 도움 없이 완주하려면**: 각 단계의 **실제 터미널 화면 · 기대 출력 · 자주 막히는 지점**을 수록한 **완주 예시 문서**를 나란히 참고하세요 → [`track_c_홈스터디_완주예시.md`](./track_c_홈스터디_완주예시.md)
>
> 이 문서(Part B)는 "무엇을 해야 하는가", 완주 예시는 "어떻게 보일 것이며 안 보이면 뭘 해야 하는가". 두 개를 함께 펴놓고 진행하면 막혀서 중단하는 일이 거의 없습니다.

## 목표

1. Claude Code 설치 + CLAUDE.md 자동 로드 체험
2. Ollama + Gemma 4 로컬 모델로 교차검증 체험
3. Streamlit "나만의 연구팀" 앱을 본인 컴퓨터에서 실행

## 사전 조건

- 본인 노트북 (macOS 또는 Windows, RAM **최소 8GB, 권장 16GB 이상**)
- 인터넷 연결 (모델 다운로드 시 약 3-10 GB)
- Node.js 18 이상, Python 3.9 이상 (아래에서 확인)

---

## 🏠 Step 1 — Claude Code 설치

### 1-1. Node.js 확인

**macOS Terminal / Windows PowerShell 공통**:
```bash
node --version
```
→ `v18` 이상이면 OK. 안 나오면 설치:

| OS | 설치 |
|---|---|
| macOS | `brew install node` 또는 https://nodejs.org 에서 LTS 다운로드 |
| Windows | `winget install OpenJS.NodeJS.LTS` 또는 https://nodejs.org |

### 1-2. Claude Code 설치

**공통**:
```bash
npm install -g @anthropic-ai/claude-code
claude --version
```

버전 번호 나오면 OK.

### 1-3. 첫 실행 (OAuth 로그인)

```bash
claude
```
브라우저가 자동으로 열립니다 → Anthropic 계정으로 로그인 (Pro $20/월 또는 무료 체험). 인증 후 터미널로 돌아옵니다.

> **Windows PowerShell에서 명령이 안 먹힘**: `npm`이 PATH에 없으면 설치 시 "Add to PATH" 체크가 빠진 것. Node.js installer 재실행하거나 `$env:PATH` 확인.

---

## 🏠 Step 2 — Ollama 설치 + 모델 다운로드

### 2-1. Ollama 설치

| OS | 설치 |
|---|---|
| macOS | `brew install ollama` 또는 https://ollama.com |
| Windows | https://ollama.com installer → 실행 (설치 후 자동 백그라운드 실행) |
| Linux | `curl -fsSL https://ollama.com/install.sh \| sh` |

**확인**:
```bash
ollama --version
```

### 2-2. 모델 다운로드

**RAM 기준 추천**:

| RAM | 권장 모델 | 다운로드 |
|---|---|---|
| 8 GB | `gemma4` 만 | `ollama pull gemma4` (약 3 GB) |
| 16 GB | `gemma4` + 검증용 | `ollama pull gemma4` + `ollama pull phi4-mini` |
| 32 GB+ | 교차검증 풀 구성 | `ollama pull gemma4 && ollama pull deepseek-r1:14b` |

```bash
ollama list
```
→ 다운받은 모델 목록 확인.

> **시간 예상**: 3GB 모델은 100 Mbps wifi에서 약 5분, 9GB는 약 15분. 당일 다운로드는 피하고 전날 미리 받아두세요.
> **Windows**: Ollama installer 설치 후 자동으로 백그라운드 실행됩니다 (`ollama serve` 별도 불필요).
> **macOS Homebrew**: 설치 후 `brew services start ollama` 또는 `ollama serve` (별도 터미널) 필요.

---

## 🏠 Step 3 — 연구 파이프라인 1회 실행 (CLI)

### 3-1. 프로젝트 폴더 준비

**macOS / Linux**:
```bash
mkdir -p ~/workshop_team_demo/output
cd ~/workshop_team_demo
```

**Windows (PowerShell)**:
```powershell
New-Item -ItemType Directory -Path "$HOME\workshop_team_demo\output" -Force
cd "$HOME\workshop_team_demo"
```

### 3-2. CLAUDE.md 배치

Track A에서 만든 CLAUDE.md를 이 폴더로 복사하세요. 또는 아래 기본 버전 사용:

```markdown
# 프로젝트 맥락 문서

## 연구 분야
[본인 분야 — 식품영양 / 노화과학 / 섬유패션 / 주거복지 / 디자인 등]

## 현재 단계
주제 탐색

## 출력 규칙
- 문체: 학술체 (~이다)
- 인용: APA 7th
- 언어: 한국어
- 확인 안 된 논문은 "확인 필요" 표기

## 금기
- 존재하지 않는 논문을 만들지 말 것
- 추측으로 연구 갭을 만들지 말 것
```

### 3-3. Claude Code 실행 + 3단계 파이프라인

```bash
claude
```

Claude Code 세션 안에서:
```
아래 순서대로 진행해줘:

1. 내 분야에서 2026년 현재 석사 논문 주제 3개 제안.
   각각 제목 + 시의성 한 줄 + 예상 방법론.
   output/01_topics.md 에 저장.

2. 가장 실현 가능한 주제 1개를 골라 선행연구 5건 정리.
   각 논문: 저자, 연도, 핵심 발견, 출처 URL.
   확인 안 되면 "확인 필요".
   output/02_literature.md 에 저장.

3. 연구 갭 2개 도출 + Research Question 제안.
   output/03_research_questions.md 에 저장.
```

진행 중 `Allow?` 권한 요청이 나오면 `y` 입력.

---

## 🏠 Step 4 — 교차검증 (핵심)

같은 결과를 **다른 모델**에게 공격시킵니다.

### 4-1. Claude Code 안에서 로컬 Gemma 4로 검증

**macOS / Linux**:
```
bash로 아래 명령 실행해줘:

cat output/03_research_questions.md | ollama run gemma4 "위 연구 설계의 논리적 문제를 찾아줘.
기존 주장에 동의하지 말고, 틀린 점을 적극적으로 찾아줘.
의심스러운 부분은 '검증 실패: [이유]'로 표시."

결과를 output/04_verification_gemma4.md 에 저장.
```

**Windows (PowerShell)**:
```
bash로 아래 명령 실행해줘:

Get-Content output/03_research_questions.md | ollama run gemma4 "위 연구 설계의 논리적 문제를 찾아줘.
기존 주장에 동의하지 말고, 틀린 점을 적극적으로 찾아줘.
의심스러운 부분은 '검증 실패: [이유]'로 표시."

결과를 output/04_verification_gemma4.md 에 저장.
```

> **왜 파이프(`|`) 방식?** 파일 내용에 따옴표가 섞여 있을 때 `$(cat ...)` 치환은 셸에서 깨질 수 있습니다. 파이프는 안전.

### 4-2. (선택) Codex / Gemini CLI로 추가 검증

```bash
npm install -g @openai/codex @google/gemini-cli
codex --version
gemini --version
```

Codex는 ChatGPT Plus 구독 기반, Gemini CLI는 무료 (Google 계정).

Claude Code 안에서:
```
cat output/03_research_questions.md | codex exec "위 연구 설계의 문제점을 찾아줘..."
cat output/03_research_questions.md | gemini "위 연구 설계의 문제점을 찾아줘..."
```

### 4-3. 비교

```
output/ 의 04_verification_*.md 파일들을 모두 읽고,
모든 검증 모델이 공통 지적한 항목을 표로 정리해줘.
컬럼: 지적사항 | Gemma4 | Codex | Gemini.
```

**이게 반증가능성의 구조적 증명**: 3개 이상 공통 지적 = 실제 약점.

---

## 🏠 체크포인트 (홈스터디 완료 기준)

- [ ] Claude Code가 본인 CLAUDE.md를 자동 로드함
- [ ] 3단계 연구 파이프라인이 파일로 저장됨 (output/01~03)
- [ ] 최소 1개 모델로 교차검증 실행 완료 (04_verification_*.md)
- [ ] "왜 여러 모델이 필요한가"를 본인 말로 설명 가능

---

## 함정 피하기

- **검증 없이 결과를 그냥 쓰지 마세요.** AI가 빠르게 내놓으니 그냥 받고 싶지만, 그게 "검증부채(Verification Debt)"입니다.
- **로컬 모델 첫 호출은 1-3분 걸립니다 (저사양은 5-10분)** — 모델을 메모리에 올리는 시간. 두 번째부터 빠름.
- **로컬 모델의 한국어가 어색해도 괜찮습니다.** 글쓰기가 아니라 검증이 목적. "이상한 점을 찾아라"는 지시에는 작은 모델도 유효.
- **4B 모델이 14B보다 나을 때도 있습니다.** 크기 ≠ 품질. 실험에서 Gemma 4 E4B(4B)가 DeepSeek R1(14B)보다 더 깊은 개념적 비판을 제공했습니다.
- **검증 프롬프트에 "동의하지 말고 공격하라"를 넣으세요.** 안 넣으면 AI가 칭찬만 합니다.

---

## 비용 구조 요약

| 역할 | 도구 | 비용 | 비고 |
|---|---|---|---|
| Writer (작성) | Claude Pro | $20/월 | 웹검색, 긴 맥락, 도구 호출 |
| Verifier 1 | Ollama + Gemma4 | **$0** | 로컬, 무한 반복 가능 |
| Verifier 2 | Codex CLI | ChatGPT Plus 포함 | 이미 구독 중이면 추가 비용 없음 |
| Verifier 3 | Gemini CLI | **무료** | Google 계정만 있으면 됨 |

**$0 → $20 점프가 가장 큰 품질 향상.** 웹검색이 가능해지면 연구 생산성이 확 바뀝니다.

Tier별 상세: `hands_on/ra_team_tiers.md`

---

## 참고 자료

- **🎯 완주 예시 (이 문서와 나란히 보기)**: `hands_on/prompts_v2/track_c_홈스터디_완주예시.md`
- 로컬 모델 세팅 상세: `hands_on/ra_team_setup.md`
- Tier별 구성: `hands_on/ra_team_tiers.md`
- 강사 환경 레퍼런스 (M4 32GB): `hands_on/reference_setup_m4_32gb.md`
- 4모델 교차검증 실제 결과: `hands_on/scenario_comparison/scenario_b/`
- 로컬 AI 무료 가이드: `appendix/01_로컬AI_무료_활용_가이드.md`
- 강사 라이브 데모의 Streamlit 앱은 repo 비공개. 같은 3-agent 구조를 Claude Code + Ollama 로 재현하는 것이 이 홈스터디 가이드의 전부.

---

*작성: 2026-04-15 | 구조 재설계: 2026-04-18 | CC BY-NC-SA 4.0*
