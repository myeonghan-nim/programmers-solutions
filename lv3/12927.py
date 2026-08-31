def solution(n, works):
    # 제곱의 합을 줄이려면 항상 가장 큰 작업량부터 1씩 깎는 것이 유리하다. 하나씩 깎는 대신 내림차순 정렬 후 "가장 큰 값들을 다음 값 높이까지 한꺼번에 깎는" 단계로 묶어 계산한다.
    # 시간 복잡도: O(m log m) (m = len(works))
    if sum(works) <= n:
        return 0  # 시간 안에 일을 전부 끝낼 수 있으면 피로도 0

    works.sort(reverse=True)
    works.append(0)  # 마지막 단계(0까지 깎기)를 위한 경계값
    for i in range(len(works) - 1):
        cur = works[i]
        nxt = works[i + 1]
        cnt = i + 1  # 현재 최고 높이 cur에 있는 작업 개수
        need = (cur - nxt) * cnt  # cnt개를 모두 nxt 높이까지 깎는 데 드는 시간

        if n >= need:
            n -= need
            continue

        # 시간이 모자라면 남은 n을 cnt개에 최대한 고르게 나눠 깎는다
        q, r = divmod(n, cnt)
        base = cur - q

        answer = r * (base - 1) ** 2  # r개는 한 번 더 깎여 base-1
        answer += (cnt - r) * base ** 2
        answer += sum(w * w for w in works[i + 1:-1])  # 아직 깎지 않은 나머지 작업들
        return answer

    return 0
