def solution(common):
    # 앞 세 수의 간격이 같으면 등차수열이라 마지막 수에 공차를 더하고, 아니면 등비수열이라 마지막 수에 공비(두 번째 수 ÷ 첫 수)를 곱한다
    if common[1] - common[0] == common[2] - common[1]:
        return common[-1] + common[1] - common[0]
    return common[-1] * (common[1] // common[0])
