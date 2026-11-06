def solution(n):
    # n의 3진법 자릿수를 낮은 자리부터 꺼내 결과에 3을 곱하며 이어 붙이면, 뒤집은 3진수가 문자열 변환 없이 바로 10진수로 만들어진다
    # 시간 복잡도: O(log n)
    answer = 0
    while n:
        n, digit = divmod(n, 3)
        answer = answer * 3 + digit
    return answer
