# Qualitative Research — Mini Demo Plan

## 메시지
"이 정도 양의 데이터도 에이전트에게 설계를 주고 맡기면 된다."
**자동화의 극단(Sakana)이 아니라 설계 기반 위임(Zhang).**

## 범위
전체 재현 불필요. **"감이 오는 정도"**만.

이 폴더 최종 산출물 (목표):

```
demo/qualitative_research/
├── PLAN.md                   ← 이 문서
├── README.md                 ← 데모 개요 (에이전트 작성)
├── CLAUDE.md                 ← 프로젝트 맥락 문서 (익명 버전)
├── codebook.md               ← 분석 체계 (질적 연구 예시라 유지)
├── deliverables/
│   ├── final_report_excerpt.md    ← 분량의 30% 발췌
│   └── policy_memo_excerpt.md     ← 분량의 30% 발췌
└── visualizations/
    └── viz_institutional_heatmap.html
```

원본의 `raw/`, `qualitative/` 전수 익명화는 **하지 않습니다.**
README.md에 원본 폴더 트리 텍스트로 기록 → 구조만 보여줘도 의도 전달.

---

## 실행 방법

이 데모는 **워크숍 본진과 별도로 Claude Code에서 생성 예정.**

### 준비
- 원본: 별도 private repo (local clone)
- 대상 파일: codebook.md, deliverables 2개, viz heatmap 1개

### Claude Code 세션 시작 프롬프트

```
~/projects/original-project/에 원본 프로젝트가 있어.
아래 규칙대로 익명화된 mini 버전을 
~/projects/yonsei_research_workshop/demo/qualitative_research/ 에 생성해줘.

[AGENTS.md 규칙]
(아래 "치환 사전" 섹션 참조)

[대상 파일 및 처리]
1. codebook.md → 그대로 (구조 보존), 기관/개인 언급만 치환
2. deliverables/final_report.md → final_report_excerpt.md (분량 30%로 축약, 익명화)
3. deliverables/policy_memo.md → policy_memo_excerpt.md (분량 30%로 축약, 익명화)
4. visualizations/viz_institutional_heatmap.html → 라벨만 섹터 코드로 치환, 기능/수치 유지

[검증]
작업 후 grep으로 원본 이름/기관명 잔여 0 hits 확인하고 보고해줘.
```

### 치환 사전

| 범주 | 치환 규칙 | 예시 |
|---|---|---|
| 연구 참여자 (7명) | P01, P02, ... P07 순차 부여 | 연구자 실명 → P01 |
| 기타 인명 | P08, P09 순차 | — |
| 국내 출연연 (17개) | 기관_[분야] 형식 | 기관_원자력, 기관_ICT, 기관_바이오 등 |
| 총괄 기관 | 총괄기관 | — |
| 해외 연구기관 | 해외기관_[국가], 해외연구소_[국가], 해외대학_[국가] | 해외대학_일본, 해외연구소_독일 |
| 날짜 | "2025년 N분기" 형식 | 250314 → 2025년 1분기 |

**원칙:**
1. 구조 100% 보존 — 폴더 트리, 파일명 패턴, 코드북 체계가 데모의 핵심
2. 한국어 유지 — 청중이 한국어 사용자
3. HTML 기능 유지 — 라벨만 치환, 인터랙티브 기능 그대로
4. 가독성 유지 — 치환 후 문맥이 자연스러운지 확인

---

## 예상 시간

Claude Code 에이전트 기준: 20-30분.
사람은 최종 검증만.

---

## 왜 "mini" 인가

워크숍 라이브 데모에서는 이 폴더의 **codebook.md와 visualizations/ HTML 한 장**만 보여줄 예정. 나머지는 "자습용 참고 자료"로만.

즉 청중이 보는 것:
1. 폴더 구조 트리 (README.md에 있음)
2. codebook.md (주제 코드 + 맥락 코드 체계)
3. heatmap HTML (시각화가 어떻게 나오는지)

나머지는 "깊이 들어가고 싶으면 repo에서 확인"으로.

---

## Vibe Researching 관점

이 데모가 보여주는 것은 Zhang (2026)의 **Vibe Researching** 입장입니다:

- 연구자가 **의도(codebook, 치환 규칙)를 설계** → 에이전트가 실행
- 연구자가 **검증** → 에이전트가 자동 수정
- 반복 가능한 파이프라인 → 다른 프로젝트에도 재사용

**Sakana AI Scientist (Nature 651, 2026)**의 완전 자동화와의 차이:
- Sakana: "아이디어부터 peer review까지 전부 에이전트가"
- Zhang: "연구자가 판단을 책임지고 에이전트는 실행 기술을"

본 데모는 Zhang 쪽. 완전 자동화 아님.

---

## 경량 모델로 가능한가?

이 익명화 작업 자체는 경량 모델로 충분합니다.

| 작업 | Gemma 4 E2B (2.3B) | Gemma 4 E4B (4B) | Phi-4-mini (3.8B) | Qwen3-Coder 30B |
|---|---|---|---|---|
| 사전 기반 단순 치환 | ✅ | ✅ | ✅ | ✅ |
| 치환 후 문맥 자연스러움 검증 | ⚠️ | ✅ | ✅ | ✅ |
| codebook 엔트리 재구성 | ❌ | ⚠️ | ⚠️ | ✅ |
| HTML 라벨 교체 + 기능 보존 | ✅ (단순) | ✅ | ✅ | ✅ |

**결론:** 경량 모델로도 가능. 단 최종 검수는 Claude Sonnet/Opus급 권장.
상세는 `appendix/01_로컬AI_무료_활용_가이드.md`.

---

## 체크 (데모 준비 완료 여부)

- [ ] Claude Code 세션 실행
- [ ] 5개 산출물 생성 (README, CLAUDE.md, codebook.md, deliverables 2개, viz 1개)
- [ ] 원본 인명/기관명 잔여 0 hits (grep 검증)
- [ ] HTML 브라우저 열어 작동 확인
- [ ] workshop day -1 까지 이 PLAN.md를 참고해 생성 완료
