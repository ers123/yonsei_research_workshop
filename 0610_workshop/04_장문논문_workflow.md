# 04. 장문 논문 Workflow

## 한 줄 설명

긴 논문은 한 번에 쓰지 않습니다. 먼저 AI 세션에 선행연구 흐름과 연구자의 논리를 검토시키고, 답변 생성을 막은 뒤, 제목, 목차, section flow, paragraph unit 순서로 좁혀서 씁니다.

```text
학습 먼저, 답변은 나중
```

## 언제 쓰나

- 학위논문처럼 긴 분량 요구가 있다.
- 선행연구 흐름을 충분히 반영해야 한다.
- "서론 써줘"라고 하면 내용이 얕고 산만해진다.
- 기존 논문과 차별화된 제목/목차가 필요하다.
- 문단마다 citation과 source boundary를 관리하고 싶다.

## 준비물

| 준비물 | 설명 |
|---|---|
| tentative RQ | 아직 확정 전이어도 좋지만 방향은 있어야 함 |
| literature-flow reports | 흐름별 대표 논문, 개념, 방법, 한계, 현재 연구와의 연결 |
| bibliography 후보 | Zotero, EndNote, BibTeX, 수기 목록 모두 가능 |
| do-not-claim list | 아직 말하면 안 되는 주장 |
| 학교/학과 형식 | 5장 구조, 인용양식, 분량 |
| human decision log | 제목, 목차, 인용, 방법 선택 기록 |

## 전체 workflow

```text
1. literature-flow report를 만든다
2. AI 세션에 "검토만 하고 답변하지 말라"고 지시한다
3. 흐름별 보고서를 순서대로 넣는다
4. 제목 후보 2-3개만 받는다
5. 연구자가 제목을 선택/수정한다
6. 5장 구조 목차를 받는다
7. section flow를 문단 단위로 쪼갠다
8. paragraph unit 하나씩 작성한다
9. citation/reference matching을 한다
10. 연구자가 논리와 문체를 개정한다
```

## 하지 말아야 할 요청

```text
서론 20페이지 써줘.
```

```text
이 주제로 박사논문 전체 써줘.
```

```text
인용도 알아서 넣어줘.
```

이런 요청은 길어 보이는 글을 만들 수는 있지만, 근거와 논리 구조가 쉽게 무너집니다.

## 좋은 요청

```text
아직 본문은 쓰지 마라.
이 section을 paragraph unit으로 나누고, 각 unit의 목적, 중심 메시지, 필요한 citation, 다음 문단으로 넘어가는 transition만 제안해라.
```

## paragraph unit 방식

긴 논문은 section이 아니라 paragraph unit으로 관리합니다.

| 항목 | 설명 |
|---|---|
| purpose | 이 문단이 하는 일 |
| central message | 하나의 중심 메시지 |
| source boundary | 어떤 literature-flow report만 사용할지 |
| citation need | 필요한 citation |
| length | 짧게/자세히/몇 문장 |
| transition | 다음 문단으로 넘어가는 연결 |

## citation matching

AI가 source-only라고 해도 citation은 검증해야 합니다.

각 문단 뒤에 다음 표를 붙이게 합니다.

| citation | source report | 원 논문 정보 | status |
|---|---|---|---|
| Author (Year) | literature-flow 1 | 확인됨/확인 필요 | pass/needs verification |

확인되지 않은 reference는 지어내지 않고 `needs verification`으로 둡니다.

## 분량을 늘리는 안전한 방법

관련 없는 말을 추가하지 않습니다. paragraph unit을 더 세밀하게 나눕니다.

나쁜 방법:

- 같은 말을 반복한다.
- 새로운 literature를 만들어낸다.
- 통계/인과/효과 주장을 확장한다.

좋은 방법:

- 선행연구 흐름을 더 세분화한다.
- 개념 정의, 방법 차이, 연구 gap을 분리한다.
- 현재 연구의 contribution과 limitation을 별도 문단으로 둔다.
- 각 문단의 source boundary를 유지한다.

## 핵심 문장

```text
장문 논문 작성에서 AI의 가치는 긴 글을 한 번에 뽑는 데 있지 않습니다. 먼저 AI가 연구자의 선행연구 흐름을 이해하게 만들고, 그 다음 가장 작은 문단 단위로 통제하는 데 있습니다.
```
