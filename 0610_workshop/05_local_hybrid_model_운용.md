# 05. Local/Hybrid Model 운용

## 한 줄 설명

로컬 모델은 만능 대체재가 아니라, privacy, 비용, 반복 작업, 정책/업로드 제한을 다루기 위한 선택지입니다. 좋은 운영은 local과 cloud를 역할별로 나눕니다.

## 기본 원칙

```text
raw/private material: local 또는 human-only
sanitized summary: cloud 가능
draft prose: cloud 또는 strong local 가능
risk/privacy check: local second pass 권장
final approval: human-only
```

## 로컬에 두는 것이 좋은 것

- 참여자 단위 raw data
- 인터뷰 원문
- 실명, private link, 식별 가능한 파일명
- IRB/동의 관련 자료
- quotation approval 전 원문
- 민감한 연구 주제의 초기 탐색
- privacy-risk flagging
- 자료 inventory와 분류

## cloud model에 보낼 수 있는 것

사람이 확인한 뒤, 다음처럼 de-identified/sanitized된 자료는 cloud drafting에 쓸 수 있습니다.

- 연구 질문
- 익명화된 materials inventory
- 요약된 findings
- evidence binding table
- do-not-claim list
- source-verification 결과
- figure/table spec
- quote가 제거된 draft

## 작업별 routing

| 작업 | local | cloud/main | human |
|---|---|---|---|
| 파일 목록 분류 | primary | 불필요 | 확인 |
| privacy flag | primary | 보통 불필요 | 승인 |
| raw interview 요약 | local-only 권장 | 금지 또는 sanitized 후 | 승인 |
| evidence binding 점검 | primary/secondary | 가능 | 승인 |
| section architecture | 가능 | 유용 | 승인 |
| first draft | 가능 | 유용 | 검토 |
| critique | 다른 local model도 좋음 | 다른 cloud model도 좋음 | 결정 |
| rewrite | 가능 | 유용 | 검토 |
| figure/table spec | 가능 | 가능 | 승인 |
| empirical chart | deterministic code | 불필요 | data rule 승인 |
| quote/statistics/ethics | 보조만 가능 | 보조만 가능 | human-only |

## 로컬 모델의 장점

- 자료를 외부로 보내지 않는다.
- 짧고 반복적인 점검에 비용 부담이 적다.
- 여러 번 critique/risk pass를 돌리기 좋다.
- cloud model이 거부하거나 애매하게 답하는 민감 주제에서 초기 구조화에 도움될 수 있다.

## 로컬 모델의 한계

- 설치와 하드웨어 부담이 있다.
- 긴 문서 처리와 고품질 문장 생성은 cloud model보다 약할 수 있다.
- 작은 모델은 citation, 논리, 통계 표현을 쉽게 틀릴 수 있다.
- 느린 모델은 라이브 시연에 적합하지 않을 수 있다.

## 검열/정책 이슈를 설명하는 안전한 방식

로컬 모델은 "우회" 자체가 목적이 아닙니다. 연구에서는 민감자료, 정책적으로 애매한 주제, 비공개 코퍼스가 있을 수 있으므로, 외부 업로드 없이 초기 정리와 위험 점검을 하는 선택지로 설명합니다.

단, 다음은 여전히 human/legal/ethics gate입니다.

- 불법적 사용
- 개인정보 재식별
- 동의 범위를 벗어난 분석
- IRB 판단
- quote 공개
- 통계적 결론
- 외부 배포

## 실전 hybrid route

```text
1. raw/private material은 local-only 폴더에 둔다
2. local model 또는 수작업으로 sanitized summary를 만든다
3. 사람 검토 후 cloud model에 outline/draft를 맡긴다
4. 다른 local/cloud model로 critique를 돌린다
5. human-only gate에서 quote/statistics/ethics/circulation을 승인한다
6. ai-use-log에 어떤 모델을 어디에 썼는지 남긴다
```

## 핵심 문장

```text
로컬 모델을 쓰는 이유는 더 몰래 쓰기 위해서가 아니라, 연구자료의 경계와 책임을 더 명확히 하기 위해서입니다. cloud model은 좋은 문장을 만들 수 있지만, raw material과 최종 판단을 맡기면 안 됩니다.
```
