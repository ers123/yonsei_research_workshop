# Thread Explosion Lesson

## 진단

thread가 많아지는 이유는 Codex multi-thread workflow의 필수 조건 때문이 아닙니다. 보통 다음이 섞일 때 발생합니다.

- 역할을 보여주기 위한 thread
- 실제 실행을 위한 thread
- phase별 추가 thread
- 지연 대응용 rerun thread
- packaging 같은 supervisor 업무를 worker로 분리한 thread

## 하지 말아야 할 것

- 새 단계가 나올 때마다 새 thread를 만들지 않는다.
- role thread와 execution thread를 따로 만들지 않는다.
- outline, drafting, revision을 모두 다른 thread로 쪼개지 않는다.
- packaging을 별도 worker로 두지 않는다.
- thread가 늦는다고 바로 새 thread를 만들지 않는다.

## 해야 할 것

- 시작 전에 thread budget을 정한다.
- 기본값은 supervisor 1개 + worker 5개다.
- 하나의 역할은 하나의 durable thread로 유지한다.
- 한 thread는 자기 반환 파일 하나를 책임진다.
- 새 thread는 새 전문성이 필요할 때만 만든다.
- phase가 아니라 판단 기능을 기준으로 나눈다.
- 지연이 생기면 checkpoint를 만들고, 뒤늦은 반환은 diff해서 반영한다.

## 학생에게 보여줄 설명

```text
많은 thread 목록은 가능성을 보여주기에는 좋지만, 학생이 따라 하기에는 복잡합니다. 실제 운영에서는 compact model로 시작하고, 새 전문성이 필요할 때만 thread를 추가합니다.
```
