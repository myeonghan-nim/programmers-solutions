# programmers-solutions

프로그래머스 풀이를 모아 둔 학습용 저장소다.
초보자도 읽으므로 이름과 주석의 품질이 중요하다.
새 풀이를 더하거나 기존 풀이를 다듬을 때 아래 규칙을 기본으로 적용한다.

## 답변 언어

All user-facing text in Korean (reports, progress, questions, Bash descriptions). Re-check after context compaction, where English drift recurs. Code, paths, commands, identifiers stay as-is.

## 풀이 문체

1. 주석은 한국어로 쓴다. 함수 첫머리에 핵심 아이디어를 적고, 다음 줄에 `# 시간 복잡도: O(...)`를 따로 적고, 비자명한 줄에만 인라인 주석을 단다.
2. 주석 한 줄은 180자까지로 보고, 180자 안이면 여러 줄로 쪼개지 않는다. 시간 복잡도를 따로 적는 줄이나 단계 나열처럼 읽기 쉽게 하려는 개행은 둔다. 짧게 끊긴 주석이 오히려 읽기 불편하다는 지적에서 나온 규칙이다.
3. 코드 스멜(오타, 내장 이름 가림, 죽은 분기, 루프 변수가 남는 것을 이용한 트릭 등)은 고친다.
4. 파이썬답지 않은 이름(`Atab`, 대문자 매개변수 `A, B`)은 snake_case로 고친다. 프로그래머스는 위치 인자로 채점하므로 매개변수 이름은 바꿔도 되지만, 개수와 순서는 유지하고 쓰지 않는 매개변수도 서명에 남긴다.

## 커밋

커밋은 의미 단위(fix, perf, refactor, docs)로 나눈다.
메시지 형식은 아래와 같다.

One line `<type>: <message>` + `Co-Authored-By` trailer only. No body, no other footers; breaking change = `<type>!:`. Conventional Commits types; message in English, lowercase, imperative, readable without session context (no `R1`, `Phase 2`).

## 남은 문제를 세는 기준

모든 레벨(0부터 5까지)을 포함하되, Python(python3)으로 제출할 수 있는 문제만 센다.
SQL 전용 문제(mysql, oracle)와 파이썬을 지원하지 않는 알고리즘 문제(1829부터 1842까지, 12974 등 C++와 Java 전용)는 뺀다.
문제가 지원하는 언어는 문제 페이지 SSR(서버가 내려 주는 HTML)의 `?language=` 드롭다운 링크로 판별할 수 있다.

## 코딩 원칙

아래 원칙이 위의 풀이 문체와 부딪히면 풀이 규칙을 따른다.
예를 들어 3번은 멀쩡한 코드를 고치지 말라고 하지만, 풀이를 다듬는 작업에서는 코드 스멜과 이름을 고친다.

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.
