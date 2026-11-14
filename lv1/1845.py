def solution(nums):
    # 고를 수 있는 마릿수는 N/2로 고정이고 종류는 중복 없이 세어야 하므로, 답은 서로 다른 종류의 수와 N/2 중 작은 값이다
    # 시간 복잡도: O(n), n은 nums의 길이
    return min(len(set(nums)), len(nums) // 2)
