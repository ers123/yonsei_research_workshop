# 실습 사전 환경 설치

워크숍 실습을 원활하게 진행하려면 **전날 저녁까지** 아래 환경을 준비해 주세요.

**구조 (2026-04-18 개편)**: Part 3 실습은 **Track A + B 전원 진행**입니다. Track C (연구 조수 팀)는 Part 2 라이브 데모 + 홈스터디 가이드로 재편되었습니다. 따라서 **당일 필수 세팅은 A·B에 필요한 것만**이면 됩니다. C용 로컬 모델 설치는 관심 있는 분만 집에서 따라 해 보면 됩니다.

---

## 🧭 전날 밤 10분 체크리스트

A·B 실습만 하실 경우 — 아래만 확인하면 됩니다:

- [ ] Claude 또는 ChatGPT 계정에 **로그인된 상태**
- [ ] Chrome 또는 Edge 브라우저
- [ ] 텍스트 편집기 (Windows 메모장 / macOS 텍스트편집기 / VS Code 등)
- [ ] **리포지토리 받기** (아래 Section 0 참조)
- [ ] 본인 연구 자료 1건 이상 (없어도 OK, 강사 샘플 있음)

Track C도 시도하실 분 (홈스터디) — 추가로:

- [ ] Node.js 18+ 설치
- [ ] Ollama 설치 + `gemma4` 모델 다운로드 (약 3 GB)
- [ ] Claude Code 설치 + 첫 로그인

---

## Section 0 — 리포지토리 받기 (5분)

실습 자료(샘플 PDF, 프롬프트, 템플릿)는 모두 이 리포에 있습니다. 세 가지 방법 중 **하나** 선택:

### 방법 A — ZIP 다운로드 (가장 간단, 초심자 권장)

1. GitHub 페이지 방문: https://github.com/ers123/yonsei_research_workshop
2. 초록색 **"Code"** 버튼 클릭 → **"Download ZIP"**
3. 다운받은 파일 압축 해제 (예: 바탕화면에 `yonsei_research_workshop/` 폴더 생성)

**장점**: Git 몰라도 OK. **단점**: 이후 업데이트 받기 불편.

### 방법 B — GitHub Desktop (GUI)

1. https://desktop.github.com 에서 GitHub Desktop 설치
2. 앱 실행 → **"Clone a repository from the Internet"**
3. URL 입력: `https://github.com/ers123/yonsei_research_workshop`
4. 로컬 위치 지정 → Clone

**장점**: 업데이트 원클릭. **단점**: 앱 설치 필요.

### 방법 C — git CLI

**macOS / Linux**:
```bash
cd ~/Downloads   # 또는 원하는 상위 폴더
git clone https://github.com/ers123/yonsei_research_workshop
cd yonsei_research_workshop
```

**Windows (PowerShell)**:
```powershell
cd $HOME\Downloads
git clone https://github.com/ers123/yonsei_research_workshop
cd yonsei_research_workshop
```

Git이 없으면: macOS는 `brew install git`, Windows는 https://git-scm.com 에서 설치.

### 확인

압축 해제 또는 clone이 끝나면 폴더 안에 아래가 있어야 합니다:
- `hands_on/` (실습 자료)
- `README.md`
- `demo/qualitative_research/` (데모 사례)
- `appendix/`

> **슬라이드(.pptx)는 공개 repo 에 포함되지 않습니다.** Google Drive 로 별도 공유 — 링크는 강사(amazone1@daum.net) 에게 요청.

---

## Section 1 — 계정 · 브라우저 · 로그인 (필수)

### 1-1. 계정

| 서비스 | URL | 권장 |
|---|---|---|
| **Claude** | https://claude.ai | Pro ($20/월) 권장. 무료도 OK (업로드 한도 주의) |
| **ChatGPT** | https://chat.openai.com | Plus ($20/월) 권장. 무료도 OK |
| **NotebookLM** (선택) | https://notebooklm.google.com | Google 계정으로 접속 |

### 1-2. 로그인 상태 확인 (가장 자주 놓치는 부분)

당일 아침 다음을 확인:
- [ ] 브라우저에서 **Claude.ai 열었을 때 바로 새 채팅이 뜬다** (로그인 화면이 아님)
- [ ] ChatGPT도 동일

> **한국에서 Claude.ai 가입이 막히는 경우가 가끔 있습니다.** 이메일 가입이 안 되면 "Google로 로그인" 시도. 그래도 안 되면 ChatGPT만 써도 Track A·B는 진행 가능.
> **OAuth callback 문제**: 연세대 캠퍼스 와이파이에서 드물게 OAuth 리다이렉트가 막히는 경우가 있음. 모바일 핫스팟이나 집에서 미리 로그인을 완료해두세요.

### 1-3. 브라우저

- Chrome, Edge, 또는 Firefox 중 하나
- 위 사이트들을 북마크바에 등록해두면 편함

---

## Section 2 — 텍스트 편집기 (Track A · B 공통)

마크다운 파일(`.md`)을 저장할 도구가 필요합니다. 최소 하나 있으면 OK.

| OS | 기본 사용 가능 (주의사항 있음) | 권장 |
|---|---|---|
| **Windows** | 메모장 (파일 형식 "모든 파일", 인코딩 "UTF-8" 지정 필요) | **VS Code** |
| **macOS** | 텍스트편집기 (포맷 → "일반 텍스트로 변환" 필요) | **VS Code** |

### VS Code 빠른 설치

| OS | 명령 또는 링크 |
|---|---|
| **Windows** | PowerShell: `winget install Microsoft.VisualStudioCode` |
| **macOS** | Terminal: `brew install --cask visual-studio-code` |
| **공통** | 또는 https://code.visualstudio.com 에서 installer 다운로드 |

다른 편집기(Cursor, Obsidian, Sublime Text, Notepad++)를 이미 쓰신다면 그걸로 OK.

---

## Section 3 — 본인 자료 준비 (선택)

- 본인이 관심 있는 PDF 1건 이상 (논문, 보고서, 리뷰 논문)
- 없어도 강사 제공 **AI Index Report 2026** (`hands_on/sample_data/ai_index/`)로 실습 가능

---

## Section 4 — Track C 용 추가 설치 (홈스터디 원하는 분만)

> **당일 필수 아님.** A·B만 하실 분은 이 섹션 건너뛰셔도 됩니다.
> 관심 있는 분은 워크숍 **이후 집에서** 이 섹션 + `hands_on/prompts_v2/track_c_연구조수팀.md` Part B(홈스터디 가이드)를 따라 해 보세요.

### 4-1. Node.js 18+ (Claude Code에 필요)

**확인**:
```bash
node --version
```
→ `v18.xx.x` 이상이면 OK. 없으면:

| OS | 설치 |
|---|---|
| **macOS** | `brew install node` 또는 https://nodejs.org |
| **Windows** | PowerShell: `winget install OpenJS.NodeJS.LTS` 또는 https://nodejs.org |
| **Linux** | `sudo apt install nodejs npm` |

> **Windows 설치 주의**: installer의 **"Add to PATH"** 체크박스가 기본 체크되어 있는지 확인. 빠지면 `node`, `npm` 명령이 안 먹힘.

### 4-2. Claude Code

```bash
npm install -g @anthropic-ai/claude-code
claude --version
```

첫 실행 (`claude`)시 브라우저가 자동으로 열립니다 → Anthropic 계정 로그인 → 터미널로 돌아옴.

### 4-3. Ollama + 모델

| OS | 설치 |
|---|---|
| **macOS** | `brew install ollama` 또는 https://ollama.com |
| **Windows** | https://ollama.com installer → 실행 (설치 후 자동 백그라운드 실행) |
| **Linux** | `curl -fsSL https://ollama.com/install.sh \| sh` |

모델 다운로드 (RAM 기준):

```bash
# 8 GB (최소):
ollama pull gemma4                                  # ~3 GB

# 16 GB (권장):
ollama pull gemma4 && ollama pull phi4-mini        # 추가 ~3 GB

# 32 GB+ (풀 구성):
ollama pull gemma4 && ollama pull deepseek-r1:14b  # 추가 ~9 GB
```

> **다운로드 시간**: 100 Mbps wifi 기준 3 GB ≈ 5분, 9 GB ≈ 15분. **당일 다운로드 금지** — 전날 밤 미리.
> **Windows**: Ollama installer가 자동으로 백그라운드 실행. `ollama serve` 별도 불필요.
> **macOS Homebrew 설치 시**: `brew services start ollama` 또는 별도 터미널에서 `ollama serve`.

### 4-4. (선택) 교차검증용 추가 CLI

| 도구 | 설치 | 비용 | 용도 |
|---|---|---|---|
| **Codex CLI** | `npm install -g @openai/codex` | ChatGPT Plus 포함 | OpenAI 계열 검증 |
| **Gemini CLI** | `npm install -g @google/gemini-cli` | 무료 (Google 계정) | Google 계열 검증 |

둘 다 없어도 Ollama Gemma 4 하나로 교차검증의 핵심은 체험 가능.

### 4-5. 확인

```bash
node --version      # v18+
claude --version    # 버전 번호
ollama list         # gemma4 항목
```

셋 다 OK면 준비 완료.

---

## Section 5 — 알아두면 좋은 Claude Code 기능

| 명령 | 설명 |
|---|---|
| `/loop` | 반복 작업 자동화. "문헌 10개를 하나씩 처리해줘" 같은 지시 |
| `/compact` | 대화가 길어졌을 때 맥락 요약 (메모리 절약) |
| `/permissions` | 도구 권한 관리 — bash 명령 반복 승인이 귀찮을 때 |

```
# /loop 예시 — Track B 심화에서 사용
/loop sample_data/ 폴더의 파일을 하나씩 읽고 output/summaries/에 저장해줘
```

---

## 실습 파일 안내

당일 사용할 프롬프트와 템플릿:

```
hands_on/
├── SETUP.md                     ← 이 파일
├── prompts_v2/
│   ├── track_a_맥락문서.md       ← 트랙 A 실습 가이드 (20-25분)
│   ├── track_b_대량처리.md       ← 트랙 B 실습 가이드 (30-35분)
│   └── track_c_연구조수팀.md     ← 트랙 C 데모 스크립트 + 홈스터디 가이드
├── templates/
│   ├── CLAUDE.md.example        ← 맥락 문서 템플릿
│   └── AGENTS.md.example        ← 에이전트 행동 규칙 템플릿
├── sample_data/
│   ├── ai_index/                ← Track B 주 실습 자료 (AI Index 2026 PDF)
│   └── sample_01~10.txt         ← Track B 심화 자습용 (10개 가상 논문)
├── references/                   ← Claude Code 퀵/사용 가이드 (자습용)
├── scenario_comparison/          ← 4모델 교차검증 실제 결과
├── ra_team_setup.md             ← RA 팀 상세 구성
└── ra_team_tiers.md             ← Free/Standard/Full 비용 비교
```

---

## 트러블슈팅

**Q. 리포 ZIP 다운로드 파일명이 한글 깨짐**
A. 압축 해제 시 인코딩을 UTF-8로. Windows 기본 압축풀기가 문제면 **알집**, **반디집**, 또는 **7-Zip** 사용.

**Q. Claude/ChatGPT 응답이 이상해요.**
A. 세션을 새로 열어서(New Chat) 다시 시도. 이전 맥락이 오염됐을 수 있습니다.

**Q. Claude Code 설치가 안 돼요.**
A. Node.js 18+ 필요. `node --version`으로 확인. Windows는 "Add to PATH" 체크 여부 확인.

**Q. Windows에서 터미널이 안 열려요.**
A. 시작 메뉴 → **"PowerShell"** 검색 → 열기 (Windows Terminal 또는 Windows PowerShell).
    또는 VS Code 내장 터미널(Ctrl+`) 사용.

**Q. `.ps1` 스크립트 실행이 막힘 (venv 활성화 등)**
A. PowerShell에서 한 번 실행:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**Q. Ollama 모델이 한국어를 못 알아들어요.**
A. `gemma4` (E4B) 이상이면 기본 한국어 OK. 1B급 모델은 한국어 불안정합니다.

**Q. Ollama 첫 호출이 너무 오래 걸려요.**
A. 모델을 메모리에 올리는 시간 (1-3분, 저사양은 5-10분). 정상입니다. 두 번째부터 빠름.

**Q. 노트북이 느려요.**
A. 트랙 A/B는 웹 도구만으로 가능합니다. 로컬 모델(Track C)은 16 GB 이상 권장.

**Q. 한국어 파일명이 깨져요.**
A. macOS ↔ Windows 이동 시 발생 가능. UTF-8 인코딩 확인.

**Q. 발표 중 배터리가 빨리 닳아요 (Ollama 사용 시).**
A. 로컬 모델 추론은 CPU/GPU 100% 사용. 전원 콘센트 근처 자리 선호.

**Q. 모르겠어요.**
A. 지금 쓰고 있는 AI에게 물어보세요! "이 에러 뭐야?"라고 치면 됩니다.

---

**문의: amazone1@daum.net 또는 워크숍 당일 질문**
