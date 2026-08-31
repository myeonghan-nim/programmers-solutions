def solution(sequence):
    # 짝수 위치에 +, 홀수 위치에 -를 곱한 수열과 그 반대 부호 수열을 생각하면, 펄스를 곱해 만들 수 있는 모든 수열은 이 두 수열의 연속 부분 수열과 같다. 각각에 대해 "새로 시작 vs 앞 구간에 이어붙이기" 중 큰 쪽을 고르며(카데인 알고리즘) 최대 구간 합을 구한다.
    # 시간 복잡도: O(n)
    answer = plus_current = minus_current = 0

    for index, number in enumerate(sequence):
        sign = 1 if index % 2 == 0 else -1
        plus_value = number * sign
        minus_value = -plus_value

        # 각 위치에서 끝나는 최대 구간 합: 여기서 새로 시작하거나 앞 구간에 이어붙이거나
        plus_current = max(plus_value, plus_current + plus_value)
        minus_current = max(minus_value, minus_current + minus_value)
        answer = max(answer, plus_current, minus_current)

    return answer
