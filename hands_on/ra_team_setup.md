# 연구 조수 팀 (RA Team) 세팅 가이드

> Claude Code + Ollama 로컬 모델로 구성하는 연구 에이전트 팀
> 별도 프레임워크(CrewAI, Paperclip 등) 없이 동작

---

## 1. 왜 이 구성인가

### 대학원생의 현실

- 유료 API 예산이 제한적이거나 없다
- 인터뷰 전사 등 민감 자료를 외부 서버에 보낼 수 없다 (IRB)
- 하나의 AI에 모든 걸 시키면 맥락이 넘치고, 같은 모델이 쓰고 검증하면 같은 편향이 반복된다

### 해결: Claude Code + Ollama

| 구성 요소 | 역할 | 비유 |
|---|---|---|
| **Ollama** | 로컬 모델을 메모리에 올리고 API로 노출 | 모델의 전원 콘센트 |
| **Claude Code** | 프로젝트 맥락 관리, 도구 호출, 에이전트 조율 | 팀장 + 사무실 환경 |
| **CLAUDE.md** | 프로젝트 배경·규칙·금기를 문서화 | 신입에게 주는 프로젝트 브리핑 |

핵심: Claude Code 자체가 orchestrator다. CrewAI, LangGraph 같은 추가 프레임워크 없이 로컬 모델에 연결하면 바로 RA 팀이 된다.

---

## 2. 로컬 모델을 띄우려면 "서빙 레이어"가 필요하다

로컬 모델은 그냥 파일(가중치)이다. 이것을 메모리에 올려서 질문을 받을 수 있게 만들어주는 게 서빙 레이어다.

| 서빙 도구 | 특징 | 추천 대상 |
|---|---|---|
| **Ollama** | CLI 기반, 가볍다, 표준 API | 대부분의 사용자 (권장) |
| **LM Studio** | GUI 있음, 드래그앤드롭 | CLI가 어려운 경우 |
| **llama.cpp** | 가장 로우레벨, 직접 빌드 | 개발자/커스텀 필요 시 |

**결론: Ollama를 쓰세요.** 가장 가볍고 표준적이며, Claude Code와 바로 연결됩니다.

Paperclip, CrewAI 등 어떤 프레임워크를 쓰든 로컬 모델과 대화하려면 Ollama/LM Studio 중 하나는 **반드시** 필요합니다.

---

## 3. 모델 선택 가이드

### 환경별 권장 (2026년 4월 기준)

| 환경 | 주력 모델 | 보조/검증 모델 | 비고 |
|---|---|---|---|
| **8-16GB RAM** | Gemma 4 E4B (4B) | Phi-4-mini (3.8B) | 최소 구성. 간단한 요약·태깅까지. |
| **24GB RAM** | Qwen 2.5 14B | Gemma 4 E4B | 한국어 글쓰기 가능선. |
| **32GB RAM** | Qwen 3.5 9B | Gemma 4 26B + DeepSeek R1 14B | 추론 + 3계열 교차검증. 본 가이드 기준. |
| **32GB+ / 연구실** | Qwen3-Coder 30B | Devstral Small 2 | agentic 최상위. 256K 컨텍스트. |

### 모델별 연구 적합성

| 모델 | 크기 | 메모리(4bit) | 한국어 | 연구 활용 |
|---|---|---|---|---|
| **Qwen 3.5 9B** | 9B | ~6.6GB | 강함 | 문헌 분석, 학술 글쓰기, 추론. 32GB 노트북의 주력. |
| **Gemma 4 26B (MoE)** | 26B (4B active) | ~17GB | 보통 | 빠른 응답. 검증·교차확인에 적합. 다른 계열이라 교차검증 효과. |
| **Qwen3-Coder 30B** | 30B | ~18GB | 양호 | 코드 + 연구. 256K 컨텍스트. 32GB에서 단독 사용. |
| **Devstral Small 2** | 24B | ~15GB | 양호 | Mistral 계열. agentic coding 특화. |
| **DeepSeek R1 14B** | 14B | ~10GB | 양호 | 추론·검증 특화. MATH 92.8%. Qwen/Gemma와 다른 계열 → 교차검증 최적. |
| **Phi-4-mini** | 3.8B | ~4GB | 보통 | 함수 호출 강점. 16GB 이하 환경에서 검증 전용. |
| **Gemma 4 E4B** | 4B | ~5GB | 보통 | 멀티모달. 이미지 포함 자료 분석 가능. |
| **nomic-embed-text** | — | 274MB | — | 임베딩 전용. RAG(검색 보강 생성)에 사용. |

### 교차 검증이 중요한 이유

같은 모델(예: Qwen)이 쓰고 같은 모델이 검증하면 → **같은 편향, 같은 hallucination 패턴**.
다른 계열 모델(예: Qwen이 쓰고 Gemma가 검증)을 쓰면 → **"서로 다른 방식으로 틀린다"** → 교차점에서 진짜 오류가 드러남.

---

## 4. 설치

> **분기 안내**: 로컬 서빙 레이어는 **Ollama 또는 LM Studio** 둘 중 하나로 충분합니다.
> - **Ollama 만 쓰려는 분** (CLI 선호, 이미 익숙): Step 1 → 2 → 3 경로 B
> - **LM Studio 만 쓰려는 분** (GUI 선호, 초심자): **Step 1 건너뛰기** → 2 → 3 경로 A
> - **둘 다 쓰려는 분** (Claude Code 는 LM Studio, 직접 `ollama run` 검증은 Ollama): Step 1 → 2 → 3 경로 A
>
> 아래 Step 1 은 Ollama 기준입니다. LM Studio 사용자는 Step 3 경로 A 에서 앱 내 모델 다운로드 안내를 참조하세요.

### Step 1: Ollama 설치 + 모델 다운로드 (Ollama 경로)

```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.com/install.sh | sh

# Windows: https://ollama.com 에서 installer 다운로드
```

```bash
# 32GB 기준 권장 모델 (2026년 4월 기준)
ollama pull qwen3.5:9b          # 주력 (Scout + Writer) — 6.6GB
ollama pull deepseek-r1:14b     # 추론·검증 특화 (Verifier) — ~10GB
ollama pull gemma4:26b           # 빠른 교차검증 (2차 Verifier) — 17GB, MoE
ollama pull nomic-embed-text     # 임베딩 (RAG용, 선택) — 274MB

# 16GB 이하라면
ollama pull gemma4               # Gemma 4 E4B (4B)
ollama pull phi4-mini            # 검증용
```

확인:
```bash
ollama list
# → 모델 2개 이상 보이면 OK
```

### Step 2: Claude Code 설치

```bash
npm install -g @anthropic-ai/claude-code
```

확인:
```bash
claude --version
# → 버전 번호가 나오면 OK
```

### Step 3: Claude Code를 로컬 모델에 연결

> ⚠️ **먼저 알아둘 것**: Claude Code 는 **Anthropic Messages API (`/v1/messages`) 포맷** 으로만 통신합니다. Ollama 의 기본 포트(`11434`) 는 **OpenAI-호환 포맷** 만 제공 — 프로토콜이 달라 **직접 연결되지 않습니다**. 아래 두 경로 중 하나가 필요해요.

#### 경로 A (권장 · 초심자용) — LM Studio

LM Studio 0.4 부터 **Anthropic-호환 엔드포인트** 를 기본 제공합니다. 별도 프록시 불필요. GUI 라 설치 장벽도 낮음.

**1. LM Studio 설치 + 모델 다운로드**
- https://lmstudio.ai 에서 OS 에 맞는 설치 파일 받기 → 실행
- 앱 안 "Search" 탭에서 `qwen2.5-coder-14b` 또는 `gemma-3-9b` 등 원하는 모델 다운로드 (GGUF 포맷, Ollama 와 동일 모델 생태계)

**2. 서버 시작**
- LM Studio 앱 좌측 "Developer" 탭 → **Start Server** 버튼
- 기본 주소: `http://localhost:1234`
- "Anthropic" 호환 모드 체크 (최신 버전은 기본 활성화)

**3. Claude Code 를 LM Studio 로 라우팅**
```bash
# macOS / Linux
export ANTHROPIC_BASE_URL=http://localhost:1234
export ANTHROPIC_AUTH_TOKEN=lmstudio
claude
```
```powershell
# Windows (PowerShell)
$env:ANTHROPIC_BASE_URL="http://localhost:1234"
$env:ANTHROPIC_AUTH_TOKEN="lmstudio"
claude
```

이제 `claude` 가 시작하면서 `CLAUDE.md` 자동 로드 · subagent · MCP 도구 · 파일 작업 — **모든 기능**이 로컬 모델로 동작합니다. Anthropic 과금 없음.

#### 경로 B (CLI 선호자 · 이미 Ollama 쓰는 분) — Ollama + 번역 프록시

Ollama 를 유지하려면 Anthropic ↔ OpenAI 포맷을 **번역해주는 프록시** 가 하나 더 필요합니다. 대표적인 오픈소스 옵션:

- **`claude-code-router`** (GitHub: musistudio/claude-code-router) — npm 으로 설치, Ollama 를 백엔드로 지정
- **LiteLLM** (Python) — `litellm --model ollama/qwen3.5:9b --port 4000 --anthropic-compat`
- 또는 간단히 본인이 Express 로 래퍼 작성 (Messages API → Ollama `/api/chat` 변환)

대략의 흐름 (`claude-code-router` 예시):
```bash
# 1. Ollama 는 이미 실행 중
# 2. 라우터 설치
npm install -g @musistudio/claude-code-router

# 3. 설정 파일 ~/.claude-code-router/config.json 에 Ollama 프로바이더 등록
#    (상세는 해당 프로젝트 README 참조 — 버전별 스펙 변동 있음)

# 4. 라우터 시작
ccr start     # 기본 포트 3456

# 5. 별도 터미널에서 Claude Code 를 라우터로 연결
export ANTHROPIC_BASE_URL=http://localhost:3456
export ANTHROPIC_AUTH_TOKEN=local
claude
```

> 🚨 서드파티 프록시는 **업데이트 주기가 빠르고 Claude Code 버전과 호환이 깨질 수 있습니다**. 워크숍 당일·강의에 쓰지 말고 개인 환경에서 검증 후 사용하세요.

#### Claude Code `/model` 명령에 관한 참고

Claude Code 안에서 `/model` 을 치면 나오는 목록은 **기본적으로 Anthropic 호스팅 모델** (`claude-opus-4-7`, `claude-sonnet-4-6`, `claude-haiku-4-5`) 입니다. 위 경로 A/B 로 로컬 백엔드에 라우팅된 상태에서는 **로컬 서버가 노출한 모델명**이 `/model` 에 보입니다 — LM Studio 라면 앱에서 로드한 모델, 프록시라면 라우터 설정에 등록된 모델.

#### 편하게 쓰려면: alias 등록

```bash
# ~/.zshrc 또는 ~/.bashrc (LM Studio 기준)
alias claude-local='ANTHROPIC_BASE_URL=http://localhost:1234 ANTHROPIC_AUTH_TOKEN=lmstudio claude'
```

이후 `claude-local` 한 마디로 로컬 모드 진입.

#### 참고 자료
- LM Studio 공식 가이드 — https://lmstudio.ai/docs
- Claude Code 환경변수 레퍼런스 — https://docs.claude.com/en/docs/claude-code/settings
- [Running Google Gemma 3 locally with LM Studio Headless CLI and Claude Code](https://ai.georgeliu.com) (2026.04)

---

## 5. RA 팀 구성

### 역할별 모델 배정

```
[사용자] → 연구 주제
              ↓
┌──────────────────────────────────────────┐
│  Claude Code (Orchestrator)              │
│  = 팀장. 계획, 조율, 최종 판단           │
│  모델: qwen3.5:9b                        │
└──────┬──────────┬──────────┬─────────────┘
       ↓          ↓          ↓
  ┌─────────┐ ┌────────┐ ┌──────────────┐
  │ Scout + │ │Verifier│ │ Verifier 2   │
  │ Writer  │ │ (추론) │ │ (빠른 교차)  │
  │         │ │        │ │              │
  │ qwen    │ │deepseek│ │ gemma4       │
  │ 3.5:9b  │ │r1:14b  │ │ 26b (MoE)   │
  └─────────┘ └────────┘ └──────────────┘
    Qwen 계열   DeepSeek    Google 계열
                 계열
         ← 3개 계열 교차검증 →
```

### 프로젝트 폴더 구조

```bash
mkdir -p ~/my_research/{raw,output}
cd ~/my_research
```

### CLAUDE.md 작성

```markdown
# 프로젝트 맥락 문서

## 프로젝트
- 주제: [본인 주제]
- 방법론: [질적 / 양적 / 혼합]
- 현재 단계: [문헌검토 / 분석 / 작성]

## 출력 규칙
- 문체: 학술체 (~이다)
- 인용: APA 7th
- 언어: 한국어

## 금기
- 확인 안 된 논문 만들지 말 것 (hallucination 주의)
- 모르면 "확인 필요" 표기
- 인터뷰 원자료(raw/)는 수정 금지

## 팀 구성
- 주력 모델: qwen3.5:9b (문헌 검색, 분석, 작성)
- 검증 모델 1: deepseek-r1:14b (추론·논리 검증 — DeepSeek 계열)
- 검증 모델 2: gemma4:26b (빠른 교차 확인 — Google 계열)
- 검증 규칙: Writer가 작성한 모든 인용은 다른 계열 모델이 별도로 확인
```

### 실제 연구 파이프라인

Claude Code를 로컬 모델로 시작한 뒤, 순서대로 요청:

**1단계 — Scout (문헌 검색)**
```
"[연구 주제]에 대한 최근 5년간 주요 선행 연구를 정리해줘.
핵심 쟁점 3-5개, 각 쟁점별 대표 연구자와 주장을 포함해.
확인이 안 되는 내용은 '확인 필요'로 표시.
output/01_literature_scan.md에 저장해줘."
```

**2단계 — Writer (Literature Review 작성)**
```
"output/01_literature_scan.md를 바탕으로 literature review 초안을 작성해줘.
APA 7th 인용 형식, 학술체(~이다), 한국어.
output/02_literature_review.md에 저장해줘."
```

**3단계 — Verifier (교차 검증) ← DeepSeek R1 사용 (추론 특화)**

별도 터미널에서:
```bash
ollama run deepseek-r1:14b "아래 literature review에서:
1. 언급된 연구자와 논문이 실제로 존재하는지 확인해
2. 주장과 원문이 일치하는지 검토해
3. 논리적 비약이나 모순이 있는지 점검해
4. 의심스러운 부분은 '검증 실패: [이유]'로 표시해

$(cat output/02_literature_review.md)"
```

결과를 `output/03_verification.md`에 저장.

**3-b단계 — Verifier 2 (빠른 교차) ← Gemma4로 2차 확인 (선택)**

```bash
ollama run gemma4:26b-a4b-it-q4_K_M "아래 검증 결과를 읽고, 
놓친 문제가 있는지 한 번 더 확인해:

$(cat output/03_verification.md)"
```

**4단계 — Writer (Proposal 작성)**
```
"output/02_literature_review.md와 output/03_verification.md를 참고해서
연구 제안서(proposal) 초안을 작성해줘.
검증 실패로 표시된 부분은 제외하거나 수정해서.
output/04_proposal.md에 저장해줘."
```

**5단계 — Verifier (최종 검증)**

다시 gemma4로 proposal을 교차 검증.

### 결과물

```
output/
├── 01_literature_scan.md     ← Scout: 문헌 탐색
├── 02_literature_review.md   ← Writer: 리뷰 초안
├── 03_verification.md        ← Verifier: 교차 검증 (다른 모델)
├── 04_proposal.md            ← Writer: 제안서
└── 05_final_verification.md  ← Verifier: 최종 검증
```

---

## 6. 프레임워크 비교 (참고)

"Claude Code + Ollama 말고 다른 방법은 없나요?"

| 프레임워크 | Ollama 지원 | 연구 적합성 | 설정 복잡도 | 대학원생 현실성 |
|---|---|---|---|---|
| **Claude Code + Ollama** | 네이티브 | 높음 | 낮음 | 가장 현실적 |
| **CrewAI + Ollama** | 네이티브 | 높음 | 중간 | Python 경험 필요 |
| **AutoGen (MS)** | 네이티브 | 중간 | 중간 | 설정 파일 많음 |
| **LangGraph** | 간접 (래핑) | 낮음 | 높음 | 과도한 엔지니어링 |
| **Paperclip** | 미지원 | 없음 (코딩 전용) | 높음 | 연구 용도 부적합 |

**결론**: 로컬 모델로 연구 팀을 꾸리는 가장 현실적인 방법은 Claude Code + Ollama. 추가 프레임워크 없이, 이미 가지고 있는 도구만으로 충분합니다.

---

## 7. 트러블슈팅

**Q. Ollama 모델이 한국어를 못 알아듣는다**
A. `qwen3.5:9b` 이상이면 한국어 OK. Gemma 계열은 영어 위주 — 검증용으로는 충분하지만 한국어 글쓰기에는 Qwen 계열 권장.

**Q. Claude Code가 로컬 모델에 연결이 안 된다**
A. Ollama가 실행 중인지 확인: `ollama ps`. 모델이 하나도 안 보이면 `ollama run qwen3.5:9b`로 먼저 띄우기.

**Q. 첫 응답이 1-2분 넘게 안 온다**
A. 정상입니다. 모델을 디스크에서 메모리로 올리는 시간입니다. 모델 크기별 예상 로딩 시간:
- qwen3.5:9b (6.6GB): ~1-2분
- deepseek-r1:14b (9GB): ~2-3분
- gemma4:26b (17GB): ~3-5분

첫 응답 이후에는 빠릅니다 (메모리 상주). Ollama는 기본 5분간 모델을 메모리에 유지합니다. 5분 이상 안 쓰면 자동으로 내려가고, 다시 호출하면 또 로딩 시간이 걸립니다.

검증 단계에서 다른 모델(deepseek, gemma4)을 처음 호출할 때도 동일한 로딩 대기가 발생합니다. 파이프라인 전체로 보면 모델 전환 시 각각 1-3분의 대기가 추가된다고 생각하세요.

**Q. 메모리가 부족하다 (swap 발생)**
A. 두 모델을 동시에 올리지 말 것. Scout/Writer 작업 끝나면 `ollama stop qwen3.5:9b` 후 Verifier 모델 실행.

**Q. 로컬 모델 결과가 클라우드 모델보다 많이 떨어진다**
A. 기대치 조정 필요. 로컬 모델은 "초안 + 구조화"에 적합. 최종 품질 검수는 Claude Pro(월 $20) 한 번 쓰는 게 현실적.

---

*작성: 2026.04.15 | 이 문서는 워크숍 실습 가이드의 일부입니다.*
*로컬 모델 상세: `appendix/01_로컬AI_무료_활용_가이드.md` 참조*
