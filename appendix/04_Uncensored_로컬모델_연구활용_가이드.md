# 별첨 4: Uncensored 로컬 모델의 연구 활용

**민감 코퍼스·합성 데이터·검열 편향 통제를 위한 심화 가이드 (Apple Silicon 기준)**

> 이 문서는 별첨 1(로컬 AI 무료 활용 가이드)의 후속입니다. 별첨 1이 "클로드 코드 백엔드 대체"에 초점을 두었다면, 본 문서는 **"정렬(aligned) 모델이 오히려 연구에 해가 되는 상황"**을 다룹니다.

---

## 들어가며

대학원 연구에서 ChatGPT, Claude, Gemini 같은 상용 정렬 모델을 썼을 때 다음과 같은 경험이 있을 겁니다.

- 성폭력 피해자 면담 녹취를 코딩 보조로 돌렸더니 모델이 "민감한 내용이라 처리할 수 없다"고 거부함
- 혐오발언 분류기를 만들려고 네거티브 샘플 합성을 요청했더니 "그런 내용은 생성할 수 없다"고 반환
- 한강 『채식주의자』의 폭력 장면을 다국어로 번역 비교하려는데 완곡어법으로 재작성됨
- 범죄 판결문 요약을 맡겼더니 피고인 행위 기술에서 핵심 사실이 소거됨

이것은 **모델의 능력 문제가 아니라 정렬(alignment) 층의 개입 문제**입니다. 그리고 이 개입이 연구 데이터 파이프라인에 들어가는 순간, 재현 불가능한 편향이 결과에 스며듭니다.

본 별첨은:

1. 왜 uncensored 모델이 **연구 방법론의 관점에서** 중요한지
2. 실제로 어떤 연구 시나리오에서 강점이 있는지
3. 설치·운영·프롬프트 설계를 어떻게 할지
4. 윤리적·제도적 경계를 어떻게 지킬지

를 실제 예시 모델 하나(`Jiunsong/supergemma4-26b-uncensored-mlx-4bit-v2`)를 중심으로 설명합니다.

---

## 1. 용어 정리: "Uncensored"가 의미하는 것

### 1.1. 정렬(Alignment)의 층위

현대 LLM은 최소 세 층의 학습을 거칩니다.

| 층 | 목적 | 효과 |
|---|---|---|
| 사전학습 (Pretraining) | 언어 분포 학습 | 지식·문법·스타일 |
| 지도학습 파인튜닝 (SFT) | 지시 따르기 | 질문-답변 포맷 |
| **인간 피드백 강화학습 (RLHF/DPO)** | 선호 정렬 | **거부·완곡·면책 삽입** |

"Uncensored" 모델은 대체로 3번째 층을 **제거·완화하거나 별도 데이터로 덮어쓴** 변형입니다. 파라미터 규모나 사전학습 지식은 동일합니다.

### 1.2. 오해 정정

- **오해 1**: "Uncensored = 성인물 모델"
  → 실제로는 **거부 분기(refusal branch)가 약화된 모든 모델**. 의학·법학·역사·문학 질의에서 정렬 모델이 거부하던 것도 답하게 됨.
- **오해 2**: "Uncensored = 더 똑똑함"
  → 아님. 오히려 환각이 늘 수 있음. 안전장치가 "확신 없을 때 면책" 역할도 했기 때문.
- **오해 3**: "Uncensored = 불법"
  → 아님. 모델 자체는 가중치 파일이며, 생성물의 책임은 사용자. 단 **출력물이 특정 법령을 위반하면** 그것은 사용자 문제(아청법, 명예훼손 등).

### 1.3. 왜 MLX 4-bit 버전인가

본 별첨은 `Jiunsong/supergemma4-26b-uncensored-mlx-4bit-v2`를 예시로 삼습니다. 이유:

- Apple Silicon(M1~M4) 통합메모리에 최적화 → 24~32GB 맥북에서 구동
- 4-bit 양자화로 디스크 ~13GB, 메모리 ~14GB
- MLX-LM CLI가 단순하고 OpenAI 호환 서버 제공
- Google Gemma 3 27B 기반 → 연구 수준 품질

Windows/Linux 사용자는 Ollama의 `huihui_ai/gemma3-abliterated` 계열로 대체 가능. 본 문서의 개념은 동일하게 적용됩니다.

---

## 2. 정렬 모델이 연구에 해가 되는 4가지 유형

### 2.1. 데이터 오염 (Data Contamination)

**증상**: 입력 텍스트에 대한 요약·분류·번역 결과에 모델이 **추가한** 면책조항·완곡어·경고문이 섞여 들어감.

**연구적 해악**: 질적 연구 코딩, 코퍼스 라벨링, 체계적 문헌고찰에서 이것이 통제되지 않으면 **해석의 객관성 담보 불가**.

**예시**:
```
입력: "피해자는 가해자로부터 반복적으로 폭행당했다."
정렬 모델 출력(요약 task): "피해자는 어려운 상황에 처했던 것으로 기술된다."
```

요약 태스크에서 "폭행"이 "어려운 상황"으로 치환된 것이 **누적**되면 결과 전체가 체계적으로 부드러워집니다.

### 2.2. 재현성 실패 (Reproducibility Failure)

**증상**: 같은 프롬프트에 대한 정렬 모델의 거부율이 **시점마다 달라짐**. 상용 API는 배포 버전이 수시로 바뀌고 그 변경 로그가 공개되지 않음.

**연구적 해악**: 6개월 뒤 재현 실패. 리뷰어가 "이 결과를 지금 재현할 수 있는가?" 물을 때 답할 방법이 없음.

**해결**: 로컬 고정 weight + seed 기록. 논문 부록에 `model_hash`, `quantization`, `seed`, `temperature` 명시.

### 2.3. 합성 데이터 생성 불능

**증상**: 혐오발언 탐지기, 독성 분류기, 피싱 메시지 필터 등을 학습시키려면 **네거티브 샘플**이 필요한데, 정렬 모델은 이걸 만들어주지 않음.

**연구적 해악**: 분류기 성능이 낮아짐. 또는 네거티브 샘플을 공개 데이터셋에 의존해야 하는데, 그러면 **한국어 도메인 데이터가 빈약**함.

**우회 수법의 한계**: "역할극", "학술 연구 목적"이라고 프롬프트에 써도 정렬 모델은 종종 거부. 거부 패턴 자체가 데이터 분포에 편향을 추가.

### 2.4. IRB·개인정보 충돌

**증상**: 연구 참여자 데이터(인터뷰 녹취, 의료기록, 미성년 증언 등)를 OpenAI/Anthropic API로 보내면 **기관 규정 및 개인정보보호법 위반** 가능성.

**연구적 해악**: 윤리위 승인받은 연구가 도구 선택 때문에 막힘. 또는 익명화 후 넣어도 **데이터가 제3자 서버에 체류**한다는 사실 자체가 문제.

**해결**: 로컬 실행. 네트워크 차단 상태로도 돌아감. 참여자에게 "AI는 본인 PC에서만 작동합니다"라고 고지 가능.

---

## 3. 연구에서의 구체적 활용 시나리오

### 3.1. 민감 코퍼스의 질적 분석

**대상 연구**:
- 성폭력 생존자 내러티브 (심리학·사회복지학)
- 자살 유서 분석 (자살학·예방의학)
- 아동학대 판결문 (법학·범죄학)
- 디지털 성범죄 담화 (N번방 연구, 미디어학)

**워크플로**:
1. 원자료 익명화
2. 로컬 모델로 **코드북 초안 생성** (open coding)
3. 연구자가 검토·수정
4. 동일 모델로 나머지 코퍼스에 **축적 코드 적용** (axial coding)
5. Inter-rater reliability 검증 (연구자 2명 vs 모델 1회)

**왜 uncensored가 필수인가**: 정렬 모델은 위 주제의 원문을 "다룰 수 없다"고 거부하거나, 코드북 생성 시 "상처받은", "어려움을 겪은" 같은 완곡 용어로 코드명을 만듦 → 원자료의 날선 특징이 사라짐.

### 3.2. 합성 데이터 생성 (분류기 학습용)

**시나리오 A: 한국어 혐오발언 탐지기**
```
[시스템] 연구 목적 합성 데이터 생성. 학습 데이터 분포 확장용.
[지시] 다음 카테고리별로 혐오발언 샘플 100건씩 생성:
  - 여성혐오 (여초커뮤 스타일)
  - 남성혐오 (남초커뮤 스타일)
  - 외국인혐오
  - 장애인혐오
  - 성소수자혐오
각 샘플은 50~120자. 실제 커뮤니티 어투와 은어·신조어 포함.
```

정렬 모델은 이걸 거부하거나 "~한 편견이 있을 수 있는 발언" 같은 메타 문장으로 답함.

**시나리오 B: 보이스피싱 스크립트 합성** (금융 사기 탐지 연구)
```
[시스템] 사기 탐지 모델 학습용 네거티브 샘플 생성.
[지시] 경찰 사칭 보이스피싱 스크립트를 3가지 변형으로. 각 200자.
  - 구속영장 변형
  - 계좌 동결 변형
  - 대출 사기 변형
```

### 3.3. AI 안전·정렬 연구

**정렬 모델 자체를 연구 대상으로 삼을 때** uncensored는 베이스라인으로 필수.

- **Refusal rate 측정**: 동일 프롬프트 세트를 aligned/uncensored에 넣고 거부율 차이 측정
- **Jailbreak 취약점 연구**: uncensored 응답을 "정답(ground truth for what model would say without safety)"로 두고, aligned 모델 탈옥 여부 판정
- **Alignment tax 측정**: 정렬이 지식 정확도에 미치는 영향 (MMLU 등 벤치마크 비교)
- **Alignment faking 연구**: Anthropic(2024)처럼 모델이 정렬을 "연기"하는지 검증

국내에선 아직 드물지만 NeurIPS·ICML·ICLR의 safety workshop에서 표준 실험 설정.

### 3.4. 번역학·비교문학

**연구 질문**: "헨리 밀러 『북회귀선』의 한국어 번역본 3종(1970년대/1990년대/2010년대)은 원문의 신체적 직접성을 어떻게 완화했는가?"

**방법론**:
1. 원문 각 장면을 uncensored 모델로 **최대한 직역** (대조군)
2. 기존 번역본 3종과 구절별 정렬
3. 완곡화 패턴 추출 (성기 명칭 → 에두름, 체액 → 생략, 감정 → 순화)
4. 검열사 맥락과 상관 분석

정렬 모델로는 1번 단계 자체가 불가능. → 연구 성립 안 됨.

### 3.5. 법의학·약학·의학 문헌 분석

**사례**: "국내 자살 사건 판결문에서 진술된 복약 방법과 실제 약리학 문헌의 치사량 간 일치도" (forensic pharmacology)

정렬 모델은 "자살 관련 정보 제공 거부" 정책으로 분석 자체 거부. Uncensored는 공개 문헌 데이터를 있는 그대로 대조 가능.

단, **이런 연구는 IRB·소속 기관 법무팀 검토 필수**. 본 가이드는 방법의 가능성을 말할 뿐, 개별 연구의 적법성을 보장하지 않음.

### 3.6. 극단주의·선전·전시 연구

- 테러리스트 매니페스토 주제 분석
- 전범 재판 기록 분석
- 냉전기 북한·남한 선전물 수사학 비교

자료가 공개된 학술 대상이지만, 정렬 모델은 종종 "극단주의 콘텐츠 처리 거부"로 막힘.

### 3.7. 문화·젠더·성 연구

- 포르노그래피 연구 (학문 분과 존재)
- 한국 웹소설·BL·GL 담화분석
- 성노동 현장 구술사 코딩
- 퀴어이론 고전(Delany, Dworkin) 재독

### 3.8. 언어학·사회언어학

- 한국어 욕설·비속어 코퍼스 구축
- 남초·여초 커뮤니티 언어 대조
- 군대 은어, 감옥 은어 사전 작성
- 신조어 생성 패턴 연구

---

## 4. 설치와 운영

### 4.1. 하드웨어 요건 (본 예시 모델 기준)

| 환경 | 구동 여부 | 비고 |
|---|---|---|
| 맥북 M1/M2 16GB | ❌ | 스왑 발생, 사실상 불가 |
| 맥북 M2 24GB | △ | 다른 앱 최소화시 가능 |
| **맥북 M1 Pro/M2 Pro 32GB+** | ✅ | 쾌적 (Peak 14.5GB) |
| **맥북 M3/M4 32GB+** | ✅ | 가장 쾌적 (~32 tok/s) |
| Mac Studio 48GB+ | ✅ | 여러 모델 병행 가능 |
| Intel Mac | ❌ | MLX 미지원 |

Windows/Linux 환경에선 Ollama + abliterated 모델로 대체.

### 4.2. MLX-LM 설치

```bash
# Homebrew uv 사용자
uv tool install mlx-lm

# 또는 일반 pip
pip install -U mlx-lm
```

설치 후 PATH에 `mlx_lm.generate`, `mlx_lm.chat`, `mlx_lm.server` 등 추가.

### 4.3. 세 가지 운영 모드

#### 모드 A: 단발성 생성 (`mlx_lm.generate`)

```bash
mlx_lm.generate \
  --model Jiunsong/supergemma4-26b-uncensored-mlx-4bit-v2 \
  --system-prompt "$(cat system.txt)" \
  --prompt "$(cat user.txt)" \
  --max-tokens 3000 \
  --temp 0.7 \
  --top-p 0.9
```

- 한 번의 호출만 필요한 경우 (분류, 요약, 번역 등)
- 배치 처리 스크립트와 결합 용이
- 매 호출마다 모델 리로드(약 1~2분) → 대량 처리엔 비효율

#### 모드 B: 대화형 (`mlx_lm.chat`)

```bash
mlx_lm.chat --model Jiunsong/supergemma4-26b-uncensored-mlx-4bit-v2
```

- 모델 1회 로드 후 세션 동안 재사용
- 멀티턴 연구 브레인스토밍, 코드북 공동 개발에 적합
- 히스토리 자동 관리

#### 모드 C: OpenAI 호환 서버 (`mlx_lm.server`) ⭐ 연구용 핵심

```bash
mlx_lm.server \
  --model Jiunsong/supergemma4-26b-uncensored-mlx-4bit-v2 \
  --port 8080 \
  --host 127.0.0.1
```

이게 **연구 워크플로의 핵심**입니다. 이유:

1. Python 분석 스크립트에서 OpenAI SDK 그대로 사용
2. Jupyter 노트북에서 모델 재로드 없이 반복 호출
3. 배치 파이프라인(1만 건 분류 등) 구축 가능
4. Claude Code의 백엔드로도 사용 가능 (별첨 1 방식과 동일)

**Python 호출 예**:
```python
from openai import OpenAI
client = OpenAI(base_url="http://127.0.0.1:8080/v1", api_key="local")

def classify(text):
    r = client.chat.completions.create(
        model="local",
        messages=[
            {"role": "system", "content": CODEBOOK_PROMPT},
            {"role": "user", "content": text},
        ],
        temperature=0.0,  # 분류는 결정론적으로
        max_tokens=200,
        seed=42,  # 재현성
    )
    return r.choices[0].message.content

import pandas as pd
df = pd.read_csv("interviews.csv")
df["code"] = df["transcript"].apply(classify)
df.to_csv("coded.csv", index=False)
```

### 4.4. 첫 실행 체크

```bash
mlx_lm.generate \
  --model Jiunsong/supergemma4-26b-uncensored-mlx-4bit-v2 \
  --prompt "한국어로 자기소개 한 줄." \
  --max-tokens 100
```

처음엔 모델 다운로드(~13GB, 10~20분) 후 응답 출력. `Peak memory: 14.48 GB` 같은 로그가 나오면 정상.

---

## 5. 연구용 프롬프트 패턴

### 5.1. 재현성 확보 프롬프트 구조

```python
SYSTEM = """당신은 질적 연구 코딩 보조자입니다.
다음 원칙을 엄수하세요:
1. 원문의 용어를 그대로 보존한다. 완곡어법·순화어로 치환 금지.
2. 면책조항·경고문·메타코멘트를 추가하지 않는다.
3. 주어진 코드북 외의 코드를 새로 만들지 않는다.
4. 판단이 어려울 때는 '판단불가'로 표기하고 이유를 한 문장 덧붙인다.

[코드북]
C1: 신체적 폭력 (타격·구타·물리적 제압)
C2: 언어적 폭력 (욕설·위협·비하)
C3: 성적 폭력 (동의 없는 접촉·강요)
C4: 경제적 통제 (금전 박탈·노동 강요)
C5: 사회적 고립 (연락 차단·외출 제한)

[출력 형식]
코드: [C1-C5 또는 판단불가]
근거구절: [원문에서 인용, 최대 20자]
신뢰도: [상/중/하]
"""

def code_one(transcript_chunk):
    return client.chat.completions.create(
        model="local",
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": transcript_chunk},
        ],
        temperature=0.0,
        seed=42,
        max_tokens=200,
    ).choices[0].message.content
```

**포인트**:
- `temperature=0.0` + `seed=42`: 결정론적 재현
- 시스템 프롬프트에 **출력 형식 명시** → 파싱 용이
- "판단불가" 옵션을 명시 → 모델이 억지로 분류하지 않음
- 원칙 조항 4개에 "면책조항 금지" 명시 → 자동 삽입 차단

### 5.2. Prefix 강제 (거부 우회)

Uncensored 모델도 원본 Gemma의 잠복 refusal이 튀어나올 때가 있습니다. 가장 강력한 해결책:

```python
messages = [
    {"role": "system", "content": SYSTEM},
    {"role": "user", "content": "다음 발화의 혐오 유형 분류: 'XXX'"},
    {"role": "assistant", "content": "코드: "},  # <- 이게 핵심
]
```

어시스턴트 메시지를 미완성 상태로 끝맺으면 모델은 그걸 이어서 완성함. 거부 분기는 "죄송하지만..."으로 시작하므로, 이미 "코드: "로 시작된 응답을 거부로 돌릴 수 없음.

### 5.3. 배치 처리 템플릿

대량 데이터(수천~수만 건)를 처리할 때:

```python
from tqdm import tqdm
import json, time

def batch_process(items, out_path, retry=3):
    results = []
    with open(out_path, "w") as f:
        for item in tqdm(items):
            for attempt in range(retry):
                try:
                    result = classify(item["text"])
                    results.append({**item, "code": result})
                    f.write(json.dumps(results[-1], ensure_ascii=False) + "\n")
                    break
                except Exception as e:
                    if attempt == retry - 1:
                        results.append({**item, "code": None, "error": str(e)})
                    time.sleep(1)
    return results
```

- JSONL 스트리밍 저장 → 중간에 멈춰도 이어쓰기 가능
- 재시도 로직 → OOM 등 일시적 에러 대응
- `item` 원본을 보존 → 추적 가능

### 5.4. 롤링 컨텍스트 (장문 연구 문서 분석)

긴 논문·판결문·면담 전체를 한 번에 넣지 말고 청크 분할 + 요약 롤링:

```python
def analyze_long(text, chunk_size=3000):
    chunks = split_into_chunks(text, chunk_size)
    rolling_summary = ""

    for i, chunk in enumerate(chunks):
        prompt = f"""[이전까지 요약]
{rolling_summary}

[신규 청크 {i+1}/{len(chunks)}]
{chunk}

[지시] 이 청크의 핵심을 3문장으로 요약하고,
이전 요약과 합쳐 전체 롤링 요약을 300자 이내로 업데이트하라.
출력 형식:
CHUNK_SUMMARY: ...
UPDATED_ROLLING: ...
"""
        response = client.chat.completions.create(
            model="local",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        ).choices[0].message.content

        rolling_summary = parse_rolling(response)

    return rolling_summary
```

---

## 6. 워크숍 프레임워크와의 연결

본 워크숍의 세 축 — **Context · Harness · Verification** — 안에서 uncensored 모델이 어디에 위치하는지.

### 6.1. Context Engineering

`CLAUDE.md` 또는 `AGENTS.md`에 연구 맥락을 축적할 때, **도구 레이어**에 추가:

```markdown
<!-- CLAUDE.md 발췌 -->
## 사용 가능 도구
- Claude Code (주 인터페이스)
- 로컬 uncensored MLX 모델 (http://127.0.0.1:8080/v1)
  - 사용 조건: 민감 데이터 분석, 합성 네거티브 샘플 생성, 완곡화 통제 필요 시
  - 호출 시점: CodeBook 적용, 혐오발언 분류, 번역 직역 비교
  - 기록: 모든 호출은 `logs/local_llm_calls.jsonl`에 저장 (재현성)
```

### 6.2. Harness Engineering

uncensored 서버 모드는 **하나의 harness 구성요소**로 편입됩니다:

```
[사용자 의도] → Claude Code (기획·검토·쓰기)
                    ↓
              [라우팅 판단]
              ↙          ↘
     Anthropic API    Local Uncensored
     (일반 작업)      (민감 데이터)
```

라우팅 규칙은 `AGENTS.md`에 명시:
> "민감 코퍼스 입력이 있거나, 완곡화가 결과를 왜곡할 수 있는 task는 로컬 모델로 라우팅한다."

### 6.3. Verification (검증부채 관리)

Kwon(2026)이 말하는 검증부채는 uncensored 모델에서 **더 커질 수 있음**:

- 정렬 모델은 "확신 없음"을 "죄송합니다"로 표시 → 연구자가 검증 필요 지점을 즉시 식별
- Uncensored 모델은 확신 없어도 **자신 있게 답변** → 환각을 놓치기 쉬움

**대응 프로토콜**:
1. 중요한 분석 결과는 **반드시 2개 이상 모델로 교차검증** (Claude/GPT + uncensored)
2. 원자료 근거(quote) 요구를 프롬프트에 내장
3. 정량 수치는 모델 답을 신뢰하지 말고 Python 코드로 재계산
4. `hands_on/scenario_comparison/` 방식으로 실제 교차검증 수행

---

## 7. 연구윤리·IRB·출판

### 7.1. IRB 신청서에 명시할 것

- **"AI 분석 단계"** 항목에 모델 상세 기재
  - 모델명, 양자화, 해시값
  - 실행 환경 (로컬/클라우드) — 로컬이면 "데이터 외부 전송 없음" 명시
  - 프롬프트 설계 원칙 (특히 "완곡화 방지 지침 포함" 등)
- 연구 참여자 동의서에 **"AI 분석 보조 사용" 조항** 추가
- 원자료와 AI 출력물을 **분리 보관**. AI 출력은 해석 보조이지 대체 자료가 아님을 기록

### 7.2. 논문 Methods 섹션에 명시할 것

권장 서술 템플릿:

> "질적 코딩 보조에는 MLX-LM 프레임워크에서 구동되는 `Jiunsong/supergemma4-26b-uncensored-mlx-4bit-v2` 모델(Gemma 3 27B의 4-bit 양자화 uncensored 변형)을 사용하였다. 추론은 Apple M4 로컬 환경에서 수행되어 원자료의 외부 네트워크 전송은 없었다. 프롬프트 설계, 재현성 파라미터(`temperature=0.0`, `seed=42`), 인간 코더와의 IRR은 부록 B 및 `analysis/` 디렉토리에 공개한다."

### 7.3. 리뷰어 예상 질문 대비

- Q: "왜 상용 모델이 아닌 uncensored 모델을 썼는가?"
  → A: 민감 주제에서 정렬 모델의 거부·완곡화가 코딩 일관성을 해침. 파일럿에서 aligned/uncensored 양쪽 테스트 결과 첨부.
- Q: "모델의 환각은 어떻게 통제했는가?"
  → A: (a) 모든 코드는 원문 quote 요구, (b) 샘플 N건을 인간 2인이 독립 코딩하여 IRR 계산, (c) 모델 단독 판정은 사용하지 않음.
- Q: "재현성은?"
  → A: 모델 해시, seed, 프롬프트 전체를 레포에 공개. 동일 하드웨어에서 비트 단위 재현 가능.

### 7.4. 기관 정책 체크리스트

- [ ] 소속 대학의 "생성형 AI 연구 활용 가이드라인" 최신본 확인
- [ ] 특히 "오픈소스 모델 사용"에 별도 조항이 있는지 (있는 대학 있음)
- [ ] 개인정보보호 담당자와 사전 상의 (특히 인터뷰·의료 데이터)
- [ ] 지도교수에게 방법 브리핑 + 서면 동의
- [ ] 학과·연구소 내부 세미나에서 방법 소개 (투명성)

---

## 8. 자주 하는 실수

### 8.1. "Uncensored니까 무조건 정확하겠지"
→ 아님. 오히려 환각률 상승 가능. 정량 수치, 인명·지명, 법조문은 **반드시 1차 출처로 검증**.

### 8.2. "모델이 거부하지 않으니 IRB는 필요 없겠지"
→ 틀림. IRB는 데이터 출처와 참여자 권리의 문제이지, 모델 검열 여부와 무관.

### 8.3. "시스템 프롬프트만 잘 쓰면 완전히 통제됨"
→ 완전 통제 불가. Prefix injection, 재시도, 인간 검토를 **다층**으로 두어야 함.

### 8.4. "API 비용 0원이니까 마음껏 돌리자"
→ 맞지만 **전기·배터리·SSD 수명**은 대가. 수만 건 배치는 밤에 돌리고 `caffeinate`로 절전 방지.

### 8.5. "한국어 데이터니까 한국어 강한 모델이 좋겠지"
→ 부분적으로만 맞음. 한국어 성인 문학 표현력은 이 모델이 우수하지만, **전문 용어(의학·법률)의 정확성은 Qwen 2.5/3 계열이 낫기도** 함. 태스크별 A/B 테스트 필수.

### 8.6. "로컬이니 완전 프라이빗"
→ 대체로 맞음. 단 생성물을 나중에 GPT에 넣어 편집하는 순간 외부 전송. 편집까지 로컬(Obsidian, VSCode) 유지.

### 8.7. "합성 데이터로 분류기 학습하면 실데이터 불필요"
→ 위험. 합성 데이터는 모델의 편향을 상속. 실데이터 최소 샘플 + 합성 확장이 안전.

---

## 9. 트러블슈팅

| 증상 | 원인 | 해결 |
|---|---|---|
| Metal OOM 크래시 | mlx 프로세스 중복 실행 | `ps aux \| grep mlx` 확인, 단일 프로세스 원칙 |
| 첫 실행 다운로드 느림 | HF 토큰 미설정 | `export HF_TOKEN=...`으로 인증시 속도↑ |
| 영어로 응답 | 시스템 프롬프트 약함 | "한국어 본문만 출력" 강조, prefix에 한국어 문장 |
| 응답 갑자기 끊김 | max_tokens 부족 + thinking 영어 선행 | 3000↑로 설정 |
| 모델이 추론 과정을 영어로 출력 | 이 모델의 thinking/channel 구조 | `<channel\|>` 이후 텍스트만 파싱 |
| Jupyter에서 느림 | 매 셀마다 모델 리로드 | `mlx_lm.server` 모드 + openai SDK |
| Claude Code 연동 실패 | 토큰 형식 불일치 | OpenAI 호환 모드이므로 `ANTHROPIC_BASE_URL` 대신 `OPENAI_BASE_URL` 사용 |

---

## 10. 다음 단계 — 본인 연구에 적용해 보기

### 10.1. 1일 차 — 환경 구축
1. MLX-LM 설치
2. 예시 모델 다운로드 (첫 1회만 오래 걸림)
3. `mlx_lm.chat`으로 한국어 한 문단 생성해보기

### 10.2. 1주 차 — 파일럿
1. 본인 연구의 작은 샘플(30건) 선정
2. 정렬 모델(ChatGPT 등) vs uncensored 모델 **동일 프롬프트**로 처리
3. 결과 비교 → 거부율, 완곡화, 정확도 표로 정리
4. 지도교수에게 파일럿 결과 브리핑

### 10.3. 1개월 차 — IRB·방법론 설계
1. 파일럿 결과를 근거로 IRB 신청서 작성·수정
2. 재현성 프로토콜 확정 (seed, 버전, 로깅 포맷)
3. 인간 코더와의 IRR 설계

### 10.4. 출판 준비
1. 방법론 섹션 초고 작성 (§7.2 템플릿 참조)
2. 분석 코드·프롬프트·로그를 OSF 또는 GitHub에 공개
3. 모델 해시 및 환경 정보 부록화

---

## 11. 참고 자료

### 11.1. 본 레포 내부
- `appendix/01_로컬AI_무료_활용_가이드.md` — Ollama 기반 일반 로컬 모델
- `hands_on/scenario_comparison/` — 4모델 교차검증 실제 결과
- `hands_on/templates/CLAUDE.md.filled_example` — 맥락 문서에 도구 등록 예시
- `demo/qualitative_research/` — 질적 연구 파이프라인 전체 사례

### 11.2. 외부 문서
- MLX-LM 공식: https://github.com/ml-explore/mlx-lm
- 모델 카드: https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-mlx-4bit-v2
- Hugging Face Uncensored 모델 개요: `huggingface.co/collections/mlabonne/abliteration-*`

### 11.3. 학술 참고
- Arditi et al. (2024), "Refusal in Language Models Is Mediated by a Single Direction" — abliteration 기법 이론 근거
- Zou et al. (2023), "Universal and Transferable Adversarial Attacks on Aligned Language Models" — 정렬 취약점
- 한국정보보호학회 연구윤리 가이드라인 (최신본)
- IRB 한국사회과학연구협의회 가이드 — 생성형 AI 활용 조항 (있는 경우)

### 11.4. 한국 법제·윤리
- 개인정보보호법 제15조·제17조 (개인정보 처리·제공)
- 생명윤리법 제10조·제36조 (인간대상연구 IRB)
- 각 대학 연구윤리 규정 — 생성형 AI 조항 유무 확인

---

## 12. 맺으며

Uncensored 모델의 가치는 **"더 과감한 출력"이 아니라 "연구 데이터 파이프라인에 모델 스스로의 의견·완곡·면책이 섞여 들어오는 것을 차단하는 것"**입니다.

정렬된 모델은 일반 사용자에게는 안전한 도구지만, 연구자에게는 **보이지 않는 편집자**가 될 수 있습니다. 편집자의 존재를 모르고 원고를 넘기면, 논문의 객관성이 그 편집자의 손끝에서 결정됩니다.

본 별첨의 목적은 "자유롭게 쓰세요"가 아니라 **"모델의 개입 지점을 파악하고, 도구 선택의 근거를 논문에 명시할 수 있게 하자"**입니다. 검증과 윤리의 무게는 오히려 더 커집니다.

---

**작성**: 2026-04-21 / 이요한 + Claude Code (Opus 4.7)
**라이선스**: CC BY-NC-SA 4.0
**문의**: yohan.harmony@gmail.com
**버전**: v1.0 — 초안
