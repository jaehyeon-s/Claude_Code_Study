# Claude Code Study (Python)

클로드 코드를 일주일간 학습하기 위한 실습 저장소입니다.
작은 할 일 관리 CLI(`todo.py`)를 매일 조금씩 발전시키며 Claude Code의 기능을 익힙니다.

> 진행 방식: 매 세션 `개념(짧게) → Claude가 도구 실제 실행 시연 → 직접 시켜보기`
> 모든 결과물은 이 repo에 커밋하여 복습 가능하게 보존.

## 실행 방법
```bash
python3 todo.py add "내용"   # 할 일 추가
python3 todo.py list         # 목록 보기
python3 todo.py done <번호>  # 완료 처리
```

## 📅 일주일 마스터 플랜

| Day | 주제 | 실습 예제 (Python) | 상태 |
|-----|------|--------------------|------|
| **1** | 기본기 & 멘탈모델 | 작은 CLI 앱 뼈대 만들기 + `/init`으로 CLAUDE.md 생성 | ✅ 완료 |
| **2** | 파일 탐색 & 코드 작성 | 기능 구현 → 버그 심기 → 찾아서 수정 (Read/Grep/Edit) | ✅ 완료 |
| **3** | Git & GitHub | 브랜치→커밋→PR 생성→리뷰 (GitHub MCP) | ⬜ |
| **4** | Plan Mode & 대규모 작업 | 멀티 파일 리팩터링: 계획→승인→실행 | ⬜ |
| **5** | 스킬 & 슬래시 커맨드 | `/code-review`, `/security-review`, `/simplify` | ⬜ |
| **6** | 설정 & 자동화 | `settings.json`, Hooks(저장 시 자동 테스트), MCP, `/loop`로 주기적 자율 실행 맛보기 | ⬜ |
| **7** | 종합 실전 | 작은 앱 풀사이클: 기획→구현→리뷰→테스트→PR | ⬜ |

## 핵심 멘탈모델
- Claude Code는 챗봇이 아니라 **도구를 쓰는 에이전트**: 파일 읽기(Read), 검색(Glob/Grep),
  편집(Edit/Write), 실행(Bash), 위임(서브에이전트), 스킬(슬래시 커맨드) 등을 직접 수행.
- **Claude Code on the Web** 환경: 클라우드의 임시 컨테이너 → 결과물은 반드시 commit & push 해야 보존.
- 작업 브랜치: `claude/charming-mayer-1QmW7`

## 진도 로그
- **Day 1** (2026-06-01): 로드맵 저장, 멘탈모델, 첫 CLI 앱(`todo.py`) 실습.
  GitHub App 권한 트러블슈팅(403 → 앱 설치/쓰기 권한 부여)으로 push 성공.
- **Day 2** (2026-06-02): 파일 탐색 & 코드 작성. `delete` 명령 추가(Read→Edit),
  Grep으로 `done`/`delete`의 번호 범위 버그 발견 → 예외 처리로 수정, Bash로 검증.
  기능 추가와 버그 수정을 커밋 분리.

## 메모 (나중에 실습할 주제)
- **24시간 자율 실행**: headless 모드(`claude -p`) + 권한 자동승인(`--dangerously-skip-permissions`)
  + 할 일 큐 + 격리 컨테이너 조합. 이벤트 기반(GitHub Actions)이나 `/loop` 스킬로도 가능.
  → Day 6에서 `/loop`로 안전하게 맛보기 예정.
