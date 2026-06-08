# Live Demo Guide

## 데모 목표

이 데모는 "AI가 논문을 완성한다"를 보여주는 시간이 아닙니다.

보여줄 것은 다음입니다.

1. 자료를 먼저 정리한다.
2. 역할을 나눈다.
3. 각 thread가 반환 파일을 남긴다.
4. source gate가 claim을 통과/보류/차단한다.
5. draft와 review를 분리한다.
6. 최종 결과는 publication-ready가 아니라 review-ready package다.

## 보여주는 순서

### 1. 최종 패키지 먼저

먼저 결과물을 보여줍니다.

말할 내용:

```text
이 파일은 하나의 채팅창에서 한 번에 만든 논문이 아닙니다. Supervisor가 여러 worker thread 반환물을 모아 만든 검토용 패키지입니다.
```

### 2. thread model

열 파일:

- `case_study/thread_model_public.md`

말할 내용:

```text
처음에는 역할을 많이 나눠 보여줄 수도 있지만, 학생이 따라 할 기본형은 supervisor 하나와 worker 5개입니다.
```

### 3. handoff board

열 파일:

- `case_study/handoff_board_public.md`

말할 내용:

```text
각 phase가 끝날 때마다 무엇이 반환됐고, 다음 gate로 무엇을 넘길 수 있는지를 기록합니다.
```

### 4. prompt pack

열 파일:

- `prompts/README.md`

말할 내용:

```text
좋은 프롬프트는 긴 주문이 아니라, 역할, 입력, 금지사항, 반환 파일, gate를 명확히 하는 계약입니다.
```

### 5. templates

열 파일:

- `templates/AGENTS.md.example`
- `templates/ai-use-log.md`
- `templates/do-not-claim.md`

말할 내용:

```text
학생이 당장 시작하려면 프롬프트보다 먼저 이 세 파일을 채우는 것이 좋습니다.
```

## 보여주지 말아야 할 것

공개 수업이나 녹화에서 다음은 열지 않습니다.

- raw interview
- participant-level data
- private link
- 실명이나 식별 가능한 파일명
- quote approval 전 원문
- 통계 판단 전 raw chart
- 외부 배포 승인 전 full draft

## 라이브 시연 팁

- 긴 local model 실행을 실시간으로 기다리지 않습니다.
- 이미 생성된 return file을 열어 workflow를 설명합니다.
- thread가 많아진 과거 실행은 "실패 사례"로 짧게 설명하고, compact model을 권장합니다.
- 질문이 나오면 "이건 AI가 결정할 일이 아니라 human-only gate"라고 분리합니다.

## 데모 마무리 문장

```text
오늘 보여드린 것은 논문 자동작성기가 아니라, 연구자가 AI를 여러 역할로 나누어 쓰고 그 결과를 검토 가능한 패키지로 남기는 운영 방식입니다.
```
