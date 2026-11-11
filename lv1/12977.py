from itertools import combinations


def solution(nums):
    # 서로 다른 3개를 고르는 모든 조합의 합을 구해, 2부터 제곱근까지 나누어떨어지는 수가 없으면 소수로 센다 (합은 최소 1 + 2 + 3 = 6이라 2 미만인 경우는 없다)
    # 시간 복잡도: O(n^3 * sqrt(S)), n은 nums의 길이, S는 세 수의 합의 최댓값
    return sum(all(total % divisor for divisor in range(2, int(total**0.5) + 1)) for total in map(sum, combinations(nums, 3)))
