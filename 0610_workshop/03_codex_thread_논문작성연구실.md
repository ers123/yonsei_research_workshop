# 03. Codex Thread 기반 논문 작성 연구실

## 한 줄 설명

하나의 chat에 논문 전체를 맡기지 않고, supervisor thread가 여러 worker thread를 운영하는 방식입니다.

```text
Supervisor
  -> Evidence-Literature
  -> Data-Methods
  -> Visual-Assets
  -> Review-Verification
  -> Drafting
```

## 왜 thread를 나누는가

논문 작성에는 서로 다른 판단 기능이 섞여 있습니다.

- 문헌은 연구 위치와 gap을 봅니다.
- 데이터/방법은 어떤 claim을 허용하는지 봅니다.
- 시각화는 figure/table이 주장을 과장하지 않는지 봅니다.
- 검증자는 source, privacy, overclaim을 차단합니다.
- drafting은 통과된 claim만으로 초안을 씁니다.

이 판단들을 한 thread에 모두 넣으면 결과가 빨라 보일 수 있지만, 검증과 책임 경계가 흐려집니다.

## 권장 compact thread model

실제 시연에서는 thread를 너무 많이 만들지 않는 편이 좋습니다.

| Thread | 역할 | 반환 파일 |
|---|---|---|
| Supervisor | 전체 지휘, phase gate, 병합, human signoff | `threads/supervisor/merge-report.md` |
| Evidence-Literature | 문헌 위치, 이론 렌즈, 선행연구 gap, citation 후보 | `threads/evidence-literature/return.md` |
| Data-Methods | 데이터 readiness, 분석 가능 범위, 방법 한계 | `threads/data-methods/return.md` |
| Visual-Assets | 표/그림 식별, spec, caption, 안전 라벨 | `figures/visual-manifest.md` |
| Review-Verification | source gate, privacy gate, overclaim review | `threads/review-verification/return.md` |
| Drafting | outline, long-form draft, revision | `threads/drafting/return.md` |

Supervisor 1개 + worker 5개면 대부분의 수업/연구실 데모에는 충분합니다.

## Phase-gated 운영

```text
Phase 0: Supervisor intake
Phase 1: Evidence-Literature + Data-Methods + Visual-Assets 병렬
Phase 2: Review-Verification gate
Phase 3: Drafting
Phase 4: Review-Verification second pass
Phase 5: Supervisor merge and package
Phase 6: Human signoff
```

## Codex에서 worker thread를 실제로 여는 방식

Codex multi-thread 운영은 자동 병합 기능이 아니라, 별도 thread들을 만들고 supervisor가 결과를 읽어 병합하는 방식입니다.

수동 운영:

1. Supervisor thread를 먼저 만들고 phase plan을 확정합니다.
2. 같은 프로젝트 안에 Evidence-Literature, Data-Methods, Visual-Assets, Review-Verification, Drafting worker thread를 만듭니다.
3. `threads/thread-map.md`에 thread 제목, 역할, 반환 파일, 현재 상태를 기록합니다.
4. 각 worker에게 `Worker Common Contract`와 역할별 prompt를 보냅니다.
5. worker는 본문 파일을 직접 병합하지 않고 지정된 return file만 작성합니다.
6. Supervisor가 return file을 읽고 merge report와 human signoff checklist를 작성합니다.

Codex 앱 도구 기반 운영:

```text
create_thread -> worker thread 생성
send_message_to_thread -> 역할 prompt와 후속 지시 전달
read_thread -> worker 상태와 요약 확인
Supervisor merge -> 반환 파일을 읽고 하나의 검토 패키지로 병합
```

병렬로 파일을 수정해야 하면 별도 worktree를 쓰는 편이 안전합니다. 단순 분석이나 return file 작성만 시키는 경우에는 같은 프로젝트에서 운영해도 됩니다.

## thread를 더 만들기 전 질문

새 thread는 새 전문성이 있을 때만 만듭니다.

1. 기존 worker가 처리할 수 없는 판단인가?
2. 병렬로 독립 수행 가능한가?
3. 반환 파일이 하나로 명확한가?
4. 새 thread 없이는 검증 위험이 생기는가?
5. 학생에게 보여주기 어려울 만큼 목록이 길어지지 않는가?

하나라도 애매하면 기존 worker 안에서 처리합니다.

## return-file convention

각 worker는 자기 반환 파일 하나만 책임집니다.

```text
# [Worker Role] Return

## 핵심 3줄
## 사용한 입력
## 허용 가능한 주장 또는 산출물
## 제한해야 할 주장 또는 산출물
## draft/Word에 반영할 항목
## supervisor decision needed
```

이 규칙이 있어야 supervisor가 병합할 때 상태를 잃지 않습니다.

## fallback과 checkpoint

현실적인 multi-thread 운영에서는 모든 thread가 같은 속도로 끝나지 않습니다.

지연이 생기면 바로 새 thread를 만들지 않습니다.

1. 기존 thread에 반환 파일 작성을 한 번 더 요청합니다.
2. 그래도 늦으면 supervisor checkpoint를 만듭니다.
3. 새 thread가 필요하면 `rerun-1`처럼 표시합니다.
4. 늦게 온 반환물은 checkpoint와 비교해 반영합니다.

이것은 실패가 아니라 실제 연구 운영에서 필요한 상태 관리입니다.

## Visual-Assets thread를 따로 두는 이유

논문에서 figure/table은 장식이 아닙니다. 주장의 일부입니다.

Visual-Assets thread는 다음을 관리합니다.

- 어떤 표/그림이 필요한가?
- 그 그림은 어떤 claim을 보조하는가?
- empirical chart인지 conceptual diagram인지?
- raw/private screenshot이 들어가지는 않는가?
- causal proof처럼 읽히지는 않는가?
- caption과 alt text가 안전한가?
- Word/APA 원고에 어디에 들어가는가?

## 핵심 문장

```text
thread를 많이 만드는 것이 목표가 아닙니다. 중요한 것은 문헌, 데이터, 초안, 검증, 시각화 판단을 서로 다른 눈으로 보게 만드는 것입니다.
```

## 관련 파일

- [case_study/README.md](case_study/README.md)
- [case_study/thread_model_public.md](case_study/thread_model_public.md)
- [prompts/README.md](prompts/README.md)
- [templates/thread-return-template.md](templates/thread-return-template.md)
