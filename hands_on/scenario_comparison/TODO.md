# RA 팀 시나리오 A/B 비교 실습

## 목표
같은 연구 파이프라인을 **Scenario A (완전 무료)** vs **Scenario B (Claude Pro)** 로 돌려서 결과를 비교한다.

파이프라인: 연구과제 선정 → 선행연구 탐색 → Research Question 도출

---

## 연구 분야
연세대학교 생활과학대학 심바이오틱라이프텍연구원 관련 분야에서 선택.
- 노화과학, 식품영양, 섬유패션, 휴먼라이프, 주거복지, 디자인 등

---

## Scenario A: 완전 무료 (로컬 모델 Only)

### 세팅 방법

```bash
# 1. 새 터미널을 연다 (이 세션과 별도)

# 2. 프로젝트 폴더로 이동
cd ~/Downloads/work/Yonsei/0424_research_workshop/hands_on/scenario_comparison

# 3. Ollama가 실행 중인지 확인
ollama ps
# 아무것도 안 뜨면: ollama serve &

# 4. Claude Code를 로컬 모델로 시작
ANTHROPIC_BASE_URL=http://localhost:11434/v1 claude

# 5. Claude Code 안에서 모델 선택
/model qwen3.5:9b
```

### 진행 순서

아래 프롬프트를 **순서대로** 입력:

**Step 1 — 연구과제 탐색**
```
나는 연세대학교 생활과학대학 대학원생이야.
심바이오틱라이프텍연구원의 연구 분야(노화과학, 식품영양, 섬유패션, 
휴먼라이프, 주거복지, 디자인) 중에서 2026년 현재 학술적으로 
의미 있고 실현 가능한 석사 논문 주제 5개를 제안해줘.

각 주제에 대해:
1. 제목 (한국어)
2. 왜 지금 이 주제인가 (시의성)
3. 예상 방법론
4. 데이터 접근 가능성

결과를 scenario_a/01_topic_candidates.md에 저장해줘.
```

**Step 2 — 주제 선택 + 선행연구 탐색**
```
01_topic_candidates.md에서 가장 실현 가능한 주제 1개를 골라줘.
선택 기준: 데이터 접근성 + 학술적 기여 + 석사 수준 적합성.

선택한 주제에 대해 선행연구 동향을 정리해줘:
1. 핵심 키워드 5개
2. 주요 선행연구 10건 (저자, 연도, 핵심 발견)
3. 연구 갭(gap) 3개
4. 확인이 안 되는 내용은 '확인 필요'로 표시

scenario_a/02_literature_review.md에 저장해줘.
```

**Step 3 — 검증 (다른 모델로)**
```
터미널에서 직접 실행:

ollama run deepseek-r1:14b "아래 선행연구 정리에서:
1. 언급된 논문이 실제로 존재할 가능성을 평가해
2. 논리적 비약이 있는지 확인해
3. 의심스러운 부분은 '검증 실패: [이유]'로 표시해

$(cat scenario_a/02_literature_review.md)" > scenario_a/03_verification.md
```

**Step 4 — Research Question 도출**
```
02_literature_review.md와 03_verification.md를 읽고,
검증을 통과한 내용만 기반으로 Research Question을 도출해줘.

형식:
1. 메인 RQ 1개
2. 서브 RQ 2-3개
3. 각 RQ의 근거 (어떤 gap에서 나왔는지)
4. 예상 기여 (이론적 / 실천적)

scenario_a/04_research_questions.md에 저장해줘.
```

### 예상 결과물
```
scenario_a/
├── 01_topic_candidates.md      ← 주제 후보 5개
├── 02_literature_review.md     ← 선행연구 정리
├── 03_verification.md          ← DeepSeek 교차검증
└── 04_research_questions.md    ← RQ 도출
```

---

## Scenario B: Claude Pro ($20)

### 세팅 방법

```bash
# 현재 세션(Claude Code Opus/Sonnet)에서 바로 진행
# 또는 새 터미널에서:
cd ~/Downloads/work/Yonsei/0424_research_workshop/hands_on/scenario_comparison
claude
# /model sonnet 또는 기본 모델 사용
```

### 진행 순서

**동일한 4단계 프롬프트**를 사용하되, 저장 경로만 `scenario_b/`로 변경.

- Step 1 → `scenario_b/01_topic_candidates.md`
- Step 2 → `scenario_b/02_literature_review.md`
- Step 3 → 검증은 동일하게 `ollama run deepseek-r1:14b` 사용 (Verifier는 항상 로컬)
- Step 4 → `scenario_b/04_research_questions.md`

### 예상 결과물
```
scenario_b/
├── 01_topic_candidates.md
├── 02_literature_review.md
├── 03_verification.md
└── 04_research_questions.md
```

---

## 비교 포인트

| 관점 | 확인할 것 |
|---|---|
| **주제 선택** | A와 B가 같은 주제를 골랐나? 다르다면 왜? |
| **선행연구 품질** | hallucination 비율 차이. 실제 존재하는 논문 비율. |
| **검증 결과** | 같은 Verifier(DeepSeek)가 A와 B의 결과를 각각 어떻게 평가했나? |
| **RQ 품질** | 구체성, 실현 가능성, 학술적 기여도 |
| **비용** | A=$0 vs B=$20/월 — 품질 차이가 그 가격 가치가 있나? |

---

## 체크리스트

### Scenario A
- [ ] Ollama 실행 확인
- [ ] Claude Code를 로컬 모델로 시작
- [ ] /model qwen3.5:9b 설정
- [ ] Step 1-4 순서대로 진행
- [ ] DeepSeek R1으로 검증 실행
- [ ] 결과물 4개 파일 생성 확인

### Scenario B  
- [ ] Claude Code 기본(클라우드) 세션 시작
- [ ] Step 1-4 순서대로 진행 (경로만 scenario_b/)
- [ ] DeepSeek R1으로 검증 실행
- [ ] 결과물 4개 파일 생성 확인

### 비교
- [ ] A/B 결과물을 나란히 비교
- [ ] 비교 소감을 comparison_notes.md에 기록

---

*이 파일은 워크숍 실습 가이드의 일부입니다.*
*RA 팀 세팅 상세: `hands_on/ra_team_setup.md` 참조*
