def solution(n):
    # 맨 끝 자릿수(n % 10)부터 차례로 담으면 저절로 뒤집힌 순서가 된다
    answer = []
    while n > 0:
        digit = n % 10
        answer.append(digit)
        n //= 10
    return answer
