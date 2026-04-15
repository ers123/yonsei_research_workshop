# Reference Setup: MacBook Air M4 32GB

> 강사 환경 기준 실제 구성. 워크숍 당일 데모 및 트러블슈팅 참조용.
> 기록일: 2026-04-15

---

## 하드웨어

| 항목 | 사양 |
|---|---|
| 모델 | MacBook Air (Mac16,13) |
| 칩 | Apple M4 |
| 메모리 | 32GB Unified |
| OS | macOS Darwin 25.4.0 |

## 소프트웨어

| 도구 | 버전 | 설치 방법 |
|---|---|---|
| Node.js | v24.7.0 | `brew install node` |
| pnpm | 10.12.2 | `npm install -g pnpm` |
| Ollama | 최신 | `brew install ollama` |
| Claude Code | 최신 | `npm install -g @anthropic-ai/claude-code` |
| Marp CLI | v4.3.1 | `brew install marp` |
| Python | 3.11.5 | 시스템 내장 |

## Ollama 모델 구성

```
$ ollama list

NAME                        SIZE      역할
qwen3.5:9b                  6.6 GB    주력 (Scout + Writer)
deepseek-r1:14b             ~9 GB     추론·검증 특화 (Verifier 1) ← 다운로드 중
gemma4:26b-a4b-it-q4_K_M    17 GB     빠른 교차검증 (Verifier 2, MoE)
nomic-embed-text             274 MB    임베딩 (RAG용)
```

### 메모리 운용 계획

32GB에서 동시 실행 가능한 조합:

| 조합 | 합산 | 동시 실행 | 용도 |
|---|---|---|---|
| qwen3.5 + deepseek-r1 | ~16GB | 가능 | Writer + Verifier 교차 |
| qwen3.5 + gemma4 | ~24GB | 가능 (여유 적음) | Writer + 빠른 검증 |
| deepseek-r1 + gemma4 | ~26GB | 빠듯 | 이중 검증 |
| 3개 동시 | ~33GB | 불가 (swap 발생) | 번갈아 사용 |

**운용 원칙**: 2개까지 동시, 3개는 번갈아. `ollama stop [모델명]`으로 내리고 다른 모델 올리기.

## Claude Code 로컬 모델 연결

```bash
# 기본 사용 (Anthropic API)
claude

# 로컬 모델 사용 (무료)
ANTHROPIC_BASE_URL=http://localhost:11434/v1 \
ANTHROPIC_MODEL=qwen3.5:9b \
claude
```

### alias (강사 환경)

```bash
# ~/.zshrc
alias claude-local='ANTHROPIC_BASE_URL=http://localhost:11434/v1 ANTHROPIC_MODEL=qwen3.5:9b claude'
alias claude-deepseek='ANTHROPIC_BASE_URL=http://localhost:11434/v1 ANTHROPIC_MODEL=deepseek-r1:14b claude'
```

## RA 팀 아키텍처

```
[사용자] → 연구 주제
              ↓
┌──────────────────────────────────────────┐
│  Claude Code (Harness / Orchestrator)    │
│  CLAUDE.md 자동 로드 → 맥락 유지         │
│  MCP 도구 → 파일, 웹검색, DB             │
└──────┬──────────┬──────────┬─────────────┘
       ↓          ↓          ↓
  ┌─────────┐ ┌────────┐ ┌──────────────┐
  │ Scout + │ │Verifier│ │ Verifier 2   │
  │ Writer  │ │ 1      │ │              │
  │         │ │ (추론) │ │ (빠른 교차)  │
  │ qwen    │ │deepseek│ │ gemma4       │
  │ 3.5:9b  │ │r1:14b  │ │ 26b (MoE)   │
  └─────────┘ └────────┘ └──────────────┘
    Qwen 계열   DeepSeek    Google 계열
         ← 3계열 교차검증 →
```

### 왜 Claude Code가 Harness로 최적인가

1. **CLAUDE.md 자동 로드** — 프로젝트 맥락이 매 세션 자동 적용
2. **Subagent 호출** — 역할별 로컬 모델 전환이 자연스럽다
3. **MCP 도구** — 파일·웹검색·DB 연결이 추가 코딩 없이 가능
4. **추가 프레임워크 불필요** — CrewAI, LangGraph, Paperclip 없이 동작
5. **학습 곡선 최소** — 학생이 배울 도구가 하나(Claude Code)로 줄어든다

### 프레임워크 비교 (검토 완료)

| 프레임워크 | 검토 결과 | 채택 여부 |
|---|---|---|
| **Claude Code + Ollama** | 가장 단순, 로컬 모델 네이티브 지원 | 채택 |
| CrewAI | Ollama 지원, 그러나 Python 설정 필요 | 불채택 (복잡) |
| AutoGen (MS) | 지원하나 설정 파일 많음 | 불채택 |
| LangGraph | Ollama 간접 지원, 과도한 엔지니어링 | 불채택 |
| Paperclip | Ollama 미지원, 코딩 에이전트 전용 | 불채택 (용도 불일치) |

## 대학원생 환경별 가이드

| 환경 | 모델 구성 | 메모리 | 비고 |
|---|---|---|---|
| **8-16GB 노트북** | gemma4:4b + phi4-mini | ~9GB | 최소 구성. 요약·태깅 수준. |
| **24GB 노트북** | qwen3.5:9b + gemma4:4b | ~12GB | 한국어 글쓰기 가능. |
| **32GB 노트북** | qwen3.5:9b + deepseek-r1:14b + gemma4:26b | 번갈아 | 3계열 교차검증. 본 데모 기준. |
| **연구실 PC (64GB+)** | qwen3-coder:30b + deepseek-r1:14b + gemma4:26b | 동시 가능 | 최상위 로컬 구성. |

### 16GB 이하 학생을 위한 팁

- 2개 모델 동시 실행 어려움 → **하나씩 번갈아** 사용
- `ollama stop [모델]`으로 명시적으로 내린 후 다음 모델 실행
- Writer 작업 → 파일 저장 → Writer 모델 내림 → Verifier 모델 올림 → 검증
- 클라우드 무료 티어(Claude Free, ChatGPT Free)를 Verifier로 활용하는 것도 방법

---

*이 문서는 강사 환경 레퍼런스입니다. 학생용 가이드: `hands_on/ra_team_setup.md`*
