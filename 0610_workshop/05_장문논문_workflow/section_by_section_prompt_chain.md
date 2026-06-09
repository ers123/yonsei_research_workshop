# Section-by-Section Prompt Chain

장문 논문은 하나의 긴 프롬프트가 아니라 반복 가능한 prompt chain으로 작성합니다.

## Chain Overview

```text
학습만 하기
  -> 제목 후보
  -> 상세 목차
  -> paragraph unit table
  -> unit 작성
  -> unit 검토
  -> unit 수정
  -> section 통합
  -> section critique
```

## 1. Unit 작성

```text
아래 Unit ID 하나만 작성하세요.

Unit ID:
[예: 2.1.3]

문단 기능:
[예: 자기조절 이론이 DSB 초안의 intervention logic과 어떻게 연결되는지 설명]

사용 가능한 자료:
[자료명 또는 evidence binding ID]

금지:
- 다음 unit 작성 금지
- 장 전체 작성 금지
- 자료에 없는 문헌/통계/quote 생성 금지
- citation처럼 보이는 가짜 reference 생성 금지

출력:
## Draft Unit

## Evidence Used

## Citation / Reference Status

## Risks
```

## 2. Unit 검토

```text
방금 작성한 unit을 evidence binding 기준으로 검토하세요.

검토:
1. 근거 없는 claim
2. citation needed 누락
3. 과장된 일반화
4. 이전 unit과의 연결 문제
5. 다음 unit으로 넘겨야 할 내용이 섞였는지

출력 표:
| Location | Issue | Fix | Status |
|---|---|---|---|

마지막에 gate를 표시하세요.
Gate: go / revise / stop
```

## 3. Unit 수정

```text
위 검토 결과를 반영해 같은 Unit ID만 수정하세요.

규칙:
- 새 자료를 만들지 마세요.
- blocked claim은 삭제하세요.
- needs verification은 본문에서 단정하지 말고 표시하세요.
- 수정 후 Evidence Used와 Citation / Reference Status를 다시 제시하세요.
```

## 4. Section 통합

한 section의 모든 unit이 통과한 뒤에만 실행합니다.

```text
아래 unit들을 하나의 section draft로 통합하세요.

규칙:
- unit 내용을 무리하게 늘리지 마세요.
- 중복 문장을 줄이세요.
- heading과 paragraph 흐름을 정리하세요.
- citation needed 표시를 보존하세요.
- 새 claim을 추가하지 마세요.

입력 unit:
[unit 2.1.1]
[unit 2.1.2]
[unit 2.1.3]

출력:
## Section Draft
## Removed Duplication
## Remaining Citation Needs
## Human Review Needed
```

## 5. Section critique

```text
아래 section draft를 장문 논문 기준으로 비평하세요.

기준:
1. 논리 흐름
2. 근거 연결
3. 인용 상태
4. 반복 또는 filler
5. 다음 section과의 연결
6. human-only decision

출력:
| Severity | Issue | Evidence | Suggested Revision |
|---|---|---|---|

마지막에 section 상태를 표시하세요.
Status: usable / revise / blocked
```
