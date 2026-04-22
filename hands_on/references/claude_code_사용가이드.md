# Claude Code 완전 사용 가이드

> 터미널 기반 AI 에이전트, Claude Code의 설치부터 실전 활용까지

**최종 업데이트**: 2026년 4월  
**대상 독자**: 연구자, 개발자, AI 도구 활용에 관심 있는 실무자

---

## 1. Claude Code란 무엇인가

Claude Code는 Anthropic이 만든 **터미널 기반 AI 에이전트**다. 일반 채팅 인터페이스(Claude Chat)와 달리, 실제 작업 디렉토리에서 파일을 읽고, 수정하고, 명령어를 실행하며, Git 작업까지 수행한다.

핵심 차이를 한 문장으로 정리하면: **Claude Chat은 대화 도구이고, Claude Code는 실행 도구다.**

### 1.1 Claude Code의 4가지 렌즈 (Claude Code Lens)

Claude Code를 이해하는 프레임워크:

1. **기억된 맥락 (Memoized Context)**: CLAUDE.md 파일을 통해 프로젝트 배경, 규칙, 선호를 자동으로 읽는다. 매번 복붙할 필요 없이 "이 프로젝트가 뭔지" 알고 시작한다.
2. **도구 오케스트레이션 (Tool Orchestration)**: Bash, 파일 읽기/쓰기, Git, MCP 도구 등을 스스로 조합해서 복잡한 작업을 수행한다.
3. **권한 게이트 (Permission Gate)**: 파일 수정, 명령 실행 등을 할 때 사용자 승인을 요청한다. 자동 실행이 아니라 "확인하고 실행"하는 구조.
4. **이어가기 가능한 세션 (Resumable Session)**: 작업 중단 후에도 세션을 이어갈 수 있다. `/resume`으로 이전 대화를 복원한다.

### 1.2 제품군 내 위치

| 접근 경로 | 특징 | 적합한 사용자 |
|---|---|---|
| **Claude Chat** | 대화, 아이디어 정리, 빠른 분석 | 누구나 |
| **Projects** | 같은 배경 자료를 계속 쓰고 가는 팀 | 팀 협업 |
| **Cowork** | 파일 중심 작업 자동화 (문서, 리서치) | 비개발자 |
| **Claude Code** | 코드 편집, 테스트, 빌드, Git 연동 | 개발자 / 연구자 |

---

## 2. 설치 및 시작

### 2.1 설치

```bash
# npm으로 설치 (Node.js 18+ 필요)
npm install -g @anthropic-ai/claude-code

# 설치 확인
claude --version
```

### 2.2 인증

```bash
# Anthropic 계정으로 로그인
claude auth login

# API 키 사용 시 (Console 과금)
claude auth login --console

# SSO 인증 강제
claude auth login --sso

# 인증 상태 확인
claude auth status
```

### 2.3 첫 실행

```bash
# 프로젝트 폴더로 이동
cd ~/my_project

# Claude Code 시작 (CLAUDE.md가 있으면 자동 로드)
claude

# 질문과 함께 시작
claude "이 프로젝트 구조 설명해줘"
```

---

## 3. 핵심 개념 5가지

YouTube 영상 "Get Started With Claude Code: 5 Essential Features"의 핵심 내용을 기반으로, 실전에서 가장 중요한 5가지 개념을 정리한다.

### 3.1 컨텍스트 윈도우 (Context Window)

Claude Code는 **컨텍스트 윈도우**라는 한정된 작업 공간에서 동작한다. 대화가 길어지면 앞부분을 잊기 시작한다.

**왜 중요한가**: 파일을 많이 읽거나 긴 대화를 하면 컨텍스트가 차서 앞의 지시를 잊는다. 이것이 "AI가 갑자기 엉뚱한 소리를 하는" 대부분의 원인이다.

**실전 팁**:
- `/context` 명령으로 현재 컨텍스트 사용량을 시각적으로 확인
- `/cost` 명령으로 토큰 사용 통계 확인
- 컨텍스트가 70% 이상 차면 `/compact`로 요약 후 계속

### 3.2 Plan 모드 (계획 모드)

큰 작업을 시작하기 전에 먼저 계획을 세우게 하는 모드. Claude가 바로 코드를 쓰는 대신, 무엇을 할지 먼저 정리한다.

**활성화 방법**:
- `Shift+Tab`을 눌러 모드 전환 (default → plan → auto 순환)
- `/plan` 명령으로 바로 진입
- `--permission-mode plan` 플래그로 시작 시 설정
- `/plan fix the auth bug`처럼 설명과 함께 진입 가능

**언제 쓰는가**:
- 복잡한 리팩토링 전
- 여러 파일을 동시에 수정해야 할 때
- 작업 방향이 맞는지 먼저 확인하고 싶을 때
- "뭘 할지 모르겠는데 일단 시키면 안 될 것 같을 때"

**Plan 모드에서는**: Claude가 파일을 읽고 분석하되, 실제 수정은 하지 않는다. 계획을 보여주고 승인하면 그때 실행한다.

### 3.3 @ 참조 (파일 타겟팅)

`@` 기호로 특정 파일이나 URL을 직접 지정해서 Claude에게 전달한다.

**사용법**:
```
# 파일 참조
@src/main.py 이 파일의 에러 핸들링 개선해줘

# 여러 파일 참조
@src/auth.py @src/middleware.py 이 두 파일의 인증 로직 비교해줘

# URL 참조
@https://docs.example.com/api API 문서 기반으로 클라이언트 만들어줘
```

**왜 쓰는가**: Claude가 전체 프로젝트를 스캔하는 대신 정확히 필요한 파일만 보게 해서 컨텍스트를 절약하고 정확도를 높인다.

### 3.4 컨텍스트 압축 (/compact)

대화가 길어졌을 때 이전 내용을 요약해서 컨텍스트 공간을 확보한다.

```
# 기본 압축
/compact

# 특정 내용에 집중해서 압축
/compact 인증 관련 내용 위주로 유지해줘
```

**자동 압축**: 컨텍스트가 가득 차면 Claude Code가 자동으로 압축한다 (auto-compaction). 수동으로 `/compact`를 실행하면 초점을 지정할 수 있다는 장점이 있다.

**압축 시 주의**: 압축하면 세부 내용이 사라질 수 있다. 중요한 지시사항은 CLAUDE.md에 적어두면 압축과 관계없이 유지된다.

### 3.5 체크포인트와 되돌리기 (/rewind)

Claude가 코드를 수정한 후 결과가 마음에 안 들면, 이전 상태로 되돌릴 수 있다.

```
# 되돌리기 인터페이스 열기
/rewind

# 별칭
/checkpoint
```

**작동 방식**: Claude Code는 매 턴마다 git checkpoint를 만든다. `/rewind`를 실행하면 대화와 코드 변경 모두 이전 시점으로 돌아간다.

**실전 활용**: "이 방향으로 해봐" → 결과 확인 → 마음에 안 들면 `/rewind` → 다른 방향으로 재시도. 이 사이클이 Claude Code의 핵심 워크플로우.

---

## 4. 전체 명령어 레퍼런스

### 4.1 CLI 실행 명령어 (터미널에서)

| 명령어 | 설명 | 예시 |
|---|---|---|
| `claude` | 대화형 세션 시작 | `claude` |
| `claude "질문"` | 초기 프롬프트와 함께 시작 | `claude "이 프로젝트 설명해줘"` |
| `claude -p "질문"` | 한 번 질문하고 종료 (SDK 모드) | `claude -p "이 함수 설명해줘"` |
| `cat 파일 \| claude -p "질문"` | 파이프로 내용 전달 | `cat logs.txt \| claude -p "에러 분석해줘"` |
| `claude -c` | 마지막 대화 이어가기 | `claude -c` |
| `claude -r "세션" "질문"` | 특정 세션 재개 | `claude -r "auth-refactor" "PR 마무리해줘"` |
| `claude update` | 최신 버전 업데이트 | `claude update` |
| `claude auth login` | 로그인 | `claude auth login` |
| `claude auth status` | 인증 상태 확인 | `claude auth status` |
| `claude agents` | 설정된 서브에이전트 목록 | `claude agents` |
| `claude mcp` | MCP 서버 관리 | `claude mcp` |
| `claude plugin` | 플러그인 관리 | `claude plugin install code-review@claude-plugins-official` |

### 4.2 주요 CLI 플래그

| 플래그 | 설명 | 예시 |
|---|---|---|
| `--model` | 모델 지정 | `claude --model claude-sonnet-4-6` |
| `--permission-mode` | 권한 모드 설정 | `claude --permission-mode plan` |
| `--add-dir` | 추가 작업 디렉토리 | `claude --add-dir ../apps ../lib` |
| `--worktree`, `-w` | Git worktree에서 격리 실행 | `claude -w feature-auth` |
| `--print`, `-p` | 비대화형 출력 모드 | `claude -p "질문"` |
| `--continue`, `-c` | 마지막 대화 이어가기 | `claude -c` |
| `--resume`, `-r` | 특정 세션 재개 | `claude -r auth-refactor` |
| `--name`, `-n` | 세션 이름 지정 | `claude -n "my-feature"` |
| `--effort` | 모델 노력 수준 | `claude --effort high` |
| `--max-turns` | 최대 턴 수 제한 (SDK 모드) | `claude -p --max-turns 3 "질문"` |
| `--max-budget-usd` | 최대 비용 제한 (SDK 모드) | `claude -p --max-budget-usd 5.00 "질문"` |
| `--output-format` | 출력 형식 (text/json/stream-json) | `claude -p --output-format json "질문"` |
| `--system-prompt` | 시스템 프롬프트 전체 교체 | `claude --system-prompt "You are a Python expert"` |
| `--append-system-prompt` | 시스템 프롬프트에 추가 | `claude --append-system-prompt "TypeScript만 써줘"` |
| `--bare` | 최소 모드 (빠른 시작) | `claude --bare -p "질문"` |
| `--allowedTools` | 자동 허용할 도구 | `claude --allowedTools "Bash(git *)" "Read"` |
| `--disallowedTools` | 차단할 도구 | `claude --disallowedTools "Bash(rm *)"` |
| `--mcp-config` | MCP 서버 설정 파일 로드 | `claude --mcp-config ./mcp.json` |
| `--chrome` | Chrome 브라우저 연동 활성화 | `claude --chrome` |
| `--remote` | 웹 세션으로 작업 생성 | `claude --remote "로그인 버그 수정"` |
| `--remote-control` | Remote Control 활성화 | `claude --remote-control "My Project"` |
| `--debug` | 디버그 모드 | `claude --debug "api,mcp"` |
| `--verbose` | 상세 로그 출력 | `claude --verbose` |
| `--version`, `-v` | 버전 확인 | `claude -v` |
| `--dangerously-skip-permissions` | 모든 권한 확인 건너뛰기 (위험) | CI/CD 자동화 전용 |
| `--json-schema` | JSON 스키마 기반 구조화 출력 | `claude -p --json-schema '{...}' "질문"` |
| `--fallback-model` | 과부하 시 대체 모델 | `claude -p --fallback-model sonnet "질문"` |
| `--agent` | 커스텀 에이전트 지정 | `claude --agent my-custom-agent` |
| `--plugin-dir` | 플러그인 디렉토리 로드 | `claude --plugin-dir ./my-plugins` |
| `--tools` | 사용 가능 도구 제한 | `claude --tools "Bash,Edit,Read"` |
| `--tmux` | tmux 세션으로 실행 | `claude -w feature --tmux` |
| `--teleport` | 웹 세션을 로컬로 가져오기 | `claude --teleport` |

### 4.3 세션 내 슬래시 명령어 (전체 목록)

세션 안에서 `/`를 입력하면 사용 가능한 명령어 목록이 나타난다.

#### 세션 관리

| 명령어 | 설명 |
|---|---|
| `/clear` | 대화 기록 초기화 (별칭: `/reset`, `/new`) |
| `/compact [지시]` | 대화 요약으로 컨텍스트 확보 |
| `/resume [세션]` | 이전 세션 재개 (별칭: `/continue`) |
| `/rename [이름]` | 세션 이름 변경 |
| `/branch [이름]` | 대화 분기점 생성 (별칭: `/fork`) |
| `/export [파일명]` | 대화를 텍스트로 내보내기 |
| `/exit` | 종료 (별칭: `/quit`) |

#### 모드 및 모델 전환

| 명령어 | 설명 |
|---|---|
| `/plan [설명]` | Plan 모드 진입. 설명과 함께 바로 시작 가능 |
| `/model [모델]` | 모델 변경. 좌우 화살표로 effort 조절 |
| `/effort [low\|medium\|high\|max\|auto]` | 모델 노력 수준 설정 |
| `/fast [on\|off]` | Fast 모드 토글 |

#### 코드 및 변경 관리

| 명령어 | 설명 |
|---|---|
| `/rewind` | 이전 시점으로 되돌리기 (별칭: `/checkpoint`) |
| `/diff` | 변경사항 인터랙티브 뷰어 |
| `/security-review` | 현재 브랜치 변경사항 보안 분석 |

#### 프로젝트 설정

| 명령어 | 설명 |
|---|---|
| `/init` | CLAUDE.md 생성으로 프로젝트 초기화 |
| `/memory` | CLAUDE.md 메모리 파일 편집 |
| `/config` | 설정 인터페이스 (별칭: `/settings`) |
| `/permissions` | 도구 권한 관리 (별칭: `/allowed-tools`) |
| `/hooks` | Hook 설정 보기 |
| `/add-dir <경로>` | 작업 디렉토리 추가 |

#### 정보 확인

| 명령어 | 설명 |
|---|---|
| `/help` | 도움말 및 명령어 목록 |
| `/context` | 컨텍스트 사용량 시각화 |
| `/cost` | 토큰 사용 통계 |
| `/usage` | 플랜 사용량 및 제한 |
| `/status` | 버전, 모델, 계정, 연결 상태 |
| `/stats` | 일별 사용량, 세션 기록, 모델 선호도 |
| `/doctor` | 설치 및 설정 진단 |
| `/release-notes` | 변경 로그 보기 |
| `/copy [N]` | 마지막 응답을 클립보드에 복사 |

#### 번들 스킬 (Bundled Skills)

| 명령어 | 설명 |
|---|---|
| `/batch <지시>` | 대규모 코드베이스 병렬 변경. worktree별 에이전트가 독립 작업 후 PR 생성 |
| `/debug [설명]` | 디버그 로깅 활성화 및 문제 분석 |
| `/loop [간격] [프롬프트]` | 프롬프트를 반복 실행 (별칭: `/proactive`) |
| `/simplify [초점]` | 최근 변경 파일의 코드 품질·재사용·효율성 리뷰 후 수정 |
| `/claude-api` | Claude API 레퍼런스 로드 (Python, TypeScript 등) |

#### 연동 및 도구

| 명령어 | 설명 |
|---|---|
| `/mcp` | MCP 서버 연결 관리 |
| `/plugin` | 플러그인 관리 |
| `/skills` | 사용 가능한 스킬 목록 |
| `/agents` | 에이전트 설정 관리 |
| `/chrome` | Chrome 연동 설정 |
| `/ide` | IDE 연동 관리 |
| `/schedule [설명]` | 예약 작업 (Routine) 생성 및 관리 |
| `/tasks` | 백그라운드 작업 목록 (별칭: `/bashes`) |

#### 기타

| 명령어 | 설명 |
|---|---|
| `/desktop` | Claude Code Desktop 앱으로 전환 (별칭: `/app`) |
| `/remote-control` | Remote Control 활성화 (별칭: `/rc`) |
| `/teleport` | 웹 세션을 터미널로 가져오기 (별칭: `/tp`) |
| `/autofix-pr [프롬프트]` | CI 실패/리뷰 코멘트 자동 수정 세션 생성 |
| `/ultraplan <프롬프트>` | 브라우저에서 계획 리뷰 후 실행 |
| `/btw <질문>` | 대화에 추가하지 않는 간단한 사이드 질문 |
| `/voice` | 음성 입력 토글 |
| `/feedback [보고]` | 피드백 제출 (별칭: `/bug`) |
| `/theme` | 색상 테마 변경 |
| `/color [색상]` | 프롬프트 바 색상 변경 |
| `/insights` | 사용 패턴 분석 리포트 |
| `/team-onboarding` | 팀 온보딩 가이드 자동 생성 |
| `/stickers` | Claude Code 스티커 주문 |
| `/powerup` | 기능 학습용 인터랙티브 데모 |

---

## 5. CLAUDE.md — 프로젝트 맥락 문서

### 5.1 왜 필요한가

매번 "이 프로젝트는 뭐고, 이 파일은 뭐고…"라고 설명하는 대신, CLAUDE.md 하나에 적어두면 Claude Code가 **세션 시작 시 자동으로 읽는다.** 30분 투자로 이후 30시간을 절약하는 구조.

### 5.2 파일 위치와 우선순위

| 위치 | 적용 범위 | 설명 |
|---|---|---|
| `~/.claude/CLAUDE.md` | 모든 프로젝트 | 개인 전역 설정 |
| `프로젝트루트/CLAUDE.md` | 해당 프로젝트 | 프로젝트별 맥락 |
| `프로젝트루트/.claude/CLAUDE.md` | 해당 프로젝트 | 위와 동일 (다른 경로) |

설정 우선순위: Managed (조직) > User (개인) > Project (프로젝트)

### 5.3 실전 템플릿

```markdown
# 프로젝트 맥락 문서 (CLAUDE.md)

## 프로젝트
- 주제: [프로젝트/연구 주제]
- 목표: [핵심 목표 한 줄]
- 현재 단계: [문헌검토 / 자료수집 / 분석 / 작성]

## 기술 스택
- 언어: [Python / TypeScript / etc.]
- 프레임워크: [React / FastAPI / etc.]
- 데이터베이스: [PostgreSQL / etc.]

## 출력 규칙
- 문체: [학술체 / 보고서체 / 구어체]
- 언어: [한국어 / 영어 / 혼용]
- 인용 형식: [APA 7th / Chicago / etc.]

## 금기
- 확인 안 된 논문은 만들지 말 것. 모르면 "확인 필요" 표기
- 원본 데이터(raw/) 폴더는 절대 수정하지 말 것
- [프로젝트별 추가 금기]

## 핵심 선행 연구
- [저자 (연도)] — 한 줄 요약
- [저자 (연도)] — 한 줄 요약
```

### 5.4 관련 .md 파일들

CLAUDE.md 외에도 프로젝트에 활용할 수 있는 파일들:

| 파일 | 역할 |
|---|---|
| `CLAUDE.md` | 프로젝트 맥락 (자동 로드) |
| `plan.md` | 현재 작업 계획 및 진행 상태 |
| `handoff.md` | 다음 세션/사람에게 전달할 메모 |
| `brand-voice.md` | 문체 및 톤 가이드 |
| `working-rules.md` | 운영 규칙 및 용어 기준 |
| `about-me.md` | 개인 선호 및 배경 (전역) |

---

## 6. 키보드 단축키

| 단축키 | 기능 |
|---|---|
| `Shift+Tab` | 권한 모드 전환 (default → plan → auto 순환) |
| `Escape` | 현재 응답 중단 |
| `Shift+Enter` | 여러 줄 입력 |
| `Tab` | 자동완성 (파일명, 명령어) |
| `/` | 슬래시 명령어 목록 |
| `@` | 파일/URL 참조 |

---

## 7. 권한 모드 (Permission Modes)

Claude Code는 위험한 작업을 실행하기 전에 사용자 확인을 요청한다. `Shift+Tab`으로 모드를 전환할 수 있다.

| 모드 | 설명 |
|---|---|
| `default` | 매 작업마다 확인 요청 (기본값) |
| `acceptEdits` | 파일 수정은 자동 허용, 명령 실행은 확인 |
| `plan` | 읽기만 허용, 수정/실행 차단 (계획 수립용) |
| `auto` | AI가 안전 여부를 자동 판단 (Team/Enterprise/API만) |
| `dontAsk` | 모든 권한 자동 허용 (주의 필요) |
| `bypassPermissions` | 모든 권한 검사 건너뛰기 (CI/CD 전용, 위험) |

---

## 8. 실전 워크플로우

### 8.1 새 프로젝트 시작

```bash
cd ~/my_project
claude

# 세션 안에서:
/init                         # CLAUDE.md 생성
```

### 8.2 기존 코드 분석

```bash
claude "이 프로젝트의 구조와 주요 모듈을 설명해줘"

# 또는 Plan 모드로:
claude --permission-mode plan
> 이 코드베이스를 분석하고 아키텍처 다이어그램을 만들어줘
```

### 8.3 버그 수정 사이클

```
# 1. Plan 모드에서 분석
/plan 로그인 시 세션이 유지되지 않는 버그 분석해줘

# 2. 계획 확인 후 실행 모드로 전환 (Shift+Tab)

# 3. 수정 확인
/diff

# 4. 마음에 안 들면
/rewind

# 5. 다른 방향으로 재시도
이번엔 세션 저장소를 Redis로 바꿔서 해결해봐
```

### 8.4 대량 파일 처리 (연구자용)

```bash
# Claude Code 시작
cd ~/research_project
claude

# 세션 안에서:
hands_on/sample_data/ 폴더에 PDF 10개가 있어.
각 PDF를 읽고, 아래 형식으로 output/summaries/ 폴더에
파일명_summary.md로 저장해줘.

형식:
## 메타
- 제목:
- 저자:
- 연도:
## 핵심 요약 (200자 이내)
## 방법론 한 줄
## 주요 발견 3개
```

### 8.5 세션 이어가기

```bash
# 마지막 세션 이어가기
claude -c

# 이름 붙인 세션 이어가기
claude -r "auth-refactor"

# 세션 목록 보기
claude -r   # 인터랙티브 피커 표시
```

### 8.6 Git Worktree로 병렬 작업

```bash
# 격리된 worktree에서 작업
claude -w feature-auth

# tmux와 함께 사용
claude -w feature-auth --tmux

# /batch로 대규모 병렬 처리
/batch src/ 전체를 React에서 Vue로 마이그레이션해줘
```

### 8.7 비대화형 스크립트 활용

```bash
# 한 번 질문하고 결과 받기
claude -p "package.json에서 사용하지 않는 의존성 찾아줘"

# JSON 형식으로 출력
claude -p --output-format json "이 함수의 복잡도 분석해줘"

# 파이프로 연결
git diff | claude -p "이 변경사항을 리뷰해줘"
cat error.log | claude -p "이 에러의 원인이 뭐야?"

# 비용 제한
claude -p --max-budget-usd 2.00 "전체 코드베이스 리팩토링 계획 세워줘"

# 턴 제한
claude -p --max-turns 5 "README.md 작성해줘"
```

---

## 9. Skills, Plugins, MCP

### 9.1 Skills (반복 작업 절차)

같은 작업을 두 번 반복해야 하면 Skill로 만든다.

```
~/.claude/skills/my-skill/SKILL.md    # 개인 스킬 (모든 프로젝트)
.claude/skills/my-skill/SKILL.md      # 프로젝트 스킬 (이 프로젝트만)
```

SKILL.md 예시:
```yaml
---
name: summarize-paper
description: 논문 PDF를 읽고 구조화된 요약을 생성한다
allowed-tools: Read Bash(python *)
---

논문 $ARGUMENTS을(를) 읽고 다음 형식으로 요약해줘:
1. 메타 정보 (제목, 저자, 연도, 학술지)
2. 핵심 요약 (200자 이내)
3. 방법론 한 줄
4. 주요 발견 3개
5. 인용할 만한 문장 (페이지 표시)
```

사용: `/summarize-paper paper.pdf`

### 9.2 Plugins (역할 패키지)

Skill, Hook, MCP 등을 묶은 패키지. 설치 한 줄이면 기능이 추가된다.

```bash
# 플러그인 설치
claude plugin install code-review@claude-plugins-official

# 설치된 플러그인 관리
/plugin
```

### 9.3 MCP (외부 도구 연결)

Model Context Protocol. 외부 서비스(Slack, Google Drive, Notion, GitHub 등)를 Claude에 연결한다.

```bash
# MCP 서버 설정
claude mcp add my-server -- node server.js

# 설정 파일로 로드
claude --mcp-config ./mcp.json
```

### 9.4 구분 한 줄 정리

- **Skill**은 하는 법 (반복 절차)
- **Plugin**은 묶어서 배포하는 상자 (Skill + Hook + MCP 등)
- **MCP**는 바깥 도구에 닿는 길 (외부 서비스 연결)

---

## 10. 서브에이전트 (Sub-agents)

복잡한 작업을 작은 단위로 나눠 전문 에이전트에게 위임한다.

```
.claude/agents/my-agent.md    # 커스텀 서브에이전트 정의
```

### 빌트인 에이전트 타입

| 에이전트 | 역할 |
|---|---|
| `general-purpose` | 범용 작업 (기본값) |
| `Explore` | 코드베이스 탐색 전용 (읽기 전용 도구) |
| `Plan` | 계획 수립 전용 |

### CLI에서 동적 에이전트 정의

```bash
claude --agents '{"reviewer":{"description":"코드 리뷰어","prompt":"코드 품질을 리뷰한다"}}'
```

---

## 11. Harness Engineering — 작업 환경 설계

"Claude Code를 어떻게 쓰느냐"가 아니라 **"Claude가 일하는 작업장을 어떻게 설계하느냐"**가 핵심.

### 11.1 개념

**Harness** = Claude가 일하는 실행 환경 전체. 다음을 포함한다:
- **맥락 문서** (CLAUDE.md, AGENTS.md) — 무엇을 알아야 하는가
- **도구** (Bash, Read/Write/Edit, MCP) — 무엇을 할 수 있는가
- **규칙** (permissions, hooks) — 무엇을 해도 되는가 / 안 되는가
- **구조** (폴더 구조, 템플릿, 파일명 규칙) — 결과물을 어디에 두는가

### 11.2 왜 "프롬프트 엔지니어링"이 아니라 "하네스 엔지니어링"인가

| 프롬프트 엔지니어링 | 하네스 엔지니어링 |
|---|---|
| 채팅창에서 질문을 잘 쓰기 | 작업 환경 전체를 설계하기 |
| 매번 다시 설명 | CLAUDE.md가 자동 로드 |
| 도구를 바꾸면 처음부터 | 같은 문서를 어디서든 재사용 |
| 결과가 채팅에만 존재 | 파일로 저장 → 재사용 가능 |

### 11.3 실전 폴더 구조 예시

```
my_research_project/
├── CLAUDE.md                    # 프로젝트 맥락 (자동 로드)
├── .claude/
│   ├── skills/
│   │   └── summarize-paper/
│   │       └── SKILL.md         # 논문 요약 스킬
│   └── agents/
│       └── reviewer.md          # 검증 에이전트
├── raw/                         # 원본 데이터 (수정 금지)
├── output/
│   ├── summaries/               # 추출 결과
│   ├── classification.md        # 분류표
│   └── analysis.md              # 분석 결과
└── templates/                   # 출력 템플릿
```

---

## 12. 실패 패턴과 해결법

### 12.1 "AI가 갑자기 엉뚱한 소리를 한다"

**원인**: 컨텍스트 윈도우가 가득 참.
**해결**: `/compact`로 요약하거나, 핵심 지시를 CLAUDE.md에 넣어두기.

### 12.2 "매번 같은 걸 설명해야 한다"

**원인**: 맥락 문서가 없다.
**해결**: CLAUDE.md 작성. 30분 투자 → 30시간 절약.

### 12.3 "에이전트가 임의로 분류/구조를 만든다"

**원인**: 기준을 사람이 먼저 정하지 않았다.
**해결**: 분류 축, 출력 형식을 내가 먼저 설계하고 에이전트에게 실행만 시킨다.

### 12.4 "출처가 맞는지 모르겠다"

**원인**: 검증 단계를 건너뛰었다 (검증부채).
**해결**: 에이전트 답변에서 인용된 문헌 최소 2건은 직접 확인. 다른 모델로 교차검증.

### 12.5 "수정한 게 마음에 안 든다"

**원인**: 되돌리기를 모른다.
**해결**: `/rewind`로 이전 시점으로 되돌린 후 다른 방향으로 재시도.

---

## 13. 연구자를 위한 빠른 시작 체크리스트

1. **Claude Code 설치**: `npm install -g @anthropic-ai/claude-code`
2. **프로젝트 폴더에서 시작**: `cd ~/my_research && claude`
3. **CLAUDE.md 작성**: `/init` 또는 직접 작성
4. **Plan 모드로 분석**: `Shift+Tab`으로 plan 모드 전환 후 프로젝트 구조 파악
5. **파일 처리 자동화**: PDF 읽기, 요약, 분류를 Skill로 만들어 반복 실행
6. **교차검증**: 같은 맥락 문서를 다른 AI 도구에도 넣어 결과 비교
7. **결과를 파일로 저장**: 채팅에만 남기지 말고, output/ 폴더에 .md로 저장
8. **세션 이어가기**: `claude -c`로 어제 하던 작업 계속

---

## 14. 환경 변수 (주요)

| 변수 | 설명 |
|---|---|
| `ANTHROPIC_API_KEY` | API 키 직접 설정 |
| `CLAUDE_CODE_USE_BEDROCK` | Amazon Bedrock 사용 |
| `CLAUDE_CODE_USE_VERTEX` | Google Vertex AI 사용 |
| `CLAUDE_CODE_SIMPLE` | `--bare` 모드와 동일 |
| `CLAUDE_CODE_NEW_INIT` | `/init`에서 인터랙티브 플로우 활성화 |
| `SLASH_COMMAND_TOOL_CHAR_BUDGET` | 스킬 설명 문자 예산 |

---

## 15. 참고 자료

- [Claude Code 공식 문서](https://code.claude.com/docs/en/cli-reference)
- [Claude Code 명령어 레퍼런스](https://code.claude.com/docs/en/commands)
- [스킬 가이드](https://code.claude.com/docs/en/slash-commands)
- [권한 모드 가이드](https://code.claude.com/docs/en/permission-modes)
- [MCP 문서](https://code.claude.com/docs/en/mcp)
- [Claude Code & Cowork Master Guide (CHOI, 2026)](클로드코드_가이드북_compressed.pdf) — 583페이지 종합 가이드
- [클로드 코드 잘 사용하기 (김영동, 2026)](클로드 코드 잘 사용하기.pdf) — 사내 세미나 자료
- [Get Started With Claude Code: 5 Essential Features](https://www.youtube.com/watch?v=dFWh2Al7WBo) — YouTube 영상

---

*이 문서는 2026년 4월 기준으로 작성되었습니다. Claude Code는 빠르게 업데이트되므로, `claude update`와 `/release-notes`로 최신 변경사항을 확인하세요.*
