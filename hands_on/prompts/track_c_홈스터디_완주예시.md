# Track C 홈스터디 — 완주 예시

> **📌 2026-04-23 업데이트**: 본 문서 후반부(Part 5 전후)의 Streamlit 앱은 현재 두 가지 공개 버전으로 제공됩니다:
> - **`demo/streamlit_research_team_lite/`** — 16GB 노트북 대상 경량 버전 (`gemma4:e4b` 단일 모델 × 3 역할). **집에서 바로 재현 가능**.
> - **`hands_on/claude_code_agents/`** — Claude Code 를 이미 쓰는 분용. 같은 프롬프트 9개를 `.claude/agents/` 네이티브 형식으로 이관.
>
> 따라서 **Part 1-4 (Claude Code + Ollama 기본 세팅) 또는 Streamlit Lite (Python + Ollama 만) 중 하나만 따라가도 동일한 3-agent 연구팀 파이프라인을 재현** 할 수 있습니다. Part 5 의 "풀 버전 Streamlit" 은 참고용으로만 남아있으나, 실제 재현은 Lite 변형 쪽을 권장합니다.

**목적**: Track C 홈스터디를 **아무 외부 도움 없이** 혼자 끝까지 따라갈 수 있도록, 각 단계에서 **터미널에 실제로 보일 화면**과 **생성될 결과물**, **자주 막히는 지점**을 모두 수록한 문서.

**읽는 법**: Track C 본문(`track_c_연구조수팀.md` Part B)과 **나란히** 놓고 보세요. 본문이 "무엇을 하라"면, 이 문서는 "어떻게 보일 것이고 무엇이 저장될 것인가".

**환경 가정**: 가상의 석사생 "김연구" — MacBook Air M2 16GB 또는 삼성 갤럭시북 16GB (Windows 11). Node.js·Python 미설치 상태에서 시작. 본문 각 단계에서 **macOS Terminal / Windows PowerShell 두 경로를 병기**합니다.

---

## Part 1 — Node.js & Claude Code 설치 완주

### Step 1. Node.js 확인

**입력** (macOS Terminal 또는 Windows PowerShell):
```bash
node --version
```

**가능한 결과 A — 이미 설치됨**:
```
v20.11.0
```
→ v18 이상이면 다음 단계로. 끝.

**가능한 결과 B — 명령을 찾을 수 없음**:
```
zsh: command not found: node          # macOS
```
```
node : 'node' 용어가 cmdlet, 함수, 스크립트 파일 또는 실행할 수 있는
프로그램 이름으로 인식되지 않습니다.     # Windows PowerShell
```
→ Node.js 미설치. 아래로 진행.

### Step 1-2. Node.js 설치

**macOS (Homebrew 사용)**:
```bash
brew install node
```
설치 진행 중 화면(발췌):
```
==> Downloading https://ghcr.io/v2/homebrew/core/node/manifests/20.11.0
==> Fetching node
==> Downloading https://ghcr.io/v2/homebrew/core/node/blobs/...
==> Pouring node--20.11.0.sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/node/20.11.0: 2,345 files, 78.3MB
```
3-5분 소요. 설치 완료 후:
```bash
node --version
# v20.11.0
npm --version
# 10.2.4
```

**Windows (winget 사용, PowerShell 관리자 권한)**:
```powershell
winget install OpenJS.NodeJS.LTS
```
화면:
```
Found Node.js LTS [OpenJS.NodeJS.LTS] Version 20.11.0
This application is licensed to you by its owner.
Successfully verified installer hash
Starting package install...
Successfully installed
```
→ **PowerShell 창을 완전히 닫고 새로 열어야** `node` 명령이 인식됩니다. 재시작 후:
```powershell
node --version
# v20.11.0
```

### Step 1-3. Claude Code 설치

```bash
npm install -g @anthropic-ai/claude-code
```

**진행 화면**:
```
npm warn deprecated inflight@1.0.6: This module is not supported...
added 234 packages in 18s
```
(경고 메시지는 무시해도 됩니다. 중요한 건 `added ... packages`)

**확인**:
```bash
claude --version
```
```
1.0.33 (Claude Code)
```
숫자는 버전에 따라 다를 수 있음. 비슷한 형식이면 OK.

### Step 1-4. 첫 실행 — OAuth 로그인

```bash
claude
```

**터미널 화면**:
```
Welcome to Claude Code!

Please authenticate to continue.
Press Enter to open your browser for login...
```

Enter 누르면 기본 브라우저가 자동으로 열림 → `https://console.anthropic.com/oauth/...` 같은 URL로 리다이렉트 → Anthropic 계정 로그인 → "Authorize" 버튼 클릭 → "You can now close this window" 메시지.

터미널로 돌아오면:
```
✓ Authentication successful
Starting Claude Code in /Users/your_name/current_directory
claude > 
```

이 `claude > ` 프롬프트가 나오면 **설치 완료**. `exit` 또는 `Ctrl+D`로 나옴.

### 💥 이 단계에서 자주 막히는 곳

| 증상 | 원인 | 해결 |
|---|---|---|
| `npm: command not found` | Node.js 설치 시 npm 누락 또는 PATH 문제 | Windows: installer 재실행 + "Add to PATH" 체크. Mac: `brew reinstall node` |
| 브라우저가 안 열림 | 기본 브라우저 설정 문제 | 터미널에 표시된 URL을 복사해서 직접 브라우저 주소창에 붙여넣기 |
| 로그인 후 터미널이 안 돌아옴 | localhost callback 차단 (특히 캠퍼스 wifi) | 모바일 핫스팟으로 연결 후 재시도 |
| "Authentication failed" | 브라우저 창을 너무 빨리 닫음 | 다시 `claude` 실행 후 "authorized" 메시지까지 기다리기 |

---

## Part 2 — Ollama & 모델 다운로드 완주

### Step 2-1. Ollama 설치

**macOS**:
```bash
brew install ollama
```
또는 https://ollama.com 에서 `Ollama-darwin.zip` 다운로드 → 압축 해제 → `Ollama.app`을 Applications 폴더로.

**Windows**:
https://ollama.com 에서 `OllamaSetup.exe` 다운로드 → 실행 → "Install" 클릭. 설치 후 시스템 트레이에 **라마 아이콘**이 생김 (백그라운드에서 자동 실행).

**확인**:
```bash
ollama --version
```
```
ollama version 0.5.7
```
(숫자는 다를 수 있음)

### Step 2-2. Ollama 서버 실행

**macOS (Homebrew 설치)**:
```bash
ollama serve
```
화면:
```
time=2026-04-18T20:45:00.000+09:00 level=INFO source=images.go:432 msg="total blobs: 0"
time=2026-04-18T20:45:00.000+09:00 level=INFO source=images.go:439 msg="total unused blobs removed: 0"
time=2026-04-18T20:45:00.000+09:00 level=INFO source=routes.go:1289 msg="Listening on 127.0.0.1:11434 (version 0.5.7)"
```
→ **이 터미널 창은 계속 띄워둬야 합니다** (Ctrl+C 금지). 다른 명령은 **새 터미널 창**에서 실행.

**대안 — 백그라운드 실행 (macOS)**:
```bash
brew services start ollama
```
→ 시스템 종료까지 백그라운드로 돌아감. `brew services stop ollama`로 중지.

**Windows**: installer가 자동으로 백그라운드 서비스로 실행. **별도 명령 불필요.**

**동작 확인** (새 터미널 창):
```bash
ollama list
```
아직 모델이 없으면:
```
NAME    ID    SIZE    MODIFIED
```
(비어있음, OK)

### Step 2-3. Gemma 4 다운로드

```bash
ollama pull gemma4
```
진행 화면 (예):
```
pulling manifest
pulling 6a0746a1ec1a... 100% ▕████████████████▏ 3.1 GB
pulling 097a36493f71... 100% ▕████████████████▏ 8.4 KB
pulling 109037bec39c... 100% ▕████████████████▏  136 B
pulling 22a838ceb7fb... 100% ▕████████████████▏   84 B
pulling 0b5c8e4f0c9e... 100% ▕████████████████▏  487 B
verifying sha256 digest
writing manifest
success
```

**예상 시간**: 100 Mbps wifi 기준 약 5분. 50 Mbps면 10분. 다운로드 중단되어도 재실행하면 이어받기.

**확인**:
```bash
ollama list
```
```
NAME            ID              SIZE      MODIFIED
gemma4:latest   abc123def456    3.1 GB    1 minute ago
```

### Step 2-4. 모델 첫 호출 (메모리 로드 확인)

```bash
ollama run gemma4 "안녕"
```
**첫 응답까지 1-3분 소요** (M2 Mac) 또는 **3-10분** (내장 GPU Windows). 로딩 중 화면은 무반응처럼 보일 수 있음 — **정상**입니다.

응답 예:
```
안녕하세요! 어떻게 도와드릴까요? 한국어로 대화하실 수 있어요.
>>> Send a message (/? for help)
```

`/bye` 입력으로 종료. 두 번째 호출부터는 수초 이내 응답 (모델이 메모리에 남아있음).

### 💥 Part 2 자주 막히는 곳

| 증상 | 원인 | 해결 |
|---|---|---|
| `Error: could not connect to ollama app` | 서버 미실행 | `ollama serve` (별도 터미널) 또는 Windows는 시스템 트레이의 라마 아이콘 확인 |
| 다운로드가 중간에 멈춤 | 네트워크 끊김 | `ollama pull gemma4` 재실행 — 이어받기 됨 |
| "no available memory" | RAM 부족 | 브라우저 탭 최대한 닫고 재시도. 8GB 머신에서 Gemma 4 borderline |
| 첫 응답이 10분 넘게 안 옴 | CPU 추론 (GPU 가속 없음) | 정상. 기다리거나 더 작은 모델로 교체 (`ollama pull qwen2.5:3b`) |
| 한국어 응답이 깨짐 | 1B급 모델 사용 중 | `gemma4` (4B, E4B)는 한국어 OK. 더 작은 모델은 불안정 |

---

## Part 3 — 연구 파이프라인 1회 실행 완주

### Step 3-1. 프로젝트 폴더 준비

**macOS / Linux**:
```bash
mkdir -p ~/workshop_team_demo/output
cd ~/workshop_team_demo
pwd
# /Users/your_name/workshop_team_demo
```

**Windows (PowerShell)**:
```powershell
New-Item -ItemType Directory -Path "$HOME\workshop_team_demo\output" -Force
cd "$HOME\workshop_team_demo"
pwd
# Path
# ----
# C:\Users\your_name\workshop_team_demo
```

### Step 3-2. CLAUDE.md 배치

Track A에서 만든 파일을 복사하거나, 없다면 아래 내용으로 새로 생성:

**macOS / Linux** (heredoc):
```bash
cat > CLAUDE.md << 'EOF'
# 프로젝트 맥락 문서

## 연구 분야
식품영양학 (본인 분야로 교체)

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
EOF
```

**Windows (PowerShell)**:
```powershell
@"
# 프로젝트 맥락 문서

## 연구 분야
식품영양학 (본인 분야로 교체)

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
"@ | Out-File -FilePath CLAUDE.md -Encoding UTF8
```

**확인**:
```bash
ls              # macOS/Linux
dir             # Windows cmd
Get-ChildItem   # Windows PowerShell
```
→ `CLAUDE.md`가 목록에 보이면 OK.

### Step 3-3. Claude Code 실행 + CLAUDE.md 자동 로드 확인

```bash
claude
```

화면:
```
> Welcome! I loaded the following from this directory:
  • CLAUDE.md (350 bytes)

claude > 
```

이 "I loaded CLAUDE.md" 메시지가 **핵심 확인 지점**. 안 뜨면:
- CLAUDE.md가 현재 디렉토리에 있는지 확인 (`ls` / `Get-ChildItem`)
- 파일명 대소문자 확인 (Linux/Mac은 case-sensitive)

### Step 3-4. 3단계 파이프라인 실행

Claude Code 프롬프트(`claude > `)에서 그대로 붙여넣기:

```
아래 순서대로 진행해줘:

1. 내 분야에서 2026년 현재 석사 논문 주제 3개 제안.
   각 주제: 제목 + 시의성 한 줄 + 예상 방법론.
   output/01_topics.md 에 저장.

2. 가장 실현 가능한 주제 1개를 골라 선행연구 5건 정리.
   각 논문: 저자, 연도, 핵심 발견, 출처 URL.
   확인 안 되면 "확인 필요".
   output/02_literature.md 에 저장.

3. 연구 갭 2개 도출 + Research Question 제안.
   output/03_research_questions.md 에 저장.
```

**진행 중 화면** (요약):
```
I'll complete this step by step. Let me start with Step 1.

● Write(output/01_topics.md)
  ⎿  Allow? [y/n/a]
```

→ `y` 입력 (또는 `a` = always allow로 이후 질문 없음).

```
● Write(output/01_topics.md) — 성공
  ⎿  Created output/01_topics.md with 3 topic proposals

Now moving to Step 2: literature review for the most feasible topic.

● WebSearch("독거노인 식단기록 앱 사용성")
  ⎿  Allow? [y/n/a]
```

→ `y`. 웹검색 결과를 바탕으로 02_literature.md 작성.

```
● Write(output/02_literature.md) — 성공
● Write(output/03_research_questions.md) — 성공

All three steps complete. Files saved in output/.
```

총 소요 시간: **3-7분** (웹검색 포함).

### Step 3-5. 결과 확인

```bash
ls output/
# 01_topics.md   02_literature.md   03_research_questions.md
```

```bash
cat output/01_topics.md
```

**예상 출력 (발췌)**:
```markdown
# 2026년 식품영양학 석사 논문 주제 제안 3선

## 주제 1. 독거노인의 디지털 식단기록 앱 사용성과 식이 섭취 정확도
**시의성**: 1인 노인가구 증가와 디지털 헬스 도입 확산의 교차점에서 경험적 근거 부족
**예상 방법론**: 혼합방법 — 24시간 회상법 vs 앱 기록 비교(양적) + 사후 인터뷰(질적)

## 주제 2. 지역아동센터 식단의 영양균형과 아동 미량영양소 섭취
**시의성**: 돌봄 공백 논의 속에서 "끼니 질"이 정책 검토 대상으로 부상
**예상 방법론**: 횡단면 조사 — 2주간 식단 영양소 분석 + 참여 아동 혈중 지표

## 주제 3. (생략)
```

`cat output/02_literature.md`, `cat output/03_research_questions.md` 도 동일하게 확인.

### 💥 Part 3 자주 막히는 곳

| 증상 | 원인 | 해결 |
|---|---|---|
| CLAUDE.md가 로드 안 됨 | 다른 폴더에 있음 | `pwd`로 현재 위치 확인 + CLAUDE.md가 거기 있는지 확인 |
| "Allow?" 매번 물음 | 기본 권한 설정 | `claude > /permissions` 입력 → 자주 쓰는 도구 allowlist 추가 |
| 웹검색이 작동 안 함 | Claude 구독 레벨 | Pro ($20/월)는 웹검색 기본 포함. 무료는 제한 있음 |
| output/ 폴더에 파일이 안 생김 | Claude가 경로 해석 실패 | "현재 디렉토리 기준 output/ 에 저장" 명시적으로 프롬프트 |
| 논문을 만들어냄 (할루시네이션) | 금기 규칙 미적용 | CLAUDE.md에 "확인 안 된 논문은 만들지 말 것" 명시적 금기 추가 |

---

## Part 4 — 교차검증 완주

### Step 4-1. 로컬 Gemma 4로 검증 (Claude Code 내부에서 bash 실행)

Claude Code에 입력:

**macOS / Linux**:
```
bash로 아래 명령 실행해줘:

cat output/03_research_questions.md | ollama run gemma4 "위 연구 설계의 논리적 문제를 찾아줘. 기존 주장에 동의하지 말고, 틀린 점을 적극적으로 찾아줘. 의심스러운 부분은 '검증 실패: [이유]'로 표시."

결과를 output/04_verification_gemma4.md 에 저장.
```

**Windows (PowerShell)**:
```
bash로 아래 명령 실행해줘 (Windows PowerShell 환경):

Get-Content output/03_research_questions.md | ollama run gemma4 "위 연구 설계의 논리적 문제를 찾아줘. 기존 주장에 동의하지 말고, 틀린 점을 적극적으로 찾아줘. 의심스러운 부분은 '검증 실패: [이유]'로 표시."

결과를 output/04_verification_gemma4.md 에 저장.
```

**진행 화면**:
```
● Bash(cat output/03_research_questions.md | ollama run gemma4 "...")
  ⎿  Allow? [y/n/a]
```
→ `y`. 첫 호출은 1-3분 소요.

```
● Write(output/04_verification_gemma4.md) — 성공
```

### Step 4-2. 결과물 확인

```bash
cat output/04_verification_gemma4.md
```

**예상 출력 (발췌 — 실제 내용은 주제에 따라 다름)**:
```markdown
# Gemma 4 검증 결과

## 전체 평가
제시된 연구 설계는 주제의 시의성과 방법론적 적절성 면에서 기본 요건을
충족하지만, 아래 영역에서 논리적 재검토가 필요합니다.

## 검증 실패 항목

1. **검증 실패: 정확도 측정의 준거 타당성 문제**
   24시간 회상법을 "정답"으로 전제하고 앱 기록을 비교하는 구조는,
   회상법 자체의 기억 오류(recall bias)를 무시합니다. 노인에서 기억 오류는
   더 크다는 선행연구가 있는데(Kim & Lee, 2019 등), 이 한계가 전제에서
   다루어지지 않았습니다.

2. **검증 실패: 표본 크기 근거 부재**
   "30-40명"의 표본이 혼합방법에 충분하다는 통계적 근거가 제시되지
   않았습니다. 정확도 비교(양적)에는 부족할 수 있고, 인터뷰 포화
   (qualitative saturation) 관점에서도 명시 필요.

## 문제 없음

- 연구 질문의 구체성과 변수 조작화는 명확함
- 혼합방법 채택 자체는 주제에 적합함
```

**관찰 포인트**: Gemma 4(4B)가 **실제 학술적 비판**을 할 수 있는지 체감. 크기가 작아도 "검증" 역할에는 충분한 경우가 많음.

### Step 4-3. (선택) Codex · Gemini 추가 검증

Codex CLI가 있다면:
```
bash로 아래 실행:
cat output/03_research_questions.md | codex exec "위 연구 설계의 논리적 문제를 반증가능성(falsifiability) 관점에서 공격해줘. reviewer 2 입장. 문제 최소 5개."
결과를 output/04_verification_codex.md 에 저장.
```

Gemini CLI가 있다면:
```
bash로 아래 실행:
cat output/03_research_questions.md | gemini "위 연구 설계의 실행 가능성 문제와 자원 제약 관점 비판을 해줘."
결과를 output/04_verification_gemini.md 에 저장.
```

### Step 4-4. 종합

Claude Code에 입력:
```
output/04_verification_*.md 파일들을 모두 읽고,
공통 지적 항목을 표로 정리해줘.
컬럼: 지적사항 | Gemma4 | Codex | Gemini | 공통 여부
공통 항목은 우선순위 높은 약점으로 간주.
결과를 output/05_summary.md 에 저장.
```

**예상 최종 결과 (발췌)**:
```markdown
# 교차검증 종합

| 지적사항 | Gemma4 | Codex | Gemini | 공통 |
|---|---|---|---|---|
| 정확도 준거 타당성 (회상법 자체 오류) | ✅ | ✅ | — | 2/3 |
| 표본 크기 근거 부재 | ✅ | ✅ | ✅ | **3/3** |
| 선택편향 (참여 자발성) | — | — | ✅ | 1/3 |
| 개념 정의 모호 (사용성 = ?) | — | ✅ | — | 1/3 |

**최우선 수정 대상**: 3/3 공통 지적인 "표본 크기 근거".
```

### 💥 Part 4 자주 막히는 곳

| 증상 | 원인 | 해결 |
|---|---|---|
| `$(cat ...)` 구문 에러 | Windows cmd/파워셸 문법 아님 | 본문의 Windows 블록 (`Get-Content ... \|`) 사용 |
| ollama run이 종료 안 됨 | 파이프 입력을 기다리고 있음 | 정상. 입력 끝나면 자동 종료 — 기다리기 |
| 결과 파일이 비어있음 | 모델이 응답을 생성 전에 pipe 닫힘 | 입력 크기 확인. 너무 크면 주요 섹션만 추출해서 전달 |
| codex/gemini가 명령을 못 찾음 | 미설치 또는 PATH 문제 | `npm install -g @openai/codex` / `@google/gemini-cli` 재설치 후 새 터미널 |

---

## Part 5 — Streamlit 앱 완주

### Step 5-1. Python 버전 확인

```bash
python3 --version    # macOS/Linux
python --version     # Windows
```
→ 3.9 이상 필요. 없으면 https://www.python.org (Windows는 설치 시 "Add to PATH" 체크 필수).

### Step 5-2. 리포로 이동

```bash
cd ~/Downloads/yonsei_research_workshop/demo/streamlit_research_team/
# 또는 본인이 clone/다운로드한 위치
pwd
# .../demo/streamlit_research_team
```

### Step 5-3. venv 생성 + 활성화

**macOS / Linux**:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
프롬프트가 바뀜:
```
(.venv) your_name@MacBook streamlit_research_team %
```

**Windows (PowerShell)**:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
프롬프트:
```
(.venv) PS C:\...\streamlit_research_team>
```

**권한 에러 시** (Windows):
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```
→ Y 입력 후 다시 활성화 시도.

### Step 5-4. 패키지 설치

```bash
pip install -r requirements.txt
```
진행 화면:
```
Collecting streamlit>=1.30.0
  Downloading streamlit-1.32.0-py2.py3-none-any.whl.metadata (8.5 kB)
Collecting ollama>=0.6.1
  Downloading ollama-0.6.1-py3-none-any.whl.metadata (4.1 kB)
Collecting python-docx>=1.0.0
  Downloading python_docx-1.1.0-py3-none-any.whl.metadata (2.0 kB)
Collecting pypdf>=4.0.0
  Downloading pypdf-4.0.1-py3-none-any.whl.metadata (7.2 kB)
...
Successfully installed streamlit-1.32.0 ollama-0.6.1 python-docx-1.1.0 pypdf-4.0.1 ...
```
약 1-2분.

### Step 5-5. Ollama 서버 확인

```bash
ollama list
```
`gemma4`가 목록에 있어야 함. 없으면 `ollama pull gemma4`.

### Step 5-6. Streamlit 앱 실행

```bash
streamlit run app.py
```
화면:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.xxx:8501
```
브라우저가 자동으로 열림. 안 열리면 http://localhost:8501 을 수동으로 접속.

### Step 5-7. 앱 첫 화면 예상

브라우저에 보일 구성:
- **좌측 사이드바**:
  - "설치된 모델" 드롭다운 — `gemma4:latest` 등 자동 감지된 목록
  - "세션" 섹션 — "새 프로젝트" 버튼
  - "🎓 지도교수 모드" 토글 (선택)
- **메인 영역**:
  - 프로젝트 이름 입력
  - 연구 분야 (드롭다운: 식품영양 / 노화 / 섬유 등)
  - 연구 단계 (드롭다운: 주제 탐색 / 선행연구 / RQ 도출)
  - 키워드 입력창
  - 맥락 입력창 (CLAUDE.md 내용 붙여넣어도 OK)
  - "▶ 연구팀 실행" 버튼

### Step 5-8. 1회 실행 예시

입력:
- 프로젝트: "식단기록 앱 연구"
- 분야: 식품영양
- 단계: 주제 탐색
- 키워드: 독거노인, 디지털 헬스, 식이 기록
- 맥락: (비어있어도 OK. 있으면 CLAUDE.md 그대로 복사)

"▶ 연구팀 실행" 클릭. 화면 변화:
```
[수연] 주제 탐색 중... (스트리밍 텍스트)
  → 3개 주제 후보 생성 중 ●●●
  → 완료 ✓

[준호] 검증 중... (기존 주장에 동의하지 마세요)
  → 5관점에서 공격 ●●●
  → 완료 ✓

[지은] 총괄 중...
  → 연구 설계 초안 도출 ●●●
  → 완료 ✓
```

총 3-5분 (로컬 모델 기준, 첫 호출 포함).

**최종 화면**:
- 각 에이전트 결과가 카드 형태로 병렬 표시
- 하단에 **.docx 다운로드** 버튼
- **근거 원장** (ledger) — 몇 건이 `[근거:파일]` 태그이고 몇 건이 `[추측]` 태그인지

### 💥 Part 5 자주 막히는 곳

| 증상 | 원인 | 해결 |
|---|---|---|
| "streamlit: command not found" | venv 활성화 안 됨 | 프롬프트 앞에 `(.venv)` 있는지 확인 |
| 사이드바에 모델이 안 보임 | Ollama 서버 미실행 | `ollama list`로 서버 확인 |
| 실행 중 "Connection error" | Ollama 서버 중단됨 | 서버 재실행 + 앱 새로고침 |
| 한국어 응답이 어색함 | 작은 모델(4B) 한계 | 16GB+ 머신이면 `ollama pull deepseek-r1:14b` 후 사이드바에서 변경 |
| 브라우저에서 앱이 "This site can't be reached" | 포트 충돌 | `streamlit run app.py --server.port 8502` |
| .docx 다운로드 에러 | python-docx 미설치 | `pip install python-docx>=1.0.0` |

---

## 전체 완주 체크포인트

홈스터디 1회를 끝까지 따라왔다면 아래가 모두 성립해야 합니다:

- [ ] 터미널에서 `node`, `claude`, `ollama`, `python` 4개 명령이 모두 인식됨
- [ ] `~/workshop_team_demo/output/` 에 `01_topics.md`, `02_literature.md`, `03_research_questions.md`, `04_verification_gemma4.md` (최소 4개) 존재
- [ ] 각 파일이 빈 파일이 아니고, 학술체 한국어로 내용이 채워져 있음
- [ ] 교차검증 결과에서 "검증 실패: [이유]" 형식이 최소 1건 등장
- [ ] Streamlit 앱에서 연구팀 1회 실행 + .docx 다운로드 완료
- [ ] 다운받은 .docx가 Word/Pages/LibreOffice에서 열림
- [ ] "왜 여러 모델이 필요한가"를 본인 말로 1-2 문장 설명 가능

**전부 ✅**라면 — 당신은 이제 로컬 연구 보조팀을 자립적으로 운용할 수 있습니다.

---

## 한 걸음 더 — 본인 분야로 커스터마이징

### A. Streamlit 앱의 시스템 프롬프트 바꾸기

`demo/streamlit_research_team/agents.py` 파일을 열면 3개 에이전트(수연/준호/지은)의 시스템 프롬프트가 있습니다. 본인 분야·자주 쓰는 표현·학과 표준에 맞게 문구만 수정하면 **같은 파이프라인이 다른 도메인 연구팀으로 변환**됩니다.

예: 노인학 전공이라면 "수연"의 프롬프트에 "65세 이상 노인 표본 연구 설계를 우선 고려"를 추가.

### B. 본인만의 검증 프롬프트 템플릿

`output/04_verification_*.md`를 여러 번 생성하면서 **"잘 지적한 프롬프트"**를 따로 저장해두세요. 다음 프로젝트에서 그 프롬프트를 재사용 = 본인 분야의 자동화된 reviewer 2.

### C. CLAUDE.md를 분야별로 분화

- `CLAUDE.md` — 학위논문 전체
- `CLAUDE_thesis_intro.md` — 서론 전용 (인용·문체 타이트)
- `CLAUDE_grant.md` — 연구비 신청서용 (청중이 다르므로 문체·강조점 다름)

Claude Code는 현재 폴더의 CLAUDE.md만 자동 로드하므로, 분화된 문서는 세션 시작 시 "오늘은 CLAUDE_thesis_intro.md 기준으로"라고 명시.

---

*작성: 2026-04-18 | 외부 도움 없이 혼자 완주 가능한 수준을 목표로 함 | CC BY-NC-SA 4.0*
