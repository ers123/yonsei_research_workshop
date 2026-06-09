# Thread Explosion Postmortem

상태: 수업용 실패 사례 분석

## 한 줄 진단

thread가 많아진 이유는 Codex multi-thread workflow 자체의 필수 조건 때문이 아니라, "역할을 보여주기 위한 thread"와 "실제 실행을 위한 thread"를 분리해서 만들고, 그 뒤에 phase별 실행 thread와 재시도 thread까지 추가했기 때문이다.

## 실제로 무슨 일이 있었나

이번 데모는 처음에 "영상처럼 thread가 나뉘는 모습"을 보여주기 위해 role thread를 만들었다. 이 thread들은 literature-review, methods-evidence, data-readiness, source-verifier, outline, drafting, reviewer, packaging처럼 역할을 시각적으로 보여주는 목적이었다.

이후 사용자가 "다 하는 걸 보여줘야 한다"고 요청하면서, 실제 반환 보고서를 만들기 위한 execution thread를 추가로 만들었다. 이때 기존 role thread를 계속 사용하는 대신, `논문 연구실 실행 - ... return` 형태의 새 thread를 만들었다. 결과적으로 같은 역할에 대해 "역할 소개용 thread"와 "실행용 thread"가 동시에 남았다.

그 다음 outline, drafting, reviewer, revision, packaging처럼 순차적으로 진행해도 되는 phase까지 각각 별도 thread로 만들었다. 일부 thread의 반환이 늦어지자 verifier short return, outline short return 같은 재시도 또는 보조 실행 thread도 추가되었다. 이 과정에서 thread 목록이 연구 운영 구조보다 훨씬 길어졌다.

## 원인 분석

### 1. 시연 목적과 운영 목적이 섞였다

처음 목적은 "thread가 나뉘는 모습을 보여주기"였다. 그래서 역할별 thread를 많이 만드는 것이 시각적으로 도움이 된다고 판단했다. 하지만 실제 운영 목적은 "자료 기반 초안을 효율적으로 완성하기"다. 이 두 목적은 다르다.

시연 목적만 보면 많은 thread가 장점처럼 보인다. 그러나 운영 목적에서 보면 thread가 많아질수록 상태 추적, 반환 파일 확인, 중복 판단, 병합 비용이 커진다.

### 2. thread 예산을 정하지 않았다

처음부터 "supervisor 1개 + worker 5개를 넘지 않는다"는 제한이 없었다. thread cap이 없으면 역할을 발견할 때마다 새 thread를 만들기 쉽다. 문헌, 방법, 데이터, 그림, 검증, outline, drafting, review, revision, packaging을 모두 나누면 금방 10개가 된다.

### 3. role thread와 execution thread를 분리했다

역할을 보여주기 위해 만든 thread를 그대로 실행 thread로 재사용하지 않았다. 그래서 같은 역할에 대해 두 벌의 thread가 생겼다.

피해야 할 패턴:

- `논문 연구실 - literature-review 담당`
- `논문 연구실 실행 - literature return`

권장 패턴:

- `논문 연구실 - Evidence-Literature`
- 같은 thread 안에서 brief, return, revision 요청을 이어서 처리

### 4. phase를 expertise처럼 취급했다

outline, drafting, revision, packaging은 서로 다른 전문성이 아니라 같은 writing pipeline의 단계에 가깝다. 이 단계들을 모두 별도 thread로 만들면 thread 수는 늘지만 판단 품질이 비례해서 좋아지지 않는다.

권장 병합:

- outline + drafting + revision -> Drafting thread
- source-verifier + reviewer -> Review-Verification thread
- figure-table + image/caption check -> Visual-Assets thread
- packaging -> Supervisor의 최종 병합 업무

### 5. 지연 대응을 새 thread 생성으로 해결했다

일부 thread가 늦게 반환될 때 새 thread나 short return thread를 추가했다. 이 방식은 빠르게 다음 단계로 넘어가는 데는 도움이 되지만, 수업 화면에서는 중복 thread처럼 보인다.

더 나은 방식:

- 먼저 기존 thread에 "현재 반환 파일만 작성하라"고 후속 요청을 보낸다.
- 일정 시간 후에도 안 되면 supervisor checkpoint를 만든다.
- 새 thread를 만들 경우에는 `rerun-1`처럼 명확히 표시하고, 기존 thread를 archive하거나 "증거용"으로만 남긴다.

### 6. "보여주기 좋은 workflow"와 "학생이 따라 할 workflow"를 구분하지 않았다

이번 실행은 가능성을 검증하는 데는 좋았다. 하지만 학생이 그대로 따라 하면 thread가 과도하게 늘어난다. 발표용 workflow는 재현 가능하고 단순해야 한다. 따라서 수업에서는 이번 verbose execution을 "실험 로그"로 보여주고, 실제 권장 workflow는 compact model로 제시해야 한다.

## 학생들에게 말할 교훈

### 하지 말아야 할 것

- 새 단계가 나올 때마다 새 thread를 만들지 않는다.
- role thread와 execution thread를 따로 만들지 않는다.
- outline, drafting, revision을 모두 다른 thread로 쪼개지 않는다.
- packaging을 별도 worker thread로 두지 않는다. 최종 병합은 supervisor가 맡는다.
- thread가 늦는다고 바로 새 thread를 만들지 않는다.
- 이미지가 필요하다고 바로 image generation부터 하지 않는다.

### 해야 할 것

- 시작 전에 thread budget을 정한다.
- 기본값은 supervisor 1개 + worker 5개다.
- 하나의 역할은 하나의 durable thread로 유지한다.
- 한 thread는 자기 반환 파일 하나를 책임진다.
- 새 thread는 "새 전문성"이 필요할 때만 만든다.
- phase가 아니라 판단 기능을 기준으로 thread를 나눈다.
- 이미지와 도표는 Visual-Assets thread가 specification, prompt, caption, safety check를 먼저 만든다.
- 지연이 생기면 checkpoint를 만들고, 나중에 반환이 오면 diff해서 반영한다.

## 새 thread를 만들기 전 확인 질문

새 thread를 만들기 전에 supervisor는 아래 질문에 모두 답해야 한다.

1. 이 일은 기존 worker thread가 처리할 수 없는 별도 전문성인가?
2. 이 일이 다른 thread와 병렬로 독립 수행 가능한가?
3. 이 thread가 만들 반환 파일이 명확한가?
4. 이 thread를 만들지 않으면 병목이나 검증 위험이 생기는가?
5. thread 목록이 학생에게 보여주기 어려울 만큼 길어지지 않는가?

이 중 하나라도 "아니다"라면 새 thread를 만들지 말고 기존 thread 안에서 처리한다.

## 발표용 설명 문장

> 여기서 thread가 많이 생긴 것은 Codex를 잘 쓰면 반드시 이렇게 된다는 뜻이 아닙니다. 오히려 반대입니다. 처음에는 역할을 보여주려고 많이 쪼갰고, 이후 실제 실행 thread까지 추가하면서 목록이 길어졌습니다. 이건 학생들에게 보여줄 좋은 실패 사례입니다. 실제 운영에서는 supervisor 하나와 worker 5개 정도로 시작하고, 새 thread는 새 전문성이 필요할 때만 만듭니다.

## 수정된 권장 구조

| 권장 thread | 흡수하는 기존 역할 |
|---|---|
| Supervisor | packaging, final merge, checkpoint, human signoff |
| Evidence-Literature | literature-review, source context |
| Data-Methods | methods-evidence, data-readiness |
| Drafting | outline, drafting, revision |
| Review-Verification | source-verifier, reviewer |
| Visual-Assets | figure-table, image prompt, diagram, caption, visual privacy check |

## 이번 기존 thread의 보존 방식

기존 thread는 삭제하지 않는다. 수업에서는 다음 순서로 보여준다.

1. 먼저 스크린샷 또는 `live-thread-map.md`로 verbose execution log를 보여준다.
2. "이렇게 하면 목록이 길어져 관리가 어려워진다"고 설명한다.
3. `compact-thread-model.md`를 열어 수정된 권장 모델을 보여준다.
4. 기존 thread 산출물은 proof-of-work로 남기고, 새 프로젝트에서는 compact model만 사용한다고 설명한다.
