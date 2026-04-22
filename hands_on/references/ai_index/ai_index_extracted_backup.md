# AI Index Report 2026 — 추출본 (Top Takeaways + Chapter 1.1)

> **출처**: Stanford HAI, *Artificial Intelligence Index Report 2026*
> **원본**: `ai_index_report_2026.pdf` (423 pages, 37 MB)
> **추출 범위**: Top Takeaways (pp. 9-11) + Chapter 1. Research and Development — Highlights & 1.1 Notable AI Models (pp. 13-22)
> **형식 규칙**: 본문은 평문 마크다운, 표는 마크다운 표, 차트/지도는 `[Figure X.Y: 설명 + 주요 수치]` 캡션
>
> 본 문서는 워크숍 Track B 실습용으로 준비된 **수동 큐레이션 추출본**입니다. 실제 Claude Code가 생성하는 결과물도 유사한 형태를 목표로 합니다.

---

## Top Takeaways (p. 9-11)

### 1. AI capability is not plateauing — 가속 중

Industry produced **over 90%** of notable frontier models in 2025. SWE-bench Verified에서 성능이 **60% → 거의 100%** (human baseline 대비)로 1년 만에 상승. 조직 도입률 **88%**, 대학생 **5명 중 4명**이 generative AI 사용.

### 2. The U.S.-China AI model performance gap has effectively closed

2025년 초 이후 미국·중국 모델이 여러 차례 선두 교체. 2025년 2월 DeepSeek-R1이 일시적으로 최상위 미국 모델과 동급. 2026년 3월 기준 Anthropic 최상위 모델이 **단 2.7%** 앞섬.

- 미국: top-tier 모델 수, high-impact 특허 우위
- 중국: publication 수, citation, patent 총량, 산업용 로봇 설치 우위
- **한국: AI 특허 per capita 세계 1위** ← 워크숍 참조 포인트

### 3. The United States hosts the most AI data centers

- 미국 데이터센터 수: **5,427개** (2위 국가 대비 10배 이상)
- 거의 모든 최상급 AI 칩은 TSMC(대만) 한 곳에서 제조
- 2025년 TSMC-US 확장 가동 시작

### 4. "Jagged frontier of AI"

- Gemini Deep Think: IMO 금메달
- 그러나 최상위 모델이 아날로그 시계 읽기 정확도 **50.1%**
- OSWorld agent 성공률: **12% → 약 66%** (1년)
- 구조화된 벤치마크에서도 여전히 3회 중 1회 실패

### 5. Robots still fail at most household tasks

- 가정 task 성공률: **12%**
- RLBench (시뮬레이션): **89.4%**
- 통제 환경과 실제 환경 격차 큼

### 6. Responsible AI is not keeping pace

- Documented AI incidents: **233 (2024) → 362 (2025)**
- Capability 벤치마크는 거의 모든 frontier lab 보고, responsible AI 벤치마크 보고는 드문 상태
- 한 responsible AI 차원(safety)을 개선하면 다른 차원(accuracy)이 저하되는 경향 관찰

### 7. U.S. leads in AI investment, but talent inflow is declining

- 미국 private AI investment 2025: **$285.9B** (중국의 23배, 중국 $12.4B)
- 단 중국은 정부 유도 자금으로 민간 투자 지표만으로 보면 과소평가됨
- 미국 새 AI 스타트업 자금 조달: **1,953개** (2025, 2위 국가의 10배 이상)
- 그러나 미국으로의 AI 연구자·개발자 이주는 **2017 대비 89% 감소**, 지난 1년만 **80% 감소**

### 8. AI adoption is spreading at historic speed

- Generative AI가 3년 만에 **53% 인구 도입률** 도달 — PC나 인터넷보다 빠름
- 국가별: 싱가포르 **61%**, UAE **54%**, 미국 24위 **28.3%**
- 미국 소비자 generative AI 가치 추정치: **$172B 연간** (2026 초 기준)
- 사용자당 중위 가치: 2025→2026 3배 증가

### 9. Productivity gains appear alongside entry-level employment decline

- Customer support / 소프트웨어 개발 생산성 **14%–26%** 상승
- 판단 요구 task에서는 효과가 약하거나 부정적
- AI agent 배포: 대부분 비즈니스 함수에서 한 자리 수
- 미국 22-25세 소프트웨어 개발자 고용 **2024 대비 약 20% 감소** (더 높은 연령대는 증가)

### 10. AI's environmental footprint is expanding

- Grok 4 training 배출량 추정: **72,816 tons CO₂eq**
- AI data center 전력 용량: **29.6 GW** (뉴욕주 피크 수요 수준)
- GPT-4o inference 연간 물 사용량 추정치가 **1,200만 명** 식수 수요 초과 가능

### 11. AI models for science can outperform human scientists — but not always

- ChemBench에서 frontier 모델이 화학자 평균 상회
- 그러나 astrophysics replication 점수 **20% 미만**, Earth observation 질문 **33%**
- **111M 파라미터 MSAPairformer**가 ProteinGym 선두 방법 이김
- **200M GPN-Star**가 200배 큰 모델보다 우수한 genomics 성능
- Science용 foundation model은 cross-sector 협업이 주류 (vs 일반 AI는 산업 주도)

### 12. AI is transforming clinical care, but evidence is limited

- 진료 노트 자동 생성 도구 2025년 대규모 도입
- 의사 보고: 노트 작성 시간 최대 **83% 감소**, 번아웃 유의 감소
- 500+ 임상 AI 연구 리뷰 결과: **약 절반**이 실환자 데이터가 아닌 시험문제식 데이터, **단 5%**만이 실제 임상 데이터 사용

---

## Chapter 1. Research and Development — Highlights (p. 14-15)

### Highlight 1. Industry produced over 90% of notable AI models in 2025

최상위 모델일수록 투명성 저하 — OpenAI, Anthropic, Google 일부 모델은 training code, parameter count, dataset size, training duration 모두 비공개.

### Highlight 2. China leads in research, U.S. leads in notable model development

- 중국: publication 수, citations, patent grants 우위
- 미국: 2025년 notable 모델 **50개**, 중국 **30개**
- **한국: AI 특허 per capita 세계 1위**
- 중국의 top 100 most-cited AI papers 점유율: 2021년 **33개** → 2024년 **41개**

### Highlight 3. Reported parameters held in the trillions as disclosure dropped

- 파라미터 수는 약 1조 근처에서 3년째 정체
- Frontier lab의 공식 보고는 중단됨
- Training compute는 독립 추정으로 여전히 증가 중

### Highlight 4. Synthetic data is still not replacing real data in pre-training

- 그러나 data quality + post-training 기법이 유망
- **OLMo 3.1 Think 32B**: Grok 4 대비 거의 **90배 적은 파라미터**로 여러 벤치마크 comparable 달성 (pruning, deduplication, curation 활용)

### Highlight 5. Global AI compute capacity grew 3.3x per year since 2022

- 2025년 총 용량: **17.1M H100-equivalents**
- Nvidia 점유율: **60% 이상**
- Google, Amazon이 상당 부분 공급, Huawei 작지만 증가
- 성장 동력: 하이퍼스케일러 데이터센터 확장 + frontier 훈련·추론 수요

### Highlight 6. U.S. leads in AI data centers, TSMC fabricates the majority of chips

- 미국: **5,427 데이터센터** (2위 국가의 10배+)
- 거의 모든 주요 AI 칩: TSMC 제조
- 2025년 TSMC-미국 확장 가동 시작

### Highlight 7. AI's environmental footprint increases

- Grok 4: **72,816 tons CO₂eq** 추정 training 배출
- AI data center power capacity: **29.6 GW**
- GPT-4o inference water use 추정치: **1,200만 명** 식수 수요 초과 가능

### Highlight 8. Open-source AI development continues to scale

- GitHub + Hugging Face 합산: **5.6M projects**
- Hugging Face 업로드: 2023 대비 3배
- 미국 기반 프로젝트 engagement 1위: 10-star 이상 프로젝트 누적 **30M GitHub stars**

### Highlight 9. The number of AI researchers and developers moving to the U.S. dropped 89% since 2017

- 지난 1년만 **80% 감소**
- 미국은 여전히 최다 AI 인재 보유국이지만, 10년 내 신규 유입률 최저

### Highlight 10. AI talent map is shifting, gender gaps remain entrenched

- **Switzerland, Singapore**: AI 연구자·개발자 per capita 세계 선두
- 상대적으로 높은 여성 비율: **Saudi Arabia 32.3%, Canada 29.6%, Australia 30.1%**
- 그러나 어느 국가도 gender parity 근접하지 못함

---

## 1.1 Notable AI Models (p. 16-22)

### Context (p. 16)

이 섹션은 Epoch AI의 notable model dataset을 바탕으로 **어디서**, **어떻게**, **무엇으로** 프런티어 모델을 만드는지를 추적한다. "Notable"의 기준: state-of-the-art 진전, 역사적 중요성, 높은 citation rate. 수동 큐레이션이므로 전체 AI 모델의 censuses가 아니며 **패턴**으로 해석되어야 함.

### By National Affiliation (p. 16-17)

**Figure 1.1.1 — Number of notable AI models by select geographic areas, 2025**

| 국가 | 2025년 notable 모델 수 |
|---|---|
| United States | 50 |
| China | 30 |
| South Korea | 5 |
| Canada | 1 |
| France | 1 |
| Hong Kong | 1 |
| United Kingdom | 1 |

*(Source: Epoch AI, 2026 | Chart: 2026 AI Index report)*

**본문 요약 (p. 16)**: Notable 모델 생산은 소수 국가에 집중. 역사적으로 미국이 최대, 중국이 2위. 2025년에도 패턴 유지. 모든 주요 지역에서 전년 대비 감소.

**Figure 1.1.2 — Number of notable AI models by select geographic areas, 2003-25 (time series)**

- 종점 레이블 (2025): United States = 50, China = 30, Europe = 2
- 추세: 미국 2015년 이후 급상승, 2023년 정점(~85) 후 2025년 50으로 감소. 중국은 2023년부터 급상승, 2025년 30. Europe은 저위 정체.

[Figure 1.1.2: 2003-2025년 미국·중국·Europe notable AI 모델 연도별 누적 추이 라인 차트. 미국은 2020년경부터 급상승 후 2025년 감소, 중국은 2023년 이후 추격, Europe은 낮은 수준 유지.]

**Figure 1.1.3 — Number of notable AI models by geographic area, 2003-25 (sum) — World map**

범례 구간: 1-10, 11-20, 21-60, 61-180, 181-630

[Figure 1.1.3: 2003-25 누적 notable AI 모델 수 세계지도(색상 음영).
- 최상위 구간 (181-630): United States, China
- 상위 구간 (61-180): Canada, United Kingdom, Germany, France 등 서유럽 일부, Japan, Australia
- 중위 구간 (21-60): South Korea, Israel, Singapore, Italy, Netherlands, 러시아 일부
- 하위 구간 (11-20, 1-10): 나머지 대부분 국가
- 데이터 없음: 아프리카 대부분, 남미 일부, 중앙아시아 일부
- **주의**: 정확한 국가별 카운트는 원본 지도에서 직접 확인 필요 — 이 캡션은 색상 음영으로부터의 해석이며 일부 국가 분류는 부정확할 수 있음]

### By Sector and Organization (p. 18-19)

**본문 요약**: Notable AI 모델 개발은 산업에 압도적으로 집중 (Figures 1.1.4, 1.1.5). 지난 10년간 산업 비중 꾸준히 증가, 현재 **91.6%**. 2025년 기준 학계 출신 모델 **1개**, 산업 출신 **87개**.

**Top contributors in 2025 (industry)**:

| 조직 | 2025년 notable 모델 수 |
|---|---|
| OpenAI | 19 |
| Google | 12 |
| Alibaba | 11 |

**Top contributors since 2014 (industry)**:
- Google (최다), Meta, OpenAI 순

**Top contributors (academia, past decade)**:

| 대학 | notable 모델 수 |
|---|---|
| Tsinghua University | 26 |
| Stanford University | 26 |
| Carnegie Mellon University | 25 |

**Figure 1.1.4 — Number of notable AI models by sector, 2003-25**

[Figure 1.1.4: 2003-25년 sector별 notable AI 모델 시계열 라인 차트.
- Industry: 2003년 0에 가까운 수준에서 2024년 정점 near 90 후 2025년 87로 소폭 감소
- Industry-academia collaboration: 2014-2020년대 10 수준 정점, 2025년 5
- Academia: 2003-2015 pre-2020까지 10-20 수준, 2025년 1로 급락
- Other: 2-10 수준 정체]

*(Source: Epoch AI, 2026 | Chart: 2026 AI Index report)*

---

## Model Release · Parameter and Compute Trends (p. 20-22)

> 이하는 원문의 추가 차트 섹션들. 이번 추출본에서는 **첫 교차점 실습에 필요한 범위까지만** 포함했으며, 필요 시 동일 추출 프롬프트로 확장 가능.

**Model Release 섹션 핵심 수치 (p. 20)**:
- 2025년 notable 모델 총 릴리즈 **감소 추세** — 전년 대비 모든 주요 국가에서 감소 관찰

**Parameter and Compute Trends (p. 22)**:
- Reported parameter count: 3년 연속 약 1조 근처 정체
- Training compute: 독립 추정으로 연 3.3배 성장 지속

---

## 추출 프롬프트 원본 (재현 가능성)

```
이 PDF를 AI-friendly 마크다운으로 추출해줘.

규칙:
- 본문은 평문 마크다운
- 표는 마크다운 표
- 차트/그림은 [Figure X.Y: 설명 + 주요 수치] 캡션
- 각 섹션 끝에 (p. 원본 페이지 범위) 명시

범위: "Top Takeaways" (p. 9-11) + "Chapter 1.1 Notable AI Models" (p. 16-22)
결과는 output/ai_index_extracted.md 로 저장.
```

---

## 재사용 힌트

이 추출본은 다음 질문들에 바로 답할 수 있는 형태로 만들어졌습니다:

- "한국이 1위인 항목과 근거" → Top Takeaway 2, Chapter 1 Highlight 2
- "미국·중국 모델 개발 수 비교" → Figure 1.1.1 표
- "Figure 1.1.3 지도에서 최상위 국가" → Figure 1.1.3 캡션
- "AI 투자 추세" → Top Takeaway 7
- "환경 영향" → Top Takeaway 10, Chapter 1 Highlight 7

동일한 추출본을 Claude, ChatGPT, Gemini 어디에 넣어도 결과가 일관성 있게 나오는지 확인해 보세요 — 이게 "도구 독립적 자산"의 의미입니다.

---

*추출: 2026-04-18 | 원본 © Stanford HAI · CC BY-ND 4.0 | 추출본: CC BY-NC-SA 4.0*
