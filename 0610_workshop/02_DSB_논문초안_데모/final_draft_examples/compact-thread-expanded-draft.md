상태: compact-run supervisor-merged long-form exploratory draft

# 바가 보일 때, 아이는 스스로 멈출 수 있을까

## 스크린타임-신체활동 연동형 시각 인터페이스를 통한 아동 자기조절 지원 가능성의 탐색적 분석

### 사용 범위

이 문서는 `Supervisor + 5 worker threads` compact run의 반환물을 병합해 작성한 수업용 long-form draft이다. 기존 `paper-project/draft/expanded-revised-draft.md`를 버리지 않고, Evidence-Literature, Data-Methods, Drafting, Review-Verification, Visual-Assets worker가 제안한 보강점을 반영했다. 이 문서는 투고용 완성 원고가 아니며, 외부 공유 또는 투고 전에는 참고문헌 원문 대조, 정량 분석 재검증, 정성 코딩, 개인정보 검토, 공동연구자 human signoff가 필요하다.

## 초록

아동의 스마트폰 사용 조절과 신체활동 증진은 흔히 별도의 문제로 다루어진다. 한쪽에서는 screen time을 줄이는 제한 전략이 강조되고, 다른 한쪽에서는 physical activity를 늘리는 동기화 전략이 강조된다. 그러나 실제 가정의 일상에서 두 행동은 같은 시간, 같은 규칙, 같은 가족 협상 안에서 함께 나타난다. 본 초안은 screen time과 physical activity를 하나의 bar interface로 연결한 디자인 개입을 대상으로, 이 시각적 연결이 아동의 자기조절 지원 가능성을 어떻게 탐색하게 하는지 다룬다.

본 초안은 효과 검증 연구가 아니라 AI-assisted exploratory draft이다. 정량 자료는 intervention date가 확인되는 분석 가능한 18명의 pre/post 기술통계로 제한했다. 평균 일일 screen time은 pre period 97.7분에서 post period 71.2분으로 낮아지는 관찰 경향을 보였고, 18명 중 11명에서 감소 방향이 관찰되었다. 평균 일일 steps는 9,454보에서 9,855보로 소폭 높아지는 관찰 경향을 보였으며, 18명 중 11명에서 증가 방향이 관찰되었다. 이 결과는 통계적 효과, 인과효과, 대조군 비교, 일반화의 근거가 아니다.

정성 자료는 raw transcript나 직접 인용이 아니라 researcher memo-based theme 수준으로만 사용했다. theme은 bar visibility, planning/self-monitoring, parent-led control에서 child-led management로의 이동 가능성, incentive와 penalty가 만드는 경계조건을 중심으로 정리했다. Perceived behavioral control은 측정된 outcome이 아니라 해석 렌즈로 사용했다. 결과적으로 본 초안은 bar-based interface가 아동의 자기조절을 확정적으로 개선한다고 주장하지 않는다. 대신 screen time과 physical activity를 연결해 보이게 만드는 디자인이 어떤 가능성과 위험을 동시에 갖는지, 그리고 후속 연구에서 어떤 검증이 필요한지를 제시한다.

Keywords: screen time, physical activity, self-regulation, feedback, feedforward, perceived behavioral control, child-computer interaction, behavior change design

## 1. 서론

### 1.1 문제 배경

아동의 디지털 기기 사용은 가정, 학교, 또래 관계, 여가 활동과 밀접하게 연결되어 있다. 스마트폰은 단순한 오락 도구가 아니라 소통, 정보 접근, 휴식, 게임, 학습의 매개가 된다. 따라서 screen time을 줄이는 문제는 단순히 사용을 금지할 것인가의 문제가 아니다. 아동이 언제, 왜, 얼마나, 어떤 맥락에서 스마트폰을 사용하는지 이해해야 하며, 부모와 아동이 그 사용을 어떻게 협상하는지도 함께 보아야 한다.

신체활동 역시 별도의 건강 행동으로만 보기 어렵다. 아동이 더 많이 움직일 수 있는지는 시간표, 주거 환경, 부모의 기대, 학교 일정, 친구 관계, 날씨, 동기, 피로도에 영향을 받는다. 어떤 아동에게는 운동이 즐거운 놀이일 수 있지만, 다른 아동에게는 추가 과제처럼 느껴질 수 있다. 따라서 screen time 감소와 physical activity 증가는 서로 독립된 목표가 아니라, 같은 생활 리듬 안에서 충돌하거나 보완되는 행동으로 이해할 필요가 있다.

기존 가정 기반 관리 방식은 부모 주도의 제한에 의존하는 경우가 많다. 부모가 사용 시간을 정하고, 특정 시간이 지나면 기기 접근을 제한하는 방식이다. 이러한 방식은 즉각적인 통제에는 도움이 될 수 있다. 그러나 아동이 자신의 사용 상태를 이해하고 계획하는 경험을 충분히 제공하지 못할 수 있다. 특히 부모가 계속 감시하고 개입해야 한다면, 사용 조절은 아동의 자기관리라기보다 외부 통제에 가까워진다.

본 초안이 주목하는 지점은 screen time과 physical activity 중 어느 하나를 별도로 조정하는 것이 아니라, 두 행동이 같은 일상 규칙 안에서 어떻게 서로를 설명하고 제한하고 보완하는지이다. screen time 제한과 activity 증진을 별도로 설계하면 아동이 실제로 마주하는 선택 구조를 놓칠 수 있다. 아동은 "스마트폰을 얼마나 썼는가"와 "몸을 얼마나 움직였는가"를 따로 경험하지 않는다. 두 행동은 하루의 시간, 부모의 규칙, 놀이와 휴식, 보상과 제한의 구조 안에서 함께 해석된다.

bar-based visual interface는 이 지점에서 다른 가능성을 제안한다. screen time과 physical activity를 하나의 bar로 연결하면, 아동은 자신이 이미 사용한 시간과 앞으로 확보하거나 조절해야 할 행동을 한 화면에서 볼 수 있다. 이 시각화는 사용량을 숨겨진 계산이나 부모의 지시가 아니라, 아동이 직접 읽을 수 있는 상태 정보로 바꾼다.

### 1.2 연구 gap

본 초안의 연구 gap은 아동의 screen time을 줄이는 도구가 필요한가, 또는 physical activity를 늘리는 보상이 필요한가에만 있지 않다. 더 구체적인 gap은 두 행동이 같은 일상 시간과 가족 규칙 안에서 함께 조절될 때, 아동이 그 관계를 어떻게 이해하고 자기 행동의 다음 선택으로 연결할 수 있는가에 있다.

기존 제한형 접근은 사용 가능 여부를 외부에서 통제하는 데 초점이 있다. 반대로 활동 증진 접근은 움직임을 늘리는 동기화에 초점을 둘 수 있다. 본 초안은 이 둘을 경쟁 관계로 두지 않고, screen time과 physical activity의 관계를 아동이 실시간 시각 상태로 보고 자기조절 판단을 구성할 수 있는지를 탐색한다. 따라서 bar interface는 단순한 사용량 표시가 아니라, 아동이 자신의 선택지를 읽을 수 있게 만드는 생활 리듬의 시각화로 다루어진다.

### 1.3 연구 목적과 질문

본 초안의 목적은 시스템의 효과를 확정하는 것이 아니다. 현재 자료는 탐색적 분석과 수업용 시연에는 사용할 수 있지만, 통계적 효과나 인과관계를 주장하기에는 제한이 있다. 따라서 연구 목적은 세 가지로 제한한다.

첫째, intervention date가 확인되는 분석 가능한 18명의 일별 기록에서 screen time과 steps의 pre/post 기술통계가 어떤 관찰 경향을 보이는지 정리한다. 둘째, researcher memo-based theme을 바탕으로 bar visibility가 planning, self-monitoring, parent-led control에서 child-led management로의 이동 가능성과 어떻게 연결될 수 있는지 해석한다. 셋째, feedback, feedforward, incentive, penalty가 결합된 디자인이 자기조절 scaffold로 작동할 수 있는 가능성과 동시에 가질 수 있는 위험을 논의한다.

본 초안은 다음 질문을 중심으로 구성한다.

1. 분석 가능한 18명의 pre/post 기술통계에서 screen time과 steps는 어떤 관찰 경향을 보이는가?
2. bar visibility는 아동의 planning과 self-monitoring 가능성을 어떻게 지원하는 디자인 요소로 해석될 수 있는가?
3. parent-led control에서 child-led management로의 이동 가능성은 researcher memo-based theme 수준에서 어떻게 나타나는가?
4. feedback, feedforward, incentive, penalty가 결합된 시스템은 어떤 경계조건과 후속 검증 과제를 갖는가?
5. compact multi-thread workflow는 자료 기반 논문 초안을 만들 때 어떤 검증과 제한 장치를 제공할 수 있는가?

## 2. 이론적 배경

### 2.1 Screen Time과 Physical Activity를 연결해서 보기

screen time과 physical activity는 종종 반대 방향의 행동처럼 설명된다. screen time은 앉아서 화면을 보는 시간이고, physical activity는 몸을 움직이는 시간이라는 식이다. 그러나 실제 생활에서는 두 행동이 단순히 한쪽이 늘면 다른 한쪽이 줄어드는 기계적 관계로만 나타나지 않는다. 어떤 아동은 활동량이 많아도 특정 시간대에 스마트폰을 많이 사용할 수 있고, 어떤 아동은 스마트폰 사용을 줄이더라도 반드시 활동량이 늘어나지 않을 수 있다.

따라서 본 초안은 screen time reduction과 physical activity promotion을 각각 독립된 outcome으로만 보지 않는다. 두 행동은 시간 배분, 자기조절, 가족 규칙, 보상 구조 안에서 연결된다. 이 연결을 보이게 하는 디자인은 아동에게 현재 상태를 이해할 수 있는 단서를 제공할 수 있다. 중요한 것은 단순히 덜 쓰게 만들기나 더 걷게 만들기가 아니라, 아동이 자신의 행동 사이의 관계를 파악하고 선택할 수 있는 환경을 만드는 것이다.

이 관점에서 bar interface는 행동 데이터를 시각적으로 압축하는 장치다. screen time은 이미 사용한 시간으로 나타나고, physical activity는 앞으로 확보할 수 있는 가능성 또는 조절 자원으로 나타난다. 하나의 bar가 두 행동을 함께 보여주면, 아동은 두 행동을 별도 규칙이 아니라 하나의 상태 체계로 이해할 수 있다.

### 2.2 Feedback과 Feedforward

feedback은 사용자가 이미 수행한 행동의 결과를 알려주는 기능이다. screen time 관리에서 feedback은 오늘 얼마나 사용했는지, 제한에 얼마나 가까워졌는지, 규칙을 넘었는지를 보여줄 수 있다. 그러나 feedback만으로는 앞으로 무엇을 해야 하는지까지 충분히 알려주지 못할 수 있다. 사용자가 이미 많이 썼다는 사실은 알지만, 그다음 행동을 어떻게 선택해야 하는지는 별도의 판단이 필요하다.

feedforward는 앞으로의 가능성과 필요한 행동을 미리 보여주는 기능이다. 예를 들어 더 사용하려면 어느 정도 움직여야 하는지, 현재 상태를 유지하면 어느 시점에 제한이 걸리는지, 어떤 선택이 다음 상태를 바꾸는지 알려줄 수 있다. 본 시스템의 bar는 feedback과 feedforward를 동시에 결합한다. 이미 사용한 screen time을 보여주는 동시에, physical activity와 연결된 앞으로의 조절 가능성을 드러내기 때문이다.

이론적으로 bar interface는 feedback과 feedforward를 연결하는 시각적 scaffold로 해석할 수 있다. feedback은 아동에게 이미 사용한 screen time과 현재 상태를 알려주고, feedforward는 앞으로 더 움직이거나 덜 사용하는 선택이 다음 상태를 어떻게 바꿀 수 있는지 예상하게 한다. 자기조절은 과거 행동을 확인하는 데서 끝나지 않는다. 현재 상태를 해석하고, 다음 행동을 예상하고, 목표와 규칙을 바탕으로 선택을 수정하는 과정이다.

### 2.3 Incentive와 Penalty

incentive는 원하는 행동을 강화하기 위해 보상을 연결하는 전략이다. 본 시스템에서는 physical activity가 screen time 사용 가능성과 연결될 수 있다. 이 구조는 아동에게 더 움직일 이유를 제공할 수 있다. 하지만 incentive는 항상 긍정적인 효과만 갖지 않는다. 운동이 건강, 놀이, 성취의 경험이 아니라 screen time을 얻기 위한 수단으로만 이해될 위험이 있다.

penalty는 규칙을 넘었을 때 제한이나 손실을 부여하는 전략이다. 사용 가능 시간이 소진되었을 때 추가 사용이 제한된다면, 이는 과도한 사용을 멈추는 신호로 작동할 수 있다. 그러나 penalty 역시 자율성에 긴장을 만들 수 있다. 아동이 제한을 부당하게 느끼거나, 규칙을 회피하려 하거나, 부모와 갈등할 가능성도 있다.

incentive와 penalty는 본 시스템의 행동 조절 논리를 구성하지만, 자율성 기반 개입과 긴장 관계에 있다. 더 움직이면 더 사용할 수 있다는 incentive는 단기 행동 조절에는 도움을 줄 수 있으나, physical activity를 screen time 획득 비용으로 도구화할 위험이 있다. 반대로 penalty는 과도한 사용을 멈추는 명확한 신호가 될 수 있지만, 아동이 규칙을 외부 통제로만 경험하면 자기조절 scaffold가 아니라 새로운 갈등 조건으로 작동할 수 있다.

### 2.4 Perceived Behavioral Control의 위치

Perceived behavioral control은 본 초안에서 측정된 outcome이 아니라 해석 렌즈다. 현재 자료에는 PBC를 측정한 별도 척도나 validated questionnaire 결과가 확인되어 있지 않다. 따라서 PBC가 향상되었다거나 통제감이 증가했다고 주장할 수 없다.

대신 본 초안은 PBC 관점에서 bar visibility를 해석한다. 아동이 자신에게 조절 가능한 행동 범위를 볼 수 있다면, 사용 상태를 더 명확히 이해하고 선택지를 인식할 가능성이 있다. 예를 들어 더 움직이면 사용 가능성이 달라진다는 구조, 또는 덜 사용하면 제한에 도달하지 않는다는 구조가 보이면, 아동은 자신의 행동이 다음 상태에 연결된다고 해석할 수 있다.

그러나 이 가능성은 균일하지 않다. 어떤 아동은 bar를 보고 활동량을 늘릴 수 있고, 어떤 아동은 활동 부담이 커서 사용 자체를 줄일 수 있다. 또 어떤 아동은 가족 규칙이나 생활 맥락 때문에 큰 변화를 보이지 않을 수 있다. 따라서 PBC는 결과 claim이 아니라 개인차를 해석하는 lens로 제한해야 한다.

앞의 논의가 개별 디자인 전략을 나누어 설명했다면, 본 연구의 bar-based interface는 그 전략들이 하나의 화면 상태 안에서 결합될 때 어떤 자기조절 해석이 가능한지를 보여주는 사례다. 즉 bar는 feedback, feedforward, incentive, penalty를 따로 배열하는 기능 목록이 아니라, 아동이 현재 상태와 다음 선택을 함께 읽도록 만드는 통합된 시각 단서로 이해할 수 있다.

## 3. 연구 맥락과 개입 설명

### 3.1 Bar-Based Visual Interface

본 연구가 다루는 개입은 screen time과 physical activity를 하나의 시각적 bar로 연결한다. bar는 사용된 screen time, 남은 가능성, 활동을 통해 확보할 수 있는 사용 가능성을 시각적으로 보여주는 장치로 해석할 수 있다. 이 인터페이스는 아동이 별도의 통계 화면을 열지 않아도 자신의 상태를 직관적으로 파악하도록 돕는다.

개입의 핵심은 네 가지 디자인 전략의 결합이다. feedback은 이미 사용한 screen time을 보여준다. feedforward는 앞으로 필요한 활동이나 사용 조절을 예상하게 한다. incentive는 신체활동과 사용 가능성을 연결한다. penalty는 사용 가능 시간이 소진되었을 때 제한을 만든다. 이 네 가지 전략은 독립적으로 작동하기보다, 하나의 bar interface 안에서 함께 해석된다.

bar가 보여주는 것은 단순한 수치가 아니다. 아동은 bar를 통해 이미 사용한 시간, 앞으로의 사용 가능성, 더 움직이거나 덜 사용하는 선택이 다음 상태를 어떻게 바꿀 수 있는지를 함께 읽을 수 있다. 이 점에서 bar는 부모의 직접 지시를 대체하는 확정적 해결책이 아니라, 아동이 자기 상태를 이해하고 다음 선택을 생각하게 하는 시각적 scaffold로 해석된다.

### 3.2 Figure 1 배치 계획

본문의 이 위치에는 Figure 1을 배치하는 것이 적절하다. Figure 1은 실제 앱 screenshot이 아니라 concept diagram이어야 한다. 개념도는 screen time, physical activity, bar interface, feedback, feedforward, incentive, penalty가 어떻게 연결되는지 보여준다. 실제 참여자 화면, private screenshot, 식별 가능한 기기 정보는 포함하지 않는다.

Figure 1 is specified as a concept diagram rather than a screenshot because the classroom package excludes private app screens, participant identifiers, and raw device images. Its purpose is to explain the intervention structure, not to document a participant experience.

## 4. 연구 방법

### 4.1 연구 설계

본 초안은 mixed-method exploratory draft이다. 정량 자료는 intervention date를 기준으로 pre period와 post period를 나누어 기술통계로 요약했다. 정성 자료는 formal coding 결과가 아니라 researcher memo-based theme synthesis로 제한했다. 본 문서는 AI-assisted multi-thread workflow를 통해 작성된 수업용 source-gated draft이며, 투고용 완성 원고가 아니다.

pre period는 intervention date 이전으로, post period는 intervention date 당일 및 이후로 정의했다. 이 정의는 자료를 정리하기 위한 실무적 기준이지만, intervention date 당일이 baseline과 post 상태를 명확히 분리하지 못할 수 있다. 따라서 결과를 인과적으로 해석하는 것은 적절하지 않다.

### 4.2 자료와 분석 가능 범위

정량 파일 전체에는 2,341개 일별 기록과 19명의 참여자 정보가 포함되어 있다. 그러나 pre/post 비교에는 intervention date가 확인되는 분석 가능한 18명만 포함했다. 1명의 제외는 자료 자체의 가치 판단이 아니라, intervention date를 기준으로 pre/post 비교 가능성을 확보할 수 없다는 제한 때문이다.

정량 자료의 분석 단위는 participant-level 효과 추정이 아니라 daily record를 집계한 pre/post 기술통계이다. Screen time은 초 단위 값을 분 단위로 변환해 요약했다. Steps 평균은 기존 분석 메모에 따라 `steps == 0` 행을 제외해 계산했지만, zero-step 값이 실제 무활동인지 기록 실패인지 현재 자료만으로 구분할 수 없기 때문에 후속 민감도 분석이 필요하다.

자료에는 missing screen-time 555행, missing steps 67행, zero-step 211행이 존재한다. 본 초안은 이 문제를 해결했다고 주장하지 않는다. Missing screen-time은 일별 평균과 추세 해석의 제한을 만들 수 있고, missing steps와 zero-step rows는 step outcome의 recording validity 문제와 연결된다. 결측 원인은 현재 자료만으로 확정하지 않는다.

정성 자료는 interview data structure와 연구자 메모를 바탕으로 theme 수준에서만 사용했다. 원문 발화, 실명, 참여자별 사례, private link, 식별 가능한 파일명은 수업용 초안에 포함하지 않는다. 직접 인용을 사용하려면 별도의 익명화, 동의, 맥락 검토가 필요하다.

### 4.3 분석 절차

정량 분석은 세 단계로 제한했다. 첫째, intervention date가 확인되는 참여자만 분석 가능 subset으로 분리했다. 둘째, screen time과 steps를 pre/post period로 나누어 평균값을 계산했다. 셋째, 각 지표에서 기대 방향 변화가 관찰된 참여자 수를 집계 수준으로 요약했다. 이 과정에서 통계 검정, 대조군 비교, 개인별 trajectory 분석은 수행하지 않았다.

정성 분석은 formal coding이 아니라 theme synthesis다. 자료에서 bar visibility, planning/self-monitoring, parent-led control에서 child-led management로의 이동 가능성, incentive/penalty의 경계조건을 중심으로 연구자 메모 수준의 theme을 정리했다. 이 theme은 후속 정성 분석의 출발점이지, 확정된 질적 결과가 아니다.

이러한 분석 절차 때문에 결과 section은 변화의 원인을 확정하기보다, 현재 자료 안에서 관찰 가능한 집계 패턴과 theme 수준의 해석 가능성을 분리해 제시한다. 수치 결과는 기술통계로, 정성 결과는 researcher memo-based theme으로 읽어야 하며, 두 자료는 서로를 입증하는 관계가 아니라 후속 검증 질문을 좁히는 관계로 사용된다.

### 4.4 Analysis-Ready but Not Inference-Ready

본 자료는 classroom-facing exploratory draft를 위한 analysis-ready summary로는 사용할 수 있지만, inference-ready dataset으로 보기는 어렵다. Intervention date가 있는 18명에 대해 pre/post 기술통계는 산출할 수 있으나, 결측, zero-step 처리, 참여자별 관찰 기간 차이, clean control group 부재, formal qualitative coding 미완료가 남아 있다. 따라서 현재 draft의 역할은 효과 검증이 아니라 후속 검증이 필요한 패턴과 방법상 쟁점을 정리하는 데 있다.

### 4.5 Compact Multi-Thread 작성 절차

본 초안은 Codex compact multi-thread workflow를 통해 보강되었다. Supervisor thread는 현재 대화로 유지했고, worker thread는 Evidence-Literature, Data-Methods, Drafting, Review-Verification, Visual-Assets의 5개로 제한했다. 각 worker는 기존 확장 원고를 자기 전문 관점에서 furthering했고, 하나의 반환 파일만 작성했다.

이 workflow는 empirical finding이 아니다. 연구 결과의 타당성을 자동으로 높이는 방법론으로 주장하지 않는다. 대신 이 workflow는 수업용 작성 절차의 투명성을 높이고, 문헌 framing, 데이터 한계, 초안 구조, source/privacy gate, visual safety를 분리해 검토하는 운영 방식으로 제시된다.

### 4.6 개인정보와 수업용 안전 기준

수업용 산출물에는 집계값과 evidence binding만 사용한다. 참여자별 궤적, raw transcript, raw quote, 실명, private link, 민감 문자열, 원자료 screenshot은 제외한다. 표와 그림도 동일한 원칙을 따른다. 집계형 표, 개념도, interpretive mechanism map은 허용할 수 있지만, 개인별 line chart나 raw screenshot 기반 이미지는 포함하지 않는다.

## 5. 결과

### 5.1 정량 자료의 기술적 패턴

분석 가능한 18명의 pre/post 기술통계에서 평균 일일 screen time은 pre period 97.7분에서 post period 71.2분으로 낮아지는 관찰 경향을 보였다. 방향성 요약에서는 18명 중 11명에서 평균 screen time 감소 방향이 관찰되었다. 이 결과는 집계 수준의 descriptive pattern이며, 통계적 유의성이나 인과효과를 의미하지 않는다.

평균 일일 steps는 pre period 9,454보에서 post period 9,855보로 소폭 높아지는 관찰 경향을 보였다. 18명 중 11명에서 steps 증가 방향이 관찰되었지만, 평균 증가 폭은 작고 개인차가 컸다. 따라서 이 결과를 신체활동 증진 효과로 표현하는 것은 적절하지 않다. 더 보수적으로는 screen time과 steps에서 기대 방향의 관찰 패턴이 일부 나타났다고 정리해야 한다.

아래 수치는 missing values와 zero-step handling이 존재하는 available records 기반의 집계 요약이다. 따라서 평균 변화는 관찰 경향을 설명하는 데만 사용하며, intervention의 효과 크기나 통계적 유의성을 나타내지 않는다.

| Metric | Analyzable subset | Pre mean | Post mean | Direction summary | Interpretation |
|---|---:|---:|---:|---|---|
| Daily screen time | 18 participants | 97.7 min | 71.2 min | 11/18 decreased | Descriptive pattern only |
| Daily steps | 18 participants | 9,454 steps | 9,855 steps | 11/18 increased | Small aggregate increase; heterogeneous responses |

이 기술통계는 평균 방향을 보여주지만, 아동이 왜 그런 방향으로 움직였는지는 설명하지 않는다. 따라서 다음 소절들은 수치의 원인을 확정하기보다, bar interface가 어떤 방식으로 사용 상태를 보이게 만들었는지에 대한 theme 수준의 해석을 제시한다.

### 5.2 Bar Visibility와 Self-Monitoring

researcher memo-based theme에서 bar visibility는 핵심적인 디자인 요소로 나타난다. bar는 사용한 시간과 앞으로의 가능성을 한 화면에 보여주기 때문에, 아동이 별도의 계산 없이 자신의 상태를 파악할 수 있게 한다. 이 가시성은 self-monitoring의 출발점으로 해석될 수 있다.

bar가 중요한 이유는 숫자를 단순히 표시하기 때문만은 아니다. screen time과 physical activity의 관계를 하나의 형태로 보여주기 때문이다. 아동은 얼마나 썼는가와 앞으로 어떻게 조절할 수 있는가를 동시에 볼 수 있다. 이러한 구조는 사용 조절을 부모의 외부 명령이 아니라 아동이 이해할 수 있는 상태 정보로 바꾸는 데 기여할 가능성이 있다.

그러나 이 해석은 가능성 수준에 머문다. 현재 자료는 아동이 실제로 bar를 어떻게 해석했는지에 대한 formal coding 결과를 제공하지 않는다. 따라서 bar visibility가 self-monitoring을 향상시켰다고 말하기보다, self-monitoring을 지원하는 디자인 조건으로 해석될 수 있다고 표현해야 한다.

### 5.3 Planning과 Feedforward

feedforward는 앞으로의 선택을 예상하게 하는 기능이다. 본 시스템에서 feedforward는 아동이 앞으로 얼마나 움직여야 하는지, 사용을 줄이면 어떤 상태가 되는지, 현재 사용을 계속하면 제한에 가까워지는지를 이해하도록 도울 수 있다. 이 기능은 planning과 연결된다.

planning은 목표를 세우고 행동 순서를 조정하는 과정이다. 아동이 bar를 통해 사용 가능성과 활동 요구를 볼 수 있다면, 지금 더 쓰기, 나중에 쓰기, 먼저 움직이기, 오늘은 줄이기 같은 선택을 비교할 수 있다. 이러한 비교 가능성은 자기조절의 중요한 조건이다.

다만 planning은 단순히 정보를 제공한다고 자동으로 발생하지 않는다. 아동의 나이, 이해 수준, 부모의 설명 방식, 시스템 규칙의 명확성, 활동에 대한 선호가 모두 영향을 줄 수 있다. 따라서 후속 연구에서는 bar를 본 뒤 아동이 실제로 어떤 계획 언어를 사용하는지, 부모와 어떤 협상이 발생하는지, 사용 조절이 어떤 방식으로 설명되는지를 더 직접적으로 관찰할 필요가 있다.

### 5.4 Parent-Led Control에서 Child-Led Management로의 이동 가능성

정성 theme은 일부 상황에서 부모 주도 제한에서 아동 자기관리로 이동할 가능성을 보여준다. 이 문장은 매우 조심스럽게 읽어야 한다. 이는 부모-자녀 관계가 개선되었다거나 갈등이 감소했다는 주장이 아니다. 현재 자료는 그런 claim을 입증하지 않는다. 더 정확한 표현은 연구자 메모 수준에서 직접 통제와 잔소리 중심의 관리가 bar를 매개로 한 자기점검으로 옮겨갈 가능성이 관찰되었다는 것이다.

이 가능성은 디자인 관점에서 중요하다. 부모가 매번 그만하라고 말하는 대신, bar가 현재 상태를 보여주면 아동은 자신의 사용을 더 직접적으로 볼 수 있다. 이때 부모의 역할은 감시자에서 해석을 돕는 조력자로 이동할 수 있다. 그러나 이 이동은 자동으로 발생하지 않는다. 가족 규칙이 지나치게 강하거나, 아동이 시스템을 통제 도구로만 받아들이거나, penalty가 갈등을 강화한다면 반대 결과도 가능하다.

그러나 부모 주도 제한에서 아동 자기관리로의 이동 가능성은 bar가 항상 자율적으로 경험된다는 뜻이 아니다. 같은 구조 안에서도 incentive와 penalty는 동기화와 부담을 동시에 만들 수 있다.

### 5.5 Incentive와 Penalty의 양면성

incentive는 더 움직이면 더 사용할 수 있다는 구조를 만든다. 이 구조는 단기적으로 행동을 조정하는 데 도움이 될 수 있다. 그러나 동시에 운동의 의미를 바꿀 수 있다. 아동이 physical activity를 건강이나 즐거움이 아니라 screen time을 얻기 위한 비용으로 이해할 수 있기 때문이다.

penalty는 과도한 사용을 멈추는 신호로 작동할 수 있다. 제한이 명확하면 아동은 규칙을 예측할 수 있고, 부모도 즉흥적인 개입을 줄일 수 있다. 그러나 penalty는 좌절감이나 회피 전략을 만들 수도 있다. 아동이 제한을 부당하게 느끼거나, 활동 기록을 조작하려 하거나, 부모와 새로운 협상 갈등을 만들 가능성도 고려해야 한다.

이 양면성은 본 시스템을 단순한 behavior change tool이 아니라 self-regulation scaffold로 평가해야 하는 이유다. scaffold는 사용자를 대신해 행동을 강제하는 장치가 아니라, 사용자가 자신의 행동을 이해하고 조절할 수 있도록 임시로 지지하는 구조다. 그러나 scaffold가 지나치게 강하면 자율성을 줄일 수 있고, 지나치게 약하면 행동 변화를 돕지 못할 수 있다.

## 6. 논의

### 6.1 핵심 해석

본 초안의 논의는 평균값의 방향보다 그 평균값을 안전하게 해석할 수 있는 디자인 조건에 초점을 둔다. 분석 가능한 18명의 기술통계는 기대 방향의 관찰 패턴을 보여주지만, 이 패턴을 설명하려면 bar visibility, planning, family context, incentive와 penalty의 양면성을 함께 읽어야 한다.

정량 자료는 평균 screen time 감소 경향과 평균 steps 소폭 증가 경향을 보여주지만, 개인차가 크고 통계 검정이 없다. 정성 theme은 bar visibility와 planning/self-monitoring 가능성을 보여주지만, formal coding 결과가 아니다. 따라서 두 자료를 통합해도 결론은 보수적이어야 한다. 가장 안전한 결론은 bar-based interface가 screen time과 physical activity를 연결한 자기조절 scaffold로 해석될 수 있으며, 후속 검증이 필요하다는 것이다.

이 해석에서 중요한 것은 숫자와 theme의 관계다. 정량 자료가 theme을 입증하는 것도 아니고, theme이 정량 결과의 원인을 확정하는 것도 아니다. 두 자료는 서로를 보완해 후속 질문을 좁힌다. 평균값은 어떤 방향의 관찰 패턴이 있었는지 보여주고, theme은 그 패턴을 이해하기 위해 어떤 디자인 mechanism과 가족 맥락을 더 조사해야 하는지 제안한다.

### 6.2 디자인 기여

본 개입의 디자인 기여는 세 가지로 정리할 수 있다. 첫째, screen time과 physical activity를 분리하지 않고 하나의 상태로 보여준다. 둘째, feedback과 feedforward를 결합해 과거 사용과 다음 행동 가능성을 함께 제시한다. 셋째, incentive와 penalty를 단순 보상/처벌이 아니라 자기조절 scaffold의 일부로 재해석하게 한다.

이 기여는 효과 입증이 아니다. design contribution은 intervention이 우월하거나 일반적으로 효과적이라는 뜻이 아니라, 현재 자료와 시스템 설명을 바탕으로 어떤 design mechanism을 탐색할 수 있는지를 정리한다는 뜻이다. 이 초안의 문헌적 기여는 screen time 감소나 physical activity 증가 효과를 확정하는 데 있지 않다. 기여는 두 행동을 별도 outcome이 아니라 하나의 조절 가능한 상태 체계로 보고, bar visibility가 feedback, feedforward, incentive, penalty를 어떻게 하나의 자기조절 scaffold로 묶을 수 있는지 설명하는 데 있다.

아동 대상 디자인에서 이 점은 중요하다. 아동은 성인처럼 숫자 기반 dashboard를 지속적으로 해석하지 않을 수 있다. 따라서 복잡한 수치를 직관적 상태로 바꾸는 시각화가 필요하다. bar interface는 이 요구에 대응하는 간단한 형태를 제공한다. 하지만 간단한 형태가 항상 쉬운 경험을 보장하지는 않는다. bar의 의미가 명확해야 하고, 규칙이 이해 가능해야 하며, 부모와 아동이 그 규칙을 어떻게 사용할지 합의해야 한다.

### 6.3 개인화와 경계조건

본 자료에서 가장 중요한 caution 중 하나는 참여자별 반응이 균일하지 않다는 점이다. 평균값만 보면 screen time은 낮아지고 steps는 소폭 높아진 것으로 보일 수 있다. 그러나 방향성 요약은 18명 중 11명에서만 기대 방향 변화가 관찰되었음을 보여준다. 이는 모든 아동에게 같은 전략이 작동하지 않을 수 있음을 시사한다.

후속 시스템 설계에서는 baseline activity, 기존 screen time, 가족 규칙, 운동 선호, 학교 일정, 주말/평일 패턴을 반영한 개인화가 필요할 수 있다. 예를 들어 이미 활동량이 높은 아동에게 더 많은 steps를 요구하는 것은 부담이 될 수 있다. 반대로 활동량이 낮은 아동에게 지나치게 높은 목표를 주면 좌절을 만들 수 있다. 사용 조절 목표 역시 일괄 제한보다 상황별 목표가 더 적절할 수 있다.

incentive와 penalty의 경계조건도 개인화와 연결된다. 같은 incentive가 어떤 아동에게는 동기화 신호가 될 수 있지만, 다른 아동에게는 운동의 도구화로 경험될 수 있다. 같은 penalty가 어떤 가정에서는 규칙의 예측 가능성을 높일 수 있지만, 다른 가정에서는 갈등이나 회피 전략을 만들 수 있다. 따라서 후속 연구는 평균 변화만이 아니라 반응 유형, 가족 규칙, 아동의 해석, baseline activity를 함께 보아야 한다.

### 6.4 Compact Multi-Thread Workflow의 작성상 의의

이 초안은 Codex compact multi-thread workflow의 수업 시연물이기도 하다. 그러나 workflow는 empirical finding이 아니다. Codex thread들이 문헌, 데이터, 검증, draft, visual planning을 나누어 수행했다는 사실은 작성 과정의 투명성과 검증 가능성을 높이는 데 의미가 있다. 하지만 이것이 연구 결과의 타당성을 자동으로 높여주지는 않는다.

이번 compact run에서는 supervisor를 현재 대화로 유지하고, worker thread를 정확히 5개로 제한했다. Evidence-Literature는 gap과 이론 연결을 강화했고, Data-Methods는 분석 가능 범위와 inference limitation을 정리했다. Drafting은 섹션 간 연결과 반복 조정 방안을 제안했고, Review-Verification은 source/privacy/overclaim gate를 다시 점검했다. Visual-Assets는 표와 그림의 source, caption, safety label, safe prompt를 구체화했다.

이 방식은 기존 verbose run의 문제를 보완한다. 기존 실행에서는 role-demo thread, execution thread, phase-level thread, fallback thread가 겹치며 thread 목록이 길어졌다. compact run은 같은 목표를 더 적은 thread로 수행했다. 중요한 것은 thread 수가 아니라 판단 기능의 분리다. 새 프로젝트에서는 supervisor 하나와 Evidence-Literature, Data-Methods, Drafting, Review-Verification, Visual-Assets의 5개 worker로 시작하는 것이 더 재현 가능하다.

### 6.5 Visual Safety

그림과 표는 단순한 장식이 아니다. 어떤 그림을 넣느냐에 따라 독자가 연구를 효과 검증으로 읽을 수도 있고, 탐색적 해석으로 읽을 수도 있다. 예를 들어 participant-level trajectory chart는 개인 패턴을 노출할 수 있고, p-value나 causal arrow가 들어간 그림은 현재 근거 수준을 넘어선 claim처럼 보일 수 있다.

Visual safety는 claim strength control의 일부다. individual trajectory, significance marker, causal arrow가 들어간 chart는 현재 evidence가 허용하는 것보다 강한 주장을 시각적으로 만들 수 있다. 따라서 본 초안의 figure plan은 concept diagram, aggregate descriptive chart, interpretive mechanism map으로 제한한다.

Visual-Assets worker의 제안에 따라 모든 visual에는 제한 라벨을 붙인다. Table 3과 Figure 2에는 aggregate only, descriptive only, no inferential test를 붙인다. Figure 1은 illustrative only, no private screenshot으로 둔다. Figure 3는 interpretive only, not a causal pathway로 표시한다.

## 7. 한계

첫째, 본 초안의 정량 분석은 intervention date가 확인되는 분석 가능한 18명의 pre/post 기술통계로 제한된다. 전체 19명 중 1명은 intervention date 확인 문제로 pre/post 비교에서 제외되었다. 이 제한은 결과 해석의 범위를 좁힌다.

둘째, 통계 검정과 대조군 비교를 수행하지 않았다. 따라서 평균 screen time 감소와 steps 소폭 증가는 관찰된 descriptive pattern일 뿐이다. 효과가 입증되었다고 볼 수 없고, 다른 요인에 의한 변화 가능성도 배제할 수 없다.

셋째, post period는 intervention date 당일 및 이후로 정의했다. intervention date 당일은 개입 전과 후의 상태가 섞일 수 있으므로, causal inference를 더욱 어렵게 한다. 후속 분석에서는 intervention date 당일을 별도 처리하거나 sensitivity analysis를 수행할 필요가 있다.

넷째, 관찰 기간이 참여자별로 다르다. baseline period와 post period의 길이가 다르면 단순 평균 비교가 특정 기간의 영향, 계절성, 학교 일정, 주말/평일 구성 차이에 영향을 받을 수 있다.

다섯째, missing data와 zero-step handling이 해석을 제한한다. Missing screen-time 555행, missing steps 67행, zero-step 211행은 일별 기록의 완전성과 wearable/device recording validity에 대한 제한을 남긴다. `steps == 0` 행을 제외했지만, 이 처리가 실제 무활동과 기기 미착용 또는 수집 실패를 완전히 구분하지는 못한다.

여섯째, 정성 자료는 formal coding 결과가 아니다. researcher memo-based theme은 논의의 출발점으로는 유용하지만, 질적 연구 결과로 확정하려면 coding scheme, coder agreement, quote anonymization, theme saturation 검토가 필요하다.

일곱째, 본 문서는 AI-assisted draft이다. AI가 작성한 문장은 항상 source verification과 human signoff를 거쳐야 한다. 특히 외부 문헌의 정확한 인용, 원문 문장, 저자명, 연도, 이론적 주장 범위는 별도 확인이 필요하다.

이러한 한계는 본 초안의 가치를 없애는 것이 아니라, 이 초안이 어디까지를 말할 수 있고 어디서 human signoff와 후속 분석이 필요한지를 분명히 한다. 본 초안은 submission-ready empirical paper가 아니라, 후속 분석과 정성 검토를 위한 source-gated classroom draft다.

## 8. 결론

본 초안은 screen time과 physical activity를 연결한 bar-based visual interface가 아동의 자기조절 지원 방식으로 해석될 수 있는 가능성과 경계조건을 탐색했다. 분석 가능한 18명의 pre/post 기술통계에서는 평균 screen time이 낮아지는 관찰 경향과 평균 steps가 소폭 높아지는 관찰 경향이 나타났다. 그러나 이 결과는 통계적 효과, 인과효과, 대조군 비교, 일반화의 근거가 아니다.

정성 theme은 bar visibility가 planning, self-monitoring, parent-led control에서 child-led management로의 이동 가능성과 연결될 수 있음을 시사한다. 그러나 이 해석은 researcher memo-based theme 수준이며, 관계 개선, 갈등 감소, PBC 향상 측정으로 확장할 수 없다. incentive와 penalty는 단기 조절 가능성과 자율성 긴장을 동시에 만든다.

따라서 본 개입은 확정된 해결책이 아니라 후속 연구가 필요한 exploratory design intervention으로 정리하는 것이 적절하다. 이 원고의 기여는 개입의 우월성을 주장하는 데 있지 않고, screen time과 physical activity를 연결해 보는 디자인 질문을 source-gated 방식으로 정리했다는 데 있다. 후속 연구는 더 명확한 분석 설계, missing data 처리, 개인차 분석, formal qualitative coding, privacy-safe visual reporting, 장기 추적을 포함해야 한다.

연구실 시연 관점에서는, Codex compact multi-thread workflow가 자료 기반 초안 작성의 속도를 높이는 동시에 claim gate와 privacy gate를 운영하는 방법을 보여준다는 점이 핵심이다. 한 연구자가 모든 일을 한 채팅에 몰아넣는 대신, Evidence-Literature, Data-Methods, Drafting, Review-Verification, Visual-Assets worker에게 분담시키고, supervisor가 반환물을 병합하면 더 검토 가능한 초안 패키지를 만들 수 있다.

## Appendix A. Classroom-Safe Table and Figure Plan

The following table and figure plan is designed for classroom use. Tables document workflow, evidence binding, and aggregate descriptive summaries. Figures are limited to concept diagrams, aggregate charts, and interpretive maps. No visual should include private screenshots, raw quotes, participant names, participant-level trajectories, or visual cues that imply causal proof.

### Table 1. Compact Multi-Thread Workflow Roles

제한 라벨: workflow documentation only

| Role | Responsibility | Output | Gate function |
|---|---|---|---|
| Supervisor | 전체 지휘, 반환 취합, 최종 병합 | merge report, final draft | phase gate, human signoff |
| Evidence-Literature | 연구 gap, 문헌 위치, 이론 렌즈 | literature return | source context |
| Data-Methods | 데이터 readiness, 분석 가능 범위, 방법 한계 | data-methods return | data scope gate |
| Drafting | 구조, transition, long-form draft 지시 | drafting return | writing coherence gate |
| Review-Verification | source, privacy, overclaim 검토 | review return | source/privacy gate |
| Visual-Assets | 표/그림, caption, safe prompt | visual return | visual safety gate |

Caption: Table 1. Compact multi-thread workflow roles for the classroom demonstration. The table documents how the supervisor and five worker threads divide literature, data-methods, drafting, review-verification, and visual-assets responsibilities. This table is workflow documentation only and is not empirical evidence about the intervention.

### Table 2. Claim Gate and Evidence Binding Matrix

제한 라벨: source-gate documentation only

| Claim type | Classroom-safe wording | Status | Visual implication |
|---|---|---|---|
| System description | Bar interface links screen time and physical activity | Allowed | Can appear in Figure 1 |
| Screen time | 18명 기술통계에서 평균 screen time 감소 경향이 관찰됨 | Allowed with caveat | Aggregate only |
| Steps | 평균 steps는 소폭 증가했으나 개인차가 큼 | Allowed with caveat | Aggregate only |
| PBC | PBC는 measured outcome이 아니라 interpretive lens | Allowed | Interpretive label only |
| Parent-child relation | 관계 개선 또는 갈등 감소 | Blocked/Human-only | Do not visualize |
| Effectiveness | 통계적 효과, 인과효과, 일반화 | Blocked | Do not visualize |

Caption: Table 2. Claim gate and evidence binding matrix for the source-gated classroom draft. The table links major claims to approved sources and marks which claims require caveats, human verification, or exclusion. It is source-gate documentation only, not a new analysis result.

### Table 3. Aggregate Descriptive Pre/Post Summary

제한 라벨: aggregate only; descriptive only

| Metric | Analyzable subset | Pre mean | Post mean | Descriptive change | Direction summary | Interpretation |
|---|---:|---:|---:|---:|---|---|
| Daily screen time | 18 participants | 97.7 min | 71.2 min | -27.1% | 11/18 decreased | Descriptive pattern only |
| Daily steps | 18 participants | 9,454 steps | 9,855 steps | +4.2% | 11/18 increased | Small aggregate increase; heterogeneous responses |

Caption: Table 3. Aggregate descriptive pre/post summary for the analyzable subset. Values are classroom-safe aggregate means for 18 participants with intervention dates. The table is aggregate only and descriptive only; it does not report statistical significance, causal effects, or participant-level trajectories.

### Figure 1. Intervention Concept Diagram

제한 라벨: illustrative only; no private screenshot

구성: 중앙에 bar-based visual interface를 두고, 왼쪽에 screen time use와 physical activity, 위쪽에 feedback과 feedforward, 아래쪽에 incentive와 penalty, 오른쪽에 planning/self-monitoring cues를 배치한다. 하단에는 "Conceptual diagram; no participant data"를 둔다.

Safe prompt:

```text
Create a clean academic concept diagram for a classroom research paper. Show a bar-based visual interface that links screen time use and physical activity. Include labeled components for feedback, feedforward, incentive, and penalty, and a final label for planning/self-monitoring cues. Use abstract icons only, no real app screenshot, no phone brand, no child faces, no participant data, no names, and no private information. Add small text labels: "illustrative only" and "conceptual diagram".
```

Caption: Figure 1. Conceptual diagram of the bar-based interface linking screen time and physical activity. The figure illustrates how feedback, feedforward, incentive, and penalty strategies are combined in the intervention design. It is illustrative only and does not use private screenshots, real app screens, or participant-level data.

### Figure 2. Aggregate Pre/Post Descriptive Trend

제한 라벨: aggregate only; descriptive only; no inferential test

구성: Panel A는 daily screen time aggregate mean: pre 97.7 minutes, post 71.2 minutes. Panel B는 daily steps aggregate mean: pre 9,454 steps, post 9,855 steps. Subtitle은 "18 analyzable participants; aggregate means only". Footnote는 "No p-values, no effect sizes, no control group comparison".

Safe chart prompt:

```text
Create a two-panel aggregate chart for a classroom research draft. Panel A shows daily screen time aggregate mean: Pre 97.7 minutes, Post 71.2 minutes. Panel B shows daily steps aggregate mean: Pre 9,454 steps, Post 9,855 steps. Use grouped bars, not participant-level lines. Add labels: "18 analyzable participants", "aggregate only", "descriptive only", and "no inferential test". Do not include p-values, significance stars, effect-size labels, individual points, participant IDs, or causal wording.
```

Caption: Figure 2. Aggregate descriptive pre/post patterns in screen time and step count. The figure uses classroom-safe aggregate means for 18 analyzable participants. It is aggregate only and descriptive only, with no inferential tests, control-group comparison, or participant-level trajectories.

### Figure 3. Interpretive Mechanism Map

제한 라벨: interpretive only; not a causal pathway

구성: bar visibility -> perceived behavioral control lens -> planning/self-monitoring -> possible screen-time management 또는 activity compensation. Boundary condition으로 baseline activity, motivation, family context, rule clarity를 둔다. PBC는 measured outcome이 아니라 lens라고 표시한다.

Safe prompt:

```text
Create a restrained academic interpretive mechanism map for a classroom research paper. Show "Bar visibility" connected to "Perceived behavioral control lens", then to "Planning" and "Self-monitoring", then to two possible responses: "Screen-time management" and "Activity compensation". Add boundary-condition labels: "baseline activity", "motivation", "family context", and "rule clarity". Use cautious connector labels such as "may support" and "possible response". Add labels: "interpretive only" and "not a causal pathway". Do not show causal proof, statistical effect, children’s faces, participant data, raw quotes, or real screenshots.
```

Caption: Figure 3. Interpretive mechanism map for the exploratory classroom draft. The map summarizes how bar visibility may support perceived behavioral control as an interpretive lens, planning, and self-monitoring, while allowing different possible responses across children and families. It is interpretive only and not a causal pathway.

## Appendix B. Human Signoff Checklist

- [ ] 참고문헌 원문 대조를 완료했는가?
- [ ] 모든 정량 claim이 18명 pre/post 기술통계로 제한되어 있는가?
- [ ] 통계적 유의성, 인과효과, 대조군 비교, 일반화 표현이 제거되었는가?
- [ ] intervention date 당일 post 처리 기준을 승인했는가?
- [ ] missing screen-time, missing steps, zero-step handling을 재검토했는가?
- [ ] 정성 theme을 formal coding 결과처럼 쓰지 않았는가?
- [ ] raw quote를 사용하지 않았거나, 사용할 경우 익명화와 동의 검토를 완료했는가?
- [ ] PBC를 측정 outcome처럼 표현하지 않았는가?
- [ ] 표와 그림이 집계형 또는 개념형으로 제한되어 있는가?
- [ ] generated image가 실제 연구 결과처럼 보이지 않도록 caption을 붙였는가?
- [ ] 최종 원고에 human author가 책임지는 판단 로그를 남겼는가?
