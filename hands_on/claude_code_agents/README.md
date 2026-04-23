# Claude Code 연구팀 Agents (.claude/agents/)

**Streamlit Lite 의 3-에이전트 파이프라인을 Claude Code 네이티브 subagent 형식으로 포팅**한 템플릿.

> **대상 독자**: Claude Code 이미 쓰고 있는 대학원생/연구자. Ollama · Streamlit 설치 싫고, 에디터에서 바로 연구팀 기능을 쓰고 싶은 분.

## 왜 이것도 제공하나

워크숍 슬라이드에서 말한 것처럼 **같은 harness, 다른 도구**:

| 도구 | 용도 |
|---|---|
| `demo/streamlit_research_team_lite/` | 비CLI 사용자 · 완전 로컬 Ollama · GUI |
| **이 폴더 (`hands_on/claude_code_agents/`)** | **Claude Code 사용자 · Anthropic 클라우드 · CLI 통합** |
| Zhang scholar-skill | 연구실 풀 자동화 (26 skills × 18 phases) |

3가지 중 편한 것 선택. 본질은 같은 "3-role × 3-stage = 9 prompts + 감독 persona" 구조.

---

## 설치 (5분)

### 1) Claude Code 설치 확인

```bash
claude --version
```

없으면 OS 별로:

**macOS / Linux**:
```bash
curl -fsSL https://claude.ai/install.sh | bash
# PATH 경고 나오면 출력된 echo 명령 실행 후 터미널 재시작
```

**Windows (PowerShell)**:
```powershell
irm https://claude.ai/install.ps1 | iex
# 실행 정책 에러 시: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### 2) 본인 프로젝트에 agents 복사

**옵션 A — 프로젝트별 (해당 프로젝트 폴더에서만 작동)**:

macOS / Linux:
```bash
cd /path/to/your/research-project
mkdir -p .claude/agents
cp hands_on/claude_code_agents/*.md .claude/agents/
```

Windows PowerShell:
```powershell
cd C:\path\to\your\research-project
New-Item -ItemType Directory -Force -Path .claude\agents | Out-Null
Copy-Item hands_on\claude_code_agents\*.md .claude\agents\
```

**옵션 B — 전역 (모든 Claude Code 세션에서 사용 가능)**:

macOS / Linux:
```bash
mkdir -p ~/.claude/agents
cp hands_on/claude_code_agents/*.md ~/.claude/agents/
```

Windows PowerShell:
```powershell
New-Item -ItemType Directory -Force -Path $HOME\.claude\agents | Out-Null
Copy-Item hands_on\claude_code_agents\*.md $HOME\.claude\agents\
```

### 3) 확인

`claude` 실행 후:
```
/agents
```

목록에 수연/준호/지은/한민수 (영문: scout-*/critic-*/director-*/advisor) 가 보이면 OK.

---

## 사용법

### 자동 위임 (Claude Code 가 알아서 선택)

```
> 고령자 1인가구 식품불안정을 주제로 연구 아이디어 3개 비교해줘
```

→ Claude Code 가 scout-explore agent 로 자동 위임

### 명시적 호출

```
> @scout-explore 이 주제로 탐색해줘: ...
> @critic-explore 위 결과를 Reviewer 2 스타일로 비판
> @director-explore 두 결과 종합해서 최종 설계 작성
```

### 파이프라인 시퀀스 (전체 단계)

단계마다 적절한 agent 체인을 호출:

| 단계 | 시퀀스 |
|---|---|
| 주제 탐색 | `scout-explore` → `critic-explore` → `director-explore` |
| 선행연구 정리 | `scout-literature` → `critic-literature` → `director-literature` |
| RQ 도출 | `scout-rq` → `critic-rq` → `director-rq` |
| (선택) 지도교수 질문 | `advisor` (단계 무관) |

**팁**: Claude Code 에 "단계 X 전체 파이프라인 돌려줘" 라고만 말해도 자동 체인 가능 (모델이 description 읽고 판단).

---

## 파일 구성

```
claude_code_agents/
├── README.md                        ← 이 파일
│
├── scout-explore.md                 ← 수연 · 주제 탐색
├── scout-literature.md              ← 수연 · 선행연구 정리
├── scout-rq.md                      ← 수연 · RQ 도출
│
├── critic-explore.md                ← 준호 · 주제 탐색 검증
├── critic-literature.md             ← 준호 · 선행연구 검증
├── critic-rq.md                     ← 준호 · RQ 반증가능성 공격
│
├── director-explore.md              ← 지은 · 연구 설계 총괄
├── director-literature.md           ← 지은 · 선행연구 메모 총괄
├── director-rq.md                   ← 지은 · RQ 확정
│
└── advisor.md                       ← 한민수 · 지도교수 메타 질문 (단계 무관)
```

---

## Streamlit Lite 와의 동등성

| Streamlit Lite | Claude Code |
|---|---|
| `agents.py::STAGE_PROMPTS` | 이 폴더의 10개 `.md` 파일 |
| 사이드바 모델 선택 | Claude Code `/model` · agent 별 `model:` 필드 |
| "🎯 예시로 시작" 버튼 | `/agents` → 원하는 agent 선택 후 텍스트 입력 |
| `.sessions/*.json` 저장 | Claude Code 세션 자동 저장 + git commit |
| 근거 원장 (`[근거: 파일]`) | 동일 (모든 agent 에 GROUNDING_RULE 포함) |
| 사고 모드 (think) | Claude Opus 자체 사고 (extended thinking) |
| `.docx` 내보내기 | `claude` 안에서 `pandoc` 호출 또는 직접 작성 |

---

## 민감 주제 주의

**(a) 전송 금지** 차원에선 Claude Code 도 결국 Anthropic API 로 호출이 갑니다.
IRB 참가자 식별정보가 들어간다면 **Streamlit Lite (완전 로컬 Ollama)** 를 써야 합니다.

**(b) 주제 민감성** 차원에선 Claude 도 거부 가능성 있음.
대응: `appendix/04_Uncensored_로컬모델_연구활용_가이드.md` 의 4가지 선택지 참조.

---

## 커스터마이징

각 `.md` 파일의 YAML frontmatter 필드를 수정 가능:

```yaml
---
name: scout-explore            # agent 이름 (변경 시 호출 명령도 바뀜)
description: ...               # Claude Code 자동 위임 시 매칭 기준
tools: Read, Grep, WebSearch   # 허용 도구 (생략 시 전체)
model: claude-sonnet-4-6       # 특정 모델 고정 (생략 시 메인 모델)
---
```

예: critic-rq 에만 `model: claude-opus-4-7` 설정해서 반증가능성 공격엔 Opus 사용 · 나머진 Sonnet.

---

*라이선스: CC BY-NC-SA 4.0*
*원본 프롬프트: `demo/streamlit_research_team_lite/agents.py`*
*워크숍: 연세대학교 생활과학대학 (2026.04.24)*
