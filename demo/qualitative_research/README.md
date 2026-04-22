# 질적 연구 AI 에이전트 활용 데모

## 개요

이 폴더는 AI 에이전트(Claude Code)를 활용한 **대규모 질적 연구** 사례를 워크숍 참가자에게 보여주기 위한 데모 자료입니다.

원본 프로젝트는 한국 정부출연연구기관(출연연) 15개 기관의 **국제 R&D 협력 실태**를 심층 인터뷰 기반으로 분석한 질적 실증 연구입니다. 21,011줄의 인터뷰 데이터를 LLM 기반 구조화 코딩으로 분석하여 1,527개의 코딩된 발췌문을 생성하고, 이를 토대로 정책 보고서와 시각화를 산출했습니다.

## 원본 프로젝트 구조 (익명화)

아래는 원본 프로젝트의 폴더 트리입니다. 워크숍에서 **에이전트가 다루는 데이터의 규모**를 보여주기 위해 기록합니다.

```
project_root/
├── CLAUDE.md                          # 에이전트 컨텍스트 문서
├── codebook.md                        # 분석 코드북 (주제코드 + 맥락코드)
├── raw/                               # 원본 인터뷰 녹취록
│   ├── 기관_원자력_interview.md        # ~1,400줄
│   ├── 기관_ICT_interview.md          # ~1,200줄
│   ├── 기관_표준_interview.md         # ~1,100줄
│   ├── 기관_해양_interview.md         # ~1,300줄
│   ├── 기관_바이오_interview.md       # ~1,500줄
│   ├── 기관_환경_interview.md         # ~1,600줄
│   ├── 기관_에너지_interview.md       # ~1,200줄
│   ├── 기관_기계_interview.md         # ~1,400줄
│   ├── 기관_화학_interview.md         # ~1,300줄
│   ├── 기관_항공_interview.md         # ~1,500줄
│   ├── 기관_기초과학_interview.md     # ~1,200줄
│   ├── 총괄기관_interview.md          # ~1,800줄
│   ├── 기관_핵융합_interview.md       # ~1,100줄
│   ├── 기관_정보_interview.md         # ~1,400줄
│   └── 기관_지질_interview.md         # ~1,500줄
│                                      # 합계: ~21,011줄
├── qualitative/                       # LLM 구조화 분석 결과
│   ├── 기관_원자력_coded.md           # 코딩된 발췌문
│   ├── 기관_ICT_coded.md
│   ├── ... (15개 기관)
│   ├── comprehensive_policy_analysis_kor.md
│   ├── policy_recommendations.md
│   └── policy_memo.md                 # 통합 정책 메모 (~21,000줄)
├── deliverables/                      # 최종 산출물
│   ├── final_report_revised.md        # 최종 보고서 (~947줄)
│   └── policy_memo_revised.md         # 정책 메모 최종본
├── visualizations/                    # 인터랙티브 시각화
│   ├── viz_institutional_heatmap.html # 기관별 장애요인 히트맵
│   ├── viz_causal_network.html        # 인과관계 네트워크
│   └── viz_policy_roadmap.html        # 정책 로드맵 타임라인
└── tools/                             # 분석 도구 스크립트
    ├── code_interview.py              # 인터뷰 코딩 자동화
    ├── aggregate_codes.py             # 코드 빈도 집계
    └── generate_viz.py                # 시각화 생성
```

## 이 데모 폴더의 파일 구성

| 파일 | 설명 |
|------|------|
| `PLAN.md` | 데모 기획 문서 (이 폴더를 어떻게 구성할지에 대한 계획) |
| `README.md` | 이 문서. 데모 개요 및 파일 설명 |
| `CLAUDE.md` | 에이전트 지시 문서 (익명화 버전). 원본 프로젝트에서 에이전트에게 제공한 컨텍스트 |
| `codebook.md` | 분석 코드북. 8개 주제 코드 범주, 10개 맥락 코드로 구성된 분류 체계 |
| `deliverables/final_report_excerpt.md` | 최종 보고서 발췌본 (원본의 약 30%) |
| `deliverables/policy_memo_excerpt.md` | 정책 메모 발췌본 (테마 분석 구조 + 대표 인터뷰 요약) |
| `visualizations/viz_institutional_heatmap.html` | 15개 기관의 장애요인 비교 히트맵 (Plotly 인터랙티브) |

## Vibe Researching (Zhang, 2026)

이 데모가 보여주는 것은 Zhang (2026)의 **Vibe Researching** 개념입니다:

- **연구자가 설계한다**: 코드북, 분석 프레임워크, 익명화 규칙 등 연구의 핵심 판단은 사람이 합니다.
- **에이전트가 실행한다**: 21,000줄의 인터뷰를 코딩하고, 빈도를 집계하고, 시각화를 생성하고, 보고서를 작성하는 반복적 실행은 에이전트가 합니다.
- **연구자가 검증한다**: 코딩 결과의 정확성(Cohen's Kappa 0.85), 보고서의 논리적 일관성, 정책 제언의 타당성은 사람이 검증합니다.

이는 Sakana AI Scientist (Nature 651, 2026)의 완전 자동화와는 다릅니다. 연구자의 판단과 에이전트의 실행력을 결합하는 **설계 기반 위임** 방식입니다.

## 이 프로젝트에서 실제 사용한 모델

"AI 가 코딩했다" 는 추상 표현 대신 단계별로 어떤 모델이 돌아갔는지 기록합니다. **모델 선택 자체가 하네스 설계의 일부**입니다.

| 단계 | 사용 모델 | 왜 이 모델 |
|---|---|---|
| 1차 의미단위 분절 + 코드 1차 부여 | **Gemma 3 4B** (Ollama 로컬) | 21,011줄 반복 작업. 로컬·무료·프라이버시. 간단한 분류에 충분. |
| 코드 검증 · 경계 케이스 판정 | **Claude Sonnet 4.6** | Gemma 가 확신 못 한 케이스만 골라 정밀 재분류. 비용 절감. |
| 최종 보고서 · 정책 메모 작성 | **Claude Opus 4.7** | 한국어 학술체 · 긴 문서 일관성. 비용 高, 품질 최우선. |
| 교차검증 (200개 표본 재코딩) | **Qwen 2.5 14B** (Ollama 로컬) | Gemma 와 다른 계열 모델로 독립 재코딩 → Cohen's Kappa 0.85 산출. |
| 시각화 HTML/JS 생성 | **Claude Sonnet 4.6** | Plotly 코드 작성 정확도 · 빠른 iteration. |

**핵심 교훈**: 프런티어 모델(Opus/Sonnet) 하나로만 전부 돌리면 비용이 과다하고, 경량 모델(Gemma/Qwen) 하나로만 돌리면 한국어 학술문 품질이 떨어집니다. **단계별 특성에 맞춰 모델을 나눈 것**이 이 프로젝트 하네스의 실체입니다.

---

## 워크숍에서 보여줄 것

1. **폴더 구조 트리** (위 참조) -- 에이전트가 다루는 데이터의 규모
2. **codebook.md** -- 연구자가 설계한 분석 체계
3. **viz_institutional_heatmap.html** -- 에이전트가 생성한 인터랙티브 시각화
4. **deliverables/** -- 에이전트가 작성한 최종 산출물

나머지 파일은 "깊이 들어가고 싶으면 repo에서 확인"으로 안내합니다.
