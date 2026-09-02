MOD = 1_000_000_007


def _count_cases(a, offset, length):
    dp = [0] * (length + 1)
    dp[0] = 1

    max_level = [0] * length

    prefix_to_boundary = {0: 0}
    prefix_sum = 0

    for i in range(length):
        value = a[offset + i]
        prefix_sum += value
        prefix_to_boundary[prefix_sum] = i + 1

        cell_sum = value
        cell_start = i
        merge_count = 0

        ways = dp[i]

        while cell_start > 0:
            left_end = cell_start - 1
            left_base = a[offset + left_end]
            ratio, remainder = divmod(cell_sum, left_base)

            if remainder or (ratio & (ratio - 1)):
                break

            required_level = ratio.bit_length() - 1
            if required_level > max_level[left_end]:
                break

            merge_count += 1
            cell_sum *= 2
            cell_start = prefix_to_boundary[prefix_sum - cell_sum]
            ways += dp[cell_start]

        max_level[i] = merge_count
        dp[i + 1] = ways % MOD

    return dp[length]


def solution(a, s):
    answer = []
    offset = 0

    for length in s:
        answer.append(_count_cases(a, offset, length))
        offset += length

    return answer
