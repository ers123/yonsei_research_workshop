# 연구팀 Lite — 16GB 노트북용

단일 4B 모델(`gemma4:e4b`) 로 세 에이전트 역할 전부를 돌리는 **경량 버전**. 16GB RAM · Intel Mac 포함 · macOS 12 에서도 작동.

> **포지셔닝**: "같은 모델 · 역할별 프롬프트만 다름" 을 증명하는 미니멀 버전.
>
> 핵심 메시지: **모델 크기보다 역할 설계(=하네스)가 먼저다.**

---

## 같은 파이프라인의 3가지 도구

같은 "3-role × 3-stage = 9 prompts + 감독 persona" 구조를 세 가지 다른 도구로 실현할 수 있습니다:

| 도구 | 경로 | 대상 |
|---|---|---|
| **Streamlit Lite (이 폴더)** | `demo/streamlit_research_team_lite/` | 비CLI · 완전 로컬 Ollama · GUI |
| **Claude Code subagents** | `hands_on/claude_code_agents/` | Claude Code 사용자 · 네이티브 CLI · Anthropic 클라우드 |
| **Scholar-skill** (Zhang 2026) | 외부 arXiv 레퍼런스 | 연구실 풀 자동화 (26 skills × 18 phases × 53 quality gates) |

세 가지는 모두 **같은 프롬프트 구조를 공유** — 본 repo 의 `agents.py::STAGE_PROMPTS` 가 기준 SSOT (Single Source Of Truth).

---

## 설치 + 실행

### 1. Ollama + 모델 준비

```bash
# Ollama 설치 (macOS 14+ 는 공식 .dmg, 아니면 curl install)
# 상세: hands_on/SETUP.md

# Lite 전용 모델 pull (~9.6GB, 5-15분)
ollama pull gemma4:e4b
# 주의: "E4B" 는 effective 4B (MatFormer 구조). 디스크/메모리 실사용은 ~9.6GB.
#      16GB RAM 에서 다른 앱 닫고 돌리는 선.

# 확인
ollama list
# → gemma4:e4b 가 목록에 있으면 OK
```

> **tag 주의**: `ollama pull gemma4` (태그 미지정) 는 환경에 따라 더 큰 변종(10GB+) 을 받을 수 있습니다. Lite 는 **정확히 `gemma4:e4b`** 를 권장.

### 2. Python 환경

```bash
cd demo/streamlit_research_team_lite
python3 -m venv .venv
source .venv/bin/activate          # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 3. 실행

```bash
streamlit run app.py
```

브라우저가 자동으로 http://localhost:8501 을 엽니다.

**첫 화면에서 볼 것**:
- 사이드바 브랜드: **"연구팀 · Lite"** + 부제 `gemma4:e4b × 3 roles · 16GB-friendly`
- 사이드바 체크박스 **"⚙️ 에이전트별 모델 지정"** 이 이미 ON
- 세 역할(수연/준호/지은) 모두 `gemma4:e4b` 로 사전 선택
- 메인 상단 **🪶 Lite 모드 안내** 파란 박스

---

## 데모 시나리오

### 1단계 — 최소 경로 완주 (5분)

1. 🎯 **예시로 시작** 버튼 클릭 → 식품영양 / 고령자 식품불안정 시나리오 자동 입력
2. ▶ **연구팀 실행**
3. 수연 → 준호 → 지은 순서로 스트리밍 관찰
4. **완료 후 근거 원장** (`[근거: 파일명] X건 · [추측] Y건`) 확인
5. 산출물 내보내기 → **Word 문서** 한 번 다운로드

**예상 시간 (16GB 노트북 기준)**:
- 첫 호출 (모델 로딩): 1-3분
- 두 번째부터: 각 단계당 30-90초
- 전체 3단계 합쳐: 약 3-6분

### 2단계 — "티키타카" 확장 (여력 있으면)

여기서부터는 사이드바를 활용한 **즉석 실험**:

**실험 A — 비판자(준호)만 다른 모델로 교체**

1. 추가 모델 받기 (Gemma 4 e4b 가 이미 9.6GB 쓰고 있으니 7B 이상은 16GB 에선 스왑 주의):
   ```bash
   ollama pull deepseek-r1:7b        # ~4GB, 사고 모델 (32GB 노트북 권장)
   # 16GB 에서 안전한 대안:
   ollama pull qwen2.5:3b            # ~2GB, 한국어 OK
   ```
2. 사이드바에서 **"준호"** 드롭다운만 바꿔서 `deepseek-r1:7b` 선택
3. 사이드바 **🧠 사고 모드 ON** (준호의 비판이 길고 깊어짐)
4. 같은 입력으로 **정제 대화 → 준호만 재실행**
5. v1(e4b 준호) vs v2(deepseek 준호) 탭에서 **비판의 깊이 차이** 직접 비교

**실험 B — 총괄(지은)만 한국어 특화 모델로**

1. `ollama pull qwen2.5:7b` (아직 안 받았으면)
2. 사이드바에서 **"지은"** 만 `qwen2.5:7b` 로
3. 정제 대화 → 지은만 재실행
4. 한국어 학술체 자연스러움 개선 체감

> **주의**: 16GB 에서 4B + 7B 동시 로드는 스왑 위험. 각 단계 사이에 `ollama stop <직전 모델>` 로 메모리 비우는 게 안전.

### 3단계 — 지도교수 모드 (옵션)

- 사이드바 **🎓 지도교수 모드** 토글 ON → 한민수 (10가지 메타 질문) 추가
- 동일한 e4b 로 4번째 역할까지 실행
- 산출물 → **지도교수 회의 1-pager (.md)**

---

## 워크숍 사용법

| 트랙 | 적합한 청중 | 진행 방식 |
|---|---|---|
| 3분 라이브 데모 | 전체 청중 (강사) | 🎯 예시로 시작 → 바로 실행 → 근거 원장 · 산출물만 |
| 15분 실습 | 16GB+ 노트북 보유자 | 위 1단계 완주 + 2단계 실험 A 중 하나 |
| 홈스터디 | 관심 참석자 | 2단계 실험 A+B 전부 + 지도교수 모드 |

**다른 도구로 전환**:
- **Claude Code 쓰시는 분** → `hands_on/claude_code_agents/` 에 같은 9개 프롬프트를 `.claude/agents/` 형식으로 포팅. 설치 5분.
- **32GB + M시리즈 · 고급 시연** → 직접 `app.py` 의 `LITE_REQUIRED_MODEL` 을 더 큰 모델로 교체하거나 `per_agent_mode` 에서 역할마다 다른 모델 지정.

---

## 트러블슈팅

| 증상 | 원인 | 대응 |
|---|---|---|
| 사이드바에 `gemma4:e4b` 안 보임 | pull 안 된 상태 | `ollama pull gemma4:e4b` 후 앱 새로고침 |
| 첫 호출 5분 이상 걸림 | CPU 전용 추론 · 스왑 | 다른 앱 닫기, `ollama ps` 로 메모리 확인 |
| 응답 비어있음 (🧠 ON 상태) | 사고 예산 초과 | 🧠 사고 모드 OFF 후 재시도 |
| 한국어 품질이 아쉬움 | 4B 한계 | 실험 B (qwen2.5:7b 로 지은 교체) 시도 |
| "Ollama 연결 실패" 배너 | 서버 미기동 | `ollama serve` (별도 터미널) |
| 에이전트별 모델 섹션이 안 나옴 | 체크박스가 실수로 꺼짐 | "⚙️ 에이전트별 모델 지정" 다시 ON |

---

## 스모크 테스트

구조적 정합성(임포트 · 프롬프트 스왑 · 기본값) 검증용 파이썬 스크립트가 포함돼 있습니다. Ollama 없이도 실행 가능:

```bash
python smoke_test.py
```

**통과 조건**: 모든 체크가 `OK` 또는 `PASS` 로 표시. 실패 시 해당 줄을 강사에게 공유.

---

## 라이선스

CC BY-NC-SA 4.0 · 원본: [나만의 법무팀 (Gemma 4 + Ollama + Streamlit)](https://www.youtube.com/watch?v=t7JjQTEnKOo) · 변환: 연세대학교 생활과학대학 워크숍 (2026.04.24)
