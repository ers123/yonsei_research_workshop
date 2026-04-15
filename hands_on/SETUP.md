# 실습 사전 환경 설치

워크숍 실습을 원활하게 진행하려면 **전날 저녁까지** 아래 환경을 준비해 주세요.
트랙에 따라 필요한 세팅이 다릅니다.

---

## 전체 공통 (필수)

### 1. 계정
- [ ] **Claude** — https://claude.ai (Pro 권장, 최소 무료)
- [ ] **ChatGPT** — https://chat.openai.com (Plus 권장, 최소 무료)
- [ ] **NotebookLM** — https://notebooklm.google.com (Google 계정으로 접속)

### 2. 브라우저
- [ ] Chrome 또는 Edge
- [ ] 위 사이트를 북마크바에 등록해두면 편합니다

### 3. 본인 연구 자료
- [ ] 논문, 인터뷰 전사, 관심 주제 메모 등 **1건 이상**
- [ ] (못 가져왔어도 OK — 강사 샘플 자료가 있습니다)

---

## 트랙별 추가 세팅

### 트랙 A — 맥락 문서 만들기
추가 설치 없음. Claude / ChatGPT 계정이면 충분합니다.

### 트랙 B — 대량 자료 처리
- [ ] 텍스트 편집기 (VS Code, Obsidian, Cursor 등 — 결과 파일을 보기 위해)
- [ ] (선택) Claude Code — 배치 처리를 직접 해보려면

### 트랙 C — 연구 조수 팀 (로컬 모델 + Claude Code)
아래 모두 필요합니다:

```bash
# 1. Claude Code 설치
npm install -g @anthropic-ai/claude-code
# 공식 문서: https://docs.claude.com

# 2. Ollama 설치 + 모델 다운로드
# macOS:
brew install ollama
# 또는 Linux/macOS:
curl -fsSL https://ollama.com/install.sh | sh
# Windows: https://ollama.com 에서 installer 다운로드

# 3. 모델 받기 (RAM 기준)
# 8GB:
ollama pull gemma3:4b
# 16GB:
ollama pull gemma3:4b && ollama pull qwen2.5:14b
# 32GB+:
ollama pull gemma3:4b && ollama pull qwen2.5:14b && ollama pull phi4-mini
```

**확인 방법**:
```bash
claude --version    # → 버전 번호가 나오면 OK
ollama list         # → 모델 1개 이상 보이면 OK
```

**트랙 C 설치가 안 되면**: 당일 시간이 부족할 수 있어요.
전날 미리 설치하고, 안 되면 워크숍 시작 전에 강사에게 알려주세요.

---

## 실습 파일 안내

당일 사용할 프롬프트와 템플릿:

```
hands_on/
├── prompts_v2/
│   ├── track_a_맥락문서.md     ← 트랙 A 실습 가이드
│   ├── track_b_대량처리.md     ← 트랙 B 실습 가이드
│   └── track_c_연구조수팀.md   ← 트랙 C 실습 가이드
│
├── templates/
│   ├── CLAUDE.md.example       ← 프로젝트 맥락 문서 템플릿
│   └── AGENTS.md.example       ← 에이전트 행동 규칙 템플릿
│
└── prompts/                     ← V1 프롬프트 (자습/참고용)
    ├── 01_자료탐색.md
    ├── 02_구조화.md
    ├── 03_작성.md
    └── 04_그림작성.md
```

---

## 트러블슈팅

**Q. Claude/ChatGPT 응답이 이상해요.**
A. 세션을 새로 열어서(New Chat) 다시 시도. 이전 맥락이 오염됐을 수 있습니다.

**Q. Ollama 모델이 한국어를 못 알아들어요.**
A. `gemma3:4b` 이상이면 기본 한국어 OK. `1b` 급은 한국어 불안정합니다.

**Q. Claude Code 설치가 안 돼요.**
A. Node.js 18+ 필요. `node --version`으로 확인. 없으면 https://nodejs.org 에서 설치.

**Q. 노트북이 느려요.**
A. 트랙 A/B는 웹 도구만으로 가능합니다. 로컬 모델은 트랙 C에서만 사용.

**Q. 한국어 파일명이 깨져요.**
A. macOS → Windows 이동 시 발생 가능. UTF-8 인코딩 확인.

---

**문의: amazone1@daum.net 또는 워크숍 당일 질문**
