# Track C — 연구 조수 팀 만들기

**시간**: 45분  
**목표**: Claude Code로 연구 파이프라인을 돌리고, 다른 계열 모델들이 교차검증하는 구조를 체험한다.

---

## 핵심 메시지

> 프롬프트 시대: "AI야 논문 써줘" → 결과를 그냥 받음
> 맥락 시대: "이 맥락에서 논문 써줘" → 좀 더 나은 결과
> **하네스 시대**: "써주고, 다른 모델이 공격하고, 살아남은 것만 채택"
> → 반증가능성(falsifiability)이 구조에 내장된다

---

## 왜 이걸 하는가

하나의 AI에 모든 걸 시키면:
- 같은 모델이 쓰고 같은 모델이 검증 → **같은 편향, 같은 hallucination**
- 결과가 맞는지 사람이 전부 확인해야 함

다른 계열 모델로 교차검증하면:
- **"서로 다른 방식으로 틀린다"** → 교차점에서 진짜 오류가 드러남
- 검증은 로컬 모델로 **무제한, 무료**

---

## 실습 구조 (45분)

```
[Step 0] 환경 확인 ─────────────── 5분
[Step 1] CLAUDE.md 작성 ─────────── 5분
[Step 2] 연구 파이프라인 실행 ───── 15분
[Step 3] 교차검증 (로컬 모델) ──── 10분
[Step 4] 결과 비교 + 토론 ──────── 10분
```

---

## Step 0 — 환경 확인 (5분)

### 필수 도구

```bash
# Claude Code 확인
claude --version
# → 버전 번호 나오면 OK

# Ollama 확인
ollama list
# → 모델 1개 이상 보이면 OK

# 없으면 지금 설치:
# macOS: brew install ollama && ollama pull gemma4
# Windows: https://ollama.com 에서 설치 후 ollama pull gemma4
```

### 추가 도구 (있으면 더 좋음)

```bash
# Codex CLI (OpenAI 계열 교차검증)
codex --version

# Gemini CLI (Google 계열 교차검증)
gemini --version
```

### 모델 추천 (RAM 기준)

| RAM | 모델 | 설치 |
|---|---|---|
| **8-16GB** | `gemma4` (E4B, 4B) | `ollama pull gemma4` |
| **32GB** | `gemma4` + `deepseek-r1:14b` | 위 + `ollama pull deepseek-r1:14b` |

**참고**: 첫 모델 로딩에 1-3분 소요됩니다 (디스크→메모리). 정상입니다.

---

## Step 1 — CLAUDE.md 작성 (5분)

프로젝트 폴더를 만들고 맥락 문서를 작성합니다:

```bash
mkdir -p ~/workshop_team_demo/output
cd ~/workshop_team_demo
```

아래 내용을 `CLAUDE.md`로 저장하세요. **본인 연구 주제로 바꿔도 됩니다.**

```markdown
# 프로젝트 맥락 문서

## 소속
연세대학교 생활과학대학 대학원 (석사과정)

## 연구 분야
[본인 분야 — 식품영양 / 노화과학 / 섬유패션 / 주거복지 / 디자인 등]

## 현재 단계
연구과제 선정 전 — 주제 탐색 중

## 출력 규칙
- 문체: 학술체 (~이다)
- 인용: APA 7th
- 언어: 한국어
- 확인 안 된 논문은 "확인 필요" 표기

## 검증 규칙
- 작성 후 반드시 다른 모델로 교차검증 실행
- 검증 실패 항목은 최종 결과에서 제외 또는 수정
```

---

## Step 2 — 연구 파이프라인 실행 (15분)

Claude Code를 시작합니다:

```bash
cd ~/workshop_team_demo
claude
```

아래 프롬프트를 입력:

```
나는 연세대학교 생활과학대학 대학원생이야.

아래 순서대로 진행해줘:

1. 내 분야에서 2026년 현재 석사 논문 주제 3개를 제안해줘.
   각 주제: 제목 + 시의성 한 줄 + 예상 방법론.
   output/01_topic_candidates.md에 저장.

2. 가장 실현 가능한 주제 1개를 골라서 선행연구 5건을 정리해줘.
   각 논문: 저자, 연도, 핵심 발견, 출처 URL.
   확인 안 되는 건 "확인 필요" 표시.
   output/02_literature_review.md에 저장.

3. 연구 갭 2개를 도출하고, Research Question을 제안해줘.
   output/03_research_questions.md에 저장.
```

→ Claude Code가 CLAUDE.md를 읽고, 웹검색으로 논문을 찾고, 파일로 저장합니다.

---

## Step 3 — 교차검증: 이게 하이라이트 (10분)

Claude Code가 작성을 마치면, **다른 모델에게 공격시킵니다.**

### 방법 A: Claude Code 안에서 bash로 로컬 모델 호출

```
output/03_research_questions.md를 읽고,
bash로 ollama run gemma4를 호출해서 아래 검증을 시켜줘:

"아래 연구 설계의 논리적 문제를 찾아줘.
의심스러운 부분은 '검증 실패: [이유]'로 표시해."

검증 결과를 output/04_verification_gemma4.md에 저장해줘.
```

### 방법 B: Codex가 있으면 (OpenAI 계열)

```bash
# 별도 터미널에서
codex exec "아래 연구 설계의 논리적 문제를 찾아줘.
의심스러운 부분은 '검증 실패: [이유]'로 표시:
$(cat output/03_research_questions.md)" > output/04_verification_codex.md
```

### 방법 C: Gemini가 있으면 (Google 계열)

```bash
echo "$(cat output/03_research_questions.md)

위 연구 설계의 논리적 문제를 찾아줘.
의심스러운 부분은 '검증 실패: [이유]'로 표시해." | gemini > output/04_verification_gemini.md
```

### 왜 여러 모델을 쓰나?

| 모델 | 계열 | 편향 | 잘 잡는 것 |
|---|---|---|---|
| Gemma4 | Google | 개념적 | "전제 자체가 단순하다" |
| DeepSeek R1 | DeepSeek | 추론 | "논리 비약이 있다" |
| Codex (GPT) | OpenAI | 방법론 | "표본이 부족하다, 개념이 중복된다" |
| Gemini | Google Cloud | 실행 | "선택편향이 있다, 횡단연구 한계" |

**모델마다 다른 걸 잡는다. 하나만 썼으면 놓쳤을 문제가 여러 개를 합치면 드러난다.**

---

## Step 4 — 결과 비교 + 토론 (10분)

### 결과물 확인

```
output/
├── 01_topic_candidates.md          ← Claude 작성
├── 02_literature_review.md         ← Claude 작성 (웹검색)
├── 03_research_questions.md        ← Claude 작성
├── 04_verification_gemma4.md       ← Gemma4 검증
├── 04_verification_codex.md        ← Codex 검증 (있으면)
└── 04_verification_gemini.md       ← Gemini 검증 (있으면)
```

### 비교 포인트

1. **어떤 모델이 가장 날카로운 비판을 했나?**
2. **3개 이상 모델이 공통으로 지적한 문제는?** → 이게 진짜 약점
3. **1개 모델만 지적한 문제는?** → 해당 모델의 편향일 수도, 유일하게 잡은 것일 수도
4. **검증 결과를 반영하면 RQ가 어떻게 바뀌어야 하나?**

### 토론 질문

- "이 과정 없이 Claude 결과를 그냥 썼으면 어떤 문제가 생겼을까?"
- "동료 검토(peer review)와 비교하면 무엇이 같고 무엇이 다른가?"
- "반증가능성(falsifiability)이 연구 설계에 왜 중요한가?"

---

## 핵심 정리

### 비용 구조

| 역할 | 도구 | 비용 |
|---|---|---|
| Writer (작성) | Claude Pro | $20/월에 포함 |
| Verifier (검증) | Ollama 로컬 모델 | **$0** — 무한 반복 |
| Verifier 2 | Codex CLI | ChatGPT Plus 포함 |
| Verifier 3 | Gemini CLI | 무료 |

> **검증은 공짜다. 로컬 모델로 무한히 돌릴 수 있다.**
> 비싼 모델은 판단에만 쓰고, 반복 검증은 무료 모델에 맡겨라.

### 이 구조가 "작년과 다른 점"

| 작년 (Tool Hopping) | 올해 (Harness Engineering) |
|---|---|
| 도구 6개를 하나씩 수동 전환 | 하나의 시스템에서 자동 실행 |
| 도구 바꿀 때마다 맥락 리셋 | CLAUDE.md 한 번 쓰면 유지 |
| 검증? 사람이 눈으로 | 다른 모델이 자동 교차검증 |
| 반복 불가 | 같은 파이프라인을 다른 주제에 재사용 |
| AI가 뭘 했는지 불투명 | 파이프라인 투명성 기록 |

---

## (심화) 완전 무료로 하려면

Claude Pro 없이, 로컬 모델만으로도 가능합니다:

```bash
# Ollama + Claude Code 연결 (무료)
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_BASE_URL=http://localhost:11434
claude --model gemma4
```

**제한사항:**
- 웹검색 안 됨 → 이미 가진 자료 정리·분류에 적합
- 속도 느림 → 간단한 작업에 적합
- IRB 민감자료 처리에는 오히려 이 방법이 필수 (외부 전송 불가)

상세: `hands_on/ra_team_setup.md` 참조

---

## (심화) 연구비가 있다면

| Tier | 월 비용 | 추가되는 것 |
|---|---|---|
| Standard | $20 | 웹검색, 긴 맥락, 도구 호출 |
| Full | $220-420 | 1M context, 3사 교차검증, 자동 탐색 |

상세: `hands_on/ra_team_tiers.md` 참조

---

## 체크포인트

- [ ] Claude Code가 CLAUDE.md를 자동으로 읽었다
- [ ] 연구 파이프라인(주제→선행연구→RQ)이 파일로 저장되었다
- [ ] 1개 이상 다른 모델로 교차검증을 실행했다
- [ ] 검증 결과에서 "검증 실패" 항목을 1개 이상 발견했다
- [ ] "왜 여러 모델이 필요한가"를 한 문장으로 설명할 수 있다

---

## 함정 피하기

- **검증 없이 결과를 그냥 쓰지 마세요.** AI가 빠르게 내놓으니 그냥 받고 싶지만, 그게 "검증부채(Verification Debt)"입니다.
- **로컬 모델 첫 호출은 1-3분 걸립니다.** 모델을 메모리에 올리는 시간. 두 번째부터 빠름.
- **로컬 모델의 한국어가 어색해도 괜찮습니다.** 글쓰기가 아니라 검증이 목적. "이상한 점을 찾아라"는 지시에는 작은 모델도 유효.
- **4B 모델이 14B보다 나을 때도 있습니다.** 크기 ≠ 품질. 실험에서 Gemma4 E4B(4B)가 DeepSeek R1(14B)보다 더 깊은 개념적 비판을 제공했습니다.

---

## 참고 자료

- 로컬 모델 세팅: `hands_on/ra_team_setup.md`
- Tier별 구성: `hands_on/ra_team_tiers.md`
- 강사 환경 레퍼런스: `hands_on/reference_setup_m4_32gb.md`
- Scenario B 실제 결과: `hands_on/scenario_comparison/scenario_b/`
- Claude Code + Ollama 연결: [YouTube 가이드](https://www.youtube.com/watch?v=eAleab2cL3I)
- Running Claude Code for Free: `appendix/01_로컬AI_무료_활용_가이드.md`

---

*작성: 2026-04-15 | CC BY-NC-SA 4.0*
