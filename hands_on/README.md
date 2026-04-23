# hands_on · 실습 자료

- 연세대학교 생활과학대학 워크숍 (2026.04.24) 실습 자료 모음. 
- 파일이 많아 보이지만 **본인 상황에 맞는 경로만 따라가면** 됩니다.

---

## 📍 먼저 여기부터 — 워크숍 참가자

| 파일 | 용도 |
|---|---|
| **[실습_안내문.md](실습_안내문.md)** | 🎯 **가장 먼저 읽으세요.** 워크숍 당일 가이드 (QR 배포본) — 공통 준비 · Track A/B/C 흐름 · 트러블슈팅 · macOS/Windows 명령 병기 |
| [SETUP.md](SETUP.md) | 사전 환경 설치 상세 (OS 별 3갈래 분기). 실습_안내문이 요약한 설치 단계의 원문 |

**워크숍에 오셨다면 이 두 파일만 있으면 충분** 합니다. 아래 자료는 실습_안내문 안에서 필요할 때 링크로 연결됩니다.

---

## 🛠 Track 별 실습 자료

각 Track 실습 프롬프트 · 템플릿 · 원자료가 아래 폴더에 나눠져 있습니다. **직접 열 필요 없음** — 실습_안내문의 링크를 따라가면 자연스럽게 도달합니다.

| 폴더 | 용도 | 어느 Track 에서 씀 |
|---|---|---|
| [prompts/](prompts/) | 트랙별 실습 프롬프트 + 홈스터디 재현 예시 | A · B · C |
| [templates/](templates/) | `CLAUDE.md` · `AGENTS.md` 빈 템플릿 + 완성 예시 + A/B 응답 비교 | A |
| [references/](references/) | Stanford AI Index Report 2026 PDF (37MB) · 추출 백업 · Naive vs Harness 예시 | B |
| [sample_data/](sample_data/) | 업로드 자료 안내 placeholder | C |

---

## 🧑‍💻 Claude Code 사용자용 (선택)

| 폴더 | 용도 |
|---|---|
| [claude_code_agents/](claude_code_agents/) | 수연·준호·지은 역할을 Claude Code 네이티브 subagent 형식(`.claude/agents/`)으로 포팅한 10개 `.md` 파일. 이미 Claude Code 쓰시는 분은 Streamlit Lite 설치 없이 바로 사용 가능. **현장 실습 대상 아님** — 홈스터디용 |

---

## 📚 홈스터디 · 고급 자료

당일 워크숍 범위를 넘어 차분히 재현하거나 더 깊이 파고 싶은 분용. **워크숍에 오신 분이 당일 꼭 봐야 할 것은 없음**.

| 파일 | 용도 |
|---|---|
| [ra_team_setup.md](ra_team_setup.md) | RA 팀 상세 구성 · Claude Code + 로컬 모델 연결의 두 경로 (LM Studio / Ollama+프록시) 심화 |
| [ra_team_tiers.md](ra_team_tiers.md) | Free ($0) / Standard ($20) / Full ($220-420) 세 단계 비용·품질 비교 |
| [reference_setup_m4_32gb.md](reference_setup_m4_32gb.md) | 강사 레퍼런스 하드웨어 스펙 — "이 환경에서 뭐가 얼마나 걸리나" 벤치마크 참고 |
| [scenario_comparison/](scenario_comparison/) | 4모델 교차검증 (DeepSeek R1 · Gemma 4 E4B · Codex · Gemini) 실측 결과 — "왜 교차검증이 필요한가" 의 증거자료 |

---

## 🧭 어디서 뭘 봐야 할지 3초 판단

| 상황 | 가야 할 곳 |
|---|---|
| Workshop 참석 · 준비만 하고 싶음 | **실습_안내문.md** |
| 환경 설치부터 차근차근 | **SETUP.md** |
| Track A (맥락 문서) 만들어보고 싶음 | `prompts/track_a_맥락문서.md` |
| Track B (대량 처리) 재현 | `prompts/track_b_대량처리.md` |
| Track C (연구팀 Lite) 당일 실습 | 실습_안내문 Track C 섹션 → `demo/streamlit_research_team_lite/` |
| 나는 Claude Code 유저야 | `claude_code_agents/README.md` |
| 집에서 차분히 Claude Code + Ollama 셋업 | `prompts/track_c_홈스터디_완주예시.md` |
| 로컬 AI 전체 개념부터 | `appendix/01_로컬AI_무료_활용_가이드.md` (repo 루트 → appendix/) |
| 민감 주제 연구 용도 | `appendix/04_Uncensored_로컬모델_연구활용_가이드.md` |

---


