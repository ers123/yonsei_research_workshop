# RA 팀 Tier별 구성 가이드

> 비용에 따른 연구 도구 구성과 기대 품질
> 검증일: 2026-04-15 (웹검색 기반 최신 가격 확인)

---

## 한눈에 보기

| Tier | 월 비용 | 구성 | 기대 수준 |
|---|---|---|---|
| **Free** | $0 | Ollama 로컬 모델 only | 자료 정리·태깅. 웹검색 불가. |
| **Standard** | $20 | Claude Pro + 로컬 검증 | 웹검색 + 선행연구 + RQ 도출 + 교차검증 |
| **Full** | $220-420 | Claude Max + Perplexity Max + Codex | 연구실 수준 자동화. 3사 모델 교차검증. |

---

## Tier 1: Free ($0/월)

### 구성
```
Ollama 로컬 모델 (harness: Claude Code 또는 Codex CLI)
├── Writer: gemma4 E4B (4B) 또는 qwen3.5:9b
├── Verifier: deepseek-r1:14b (다른 계열)
└── Embedding: nomic-embed-text (RAG용)
```

### 할 수 있는 것
- 이미 가진 자료(PDF, 전사본) 요약·정리
- codebook 기반 텍스트 분류·태깅
- IRB 민감자료 처리 (외부 전송 없음)
- 교차검증 (다른 계열 모델 간)

### 할 수 없는 것
- 웹검색 (새 논문 탐색 불가)
- 긴 문서 전체 분석 (context window 제한)
- 복잡한 추론·비판적 분석

### 적합한 사용자
- 예산 없는 대학원생
- IRB 민감자료 다루는 연구자
- 오프라인 작업이 필요한 경우

---

## Tier 2: Standard ($20/월)

### 구성
```
Claude Pro $20/월 (harness: Claude Code)
├── Orchestrator: Claude Sonnet/Opus (클라우드)
│   ├── 웹검색 내장
│   ├── 파일 읽기/쓰기
│   └── bash로 로컬 모델 호출
├── Verifier 1: deepseek-r1:14b (로컬, $0)
├── Verifier 2: gemma4 E4B (로컬, $0)
└── 출처 검증: Claude가 URL 직접 방문
```

### 할 수 있는 것
- 웹검색 기반 선행연구 탐색
- 논문 존재 여부 URL 직접 확인
- 선행연구 정리 + Research Gap 도출
- 로컬 모델로 교차검증 (무제한, 무료)
- Research Question 도출
- CLAUDE.md 기반 맥락 유지

### 제한사항
- 5시간 사용량 제한 (리셋 후 재사용)
- 긴 논문 전체 분석은 어려움 (context 제한)
- 동시 에이전트 제한

### 적합한 사용자
- 대부분의 대학원생 (최적 가성비)
- 석사 논문 수준 연구

### 실제 데모 결과 (본 워크숍에서 시연)
- 주제 후보 5개 생성 + 선행연구 14건 정리 + 교차검증 + RQ 도출
- 인용 논문 5건 URL 직접 방문하여 존재 확인 완료
- 로컬 검증 비용: $0 (무한 반복 가능)

---

## Tier 3: Full ($220-420/월)

### 구성
```
Claude Max $100-200/월
├── 1M context window — 논문 10편을 통째로 읽고 cross-reference
├── Subagent 자동 병렬 처리
├── 우선 접근: Opus 4.6, 신규 모델
└── Claude Code 포함

Perplexity Max $200/월
├── Computer Agent — 19개 모델 오케스트레이션
├── 브라우저 자동 탐색 (NTIS, Google Scholar, PubMed)
├── 10,000 크레딧/월
└── Comet 브라우저 (맥락 인식 웹 탐색)

Codex (ChatGPT Plus $20 포함)
├── OpenAI 계열 독립 검증 (Claude와 다른 편향)
├── 로컬 실행 가능 (--oss 플래그)
└── Rust 기반 CLI

로컬 모델 ($0)
├── DeepSeek R1 14B — 추론 검증
└── Gemma4 — 빠른 교차 확인
```

### 할 수 있는 것
- **3사 교차검증**: Anthropic(Claude) + OpenAI(Codex) + 로컬(DeepSeek/Gemma) → hallucination 생존 극히 어려움
- **Perplexity Computer Agent**: NTIS, Google Scholar를 브라우저처럼 자동 탐색. 검색어 입력 불필요.
- **1M context**: 논문 전체를 올려서 분석. 요약이 아닌 원문 기반 추론.
- **병렬 처리**: 여러 에이전트가 동시에 다른 논문을 분석
- **연구 제안서 수준의 산출물**: 서론, 선행연구, 방법론, 예상 결과까지

### 비용 분석

| 서비스 | 가격 | 핵심 가치 |
|---|---|---|
| Claude Max 5x | $100/월 | 1M context, 우선 접근, 5x 사용량 |
| Claude Max 20x | $200/월 | 위 + 20x 사용량 (중단 없는 작업) |
| Perplexity Max | $200/월 | Computer Agent, 19개 모델, 자동 탐색 |
| ChatGPT Plus (Codex 포함) | $20/월 | OpenAI 계열 독립 검증 |
| 로컬 모델 | $0 | 무제한 검증 |
| **합계 (최소)** | **$220/월** | Claude Max 5x + Codex |
| **합계 (최대)** | **$420/월** | Claude Max 20x + Perplexity Max + Codex |

### 적합한 사용자
- 연구비가 있는 박사과정 / 교수
- 대량 논문 분석이 필요한 체계적 문헌검토
- 시간이 돈보다 귀한 경우

---

## 비용 대비 품질 점프

```
품질
  ▲
  │                              ┌─── Full ($220-420)
  │                         ┌────┘    연구실 수준
  │                    ┌────┘
  │               ┌────┘
  │          ┌────┘
  │     ┌────┘              ← $0→$20 구간이 가장 큰 점프
  │┌────┘
  ├┘
  │ Free ($0)
  └──────────────────────────────────────→ 비용
    $0    $20         $100   $200   $420
```

> **핵심 메시지**: $0과 $20 사이의 점프가 가장 크다.
> 웹검색, 긴 맥락, 도구 호출이 한꺼번에 열린다.
> $20 이후는 점진적 향상 — 더 길고, 더 깊고, 더 빠를 뿐.

---

## 검증 전략 비교

| | Free | Standard | Full |
|---|---|---|---|
| 교차검증 모델 수 | 2 (로컬 간) | 3 (Claude + 로컬 2개) | 4+ (3사 + 로컬) |
| 출처 URL 확인 | 불가 | Claude가 직접 방문 | Claude + Perplexity |
| 논문 원문 대조 | 불가 | 요약 기반 | 1M context로 원문 전체 |
| Hallucination 생존율 | 중간 | 낮음 | 극히 낮음 |

---

## Gemma4 E4B — 경량 검증 모델로서의 가치

Gemma4 E4B (4B)는 DeepSeek R1 14B보다 작지만, 본 실험에서 더 깊은 비판을 제공했다:

**DeepSeek R1 14B가 잡은 것:**
- Gap 3의 모호함
- 인용 출처 부재 (요약본 한계)
- 56.9% 수치의 신뢰성 의문

**Gemma4 E4B가 추가로 잡은 것:**
- "식품불안정이라는 다차원적 사회 문제를 AI라는 단일 기술적 해결책으로 접근하려는 전제가 지나치게 단순함"
- TAM이 '기술 수용'에만 초점 → '행동 변화'와 '정책적 개입'까지 확장 필요
- Digital Divide를 '접근성'뿐 아니라 'Capability Divide'와 'Outcome Divide'까지 포함해야 함

**시사점**: 모델 크기 ≠ 검증 품질. 4B 모델도 다른 관점에서 유의미한 비판이 가능하다. 16GB 노트북에서도 의미 있는 교차검증이 된다.

---

## 참고 자료

### 가격 출처 (2026년 4월 확인)
- [Claude Max Plan](https://claude.com/pricing/max) — $100/월 (5x), $200/월 (20x)
- [Perplexity Pricing](https://www.finout.io/blog/perplexity-pricing-in-2026) — Pro $20/월, Max $200/월
- [Perplexity Computer](https://www.buildfastwithai.com/blogs/what-is-perplexity-computer) — 19개 모델 오케스트레이션, 10,000 크레딧/월
- [Codex CLI Pricing](https://developers.openai.com/codex/pricing) — ChatGPT Plus $20에 포함
- [Claude Code Pricing Guide](https://www.ssdnodes.com/blog/claude-code-pricing-in-2026-every-plan-explained-pro-max-api-teams/)

### 설치 참고
- 로컬 모델 세팅: `hands_on/ra_team_setup.md`
- 강사 환경 레퍼런스: `hands_on/reference_setup_m4_32gb.md`
- 실습 시나리오: `hands_on/scenario_comparison/TODO.md`

---

*작성: 2026-04-15 | 이 문서는 워크숍 실습 가이드의 일부입니다.*
