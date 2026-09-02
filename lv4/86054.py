MOD = 1_000_000_007


def _count_cases(a, offset, length):
    # 합쳐진 안티 세포는 항상 "같은 합끼리 2배씩 커지는" 병합 사슬이라, dp[i] = 앞 i개 원소를 세포들로 나누는 경우의 수로 두고
    # i에서 끝나는 세포를 왼쪽으로 한 단계씩 병합해 보며 가능한 시작 지점의 dp를 모두 더한다.
    # 시간 복잡도: O(n log S) — 병합할 때마다 세포 합이 2배가 되어 한 위치당 반복이 log(전체 합)로 제한된다
    dp = [0] * (length + 1)
    dp[0] = 1

    # max_level[i]: i에서 끝나는 세포가 도달할 수 있는 최대 병합 단계(합이 원소값의 2^단계)
    max_level = [0] * length

    # 누적합 -> 그 지점까지의 원소 개수. 병합 후 세포의 시작 위치를 O(1)에 찾기 위한 표
    prefix_to_boundary = {0: 0}
    prefix_sum = 0

    for i in range(length):
        value = a[offset + i]
        prefix_sum += value
        prefix_to_boundary[prefix_sum] = i + 1

        cell_sum = value
        cell_start = i
        merge_count = 0

        ways = dp[i]  # 병합하지 않고 i 혼자 세포가 되는 경우

        while cell_start > 0:
            left_end = cell_start - 1
            left_base = a[offset + left_end]
            ratio, remainder = divmod(cell_sum, left_base)

            # 왼쪽 세포와 합이 같으려면 (현재 합 / 왼쪽 원소값)이 2의 거듭제곱이어야 한다 (비트 트릭으로 판정)
            if remainder or (ratio & (ratio - 1)):
                break

            # 왼쪽 세포가 실제로 그 단계까지 커질 수 있어야 병합 가능
            required_level = ratio.bit_length() - 1
            if required_level > max_level[left_end]:
                break

            merge_count += 1
            cell_sum *= 2  # 같은 합 두 세포를 합치면 합이 2배
            cell_start = prefix_to_boundary[prefix_sum - cell_sum]
            ways += dp[cell_start]

        max_level[i] = merge_count
        dp[i + 1] = ways % MOD

    return dp[length]


def solution(a, s):
    # s가 정한 길이대로 a를 앞에서부터 잘라, 구간(배열 b)마다 독립적으로 경우의 수를 구한다
    answer = []
    offset = 0

    for length in s:
        answer.append(_count_cases(a, offset, length))
        offset += length

    return answer
