def solution(n):
    # 1부터 n까지 나눠 보며 나누어떨어지는 수만 모으면 그대로 오름차순 약수 목록이 된다
    return [i for i in range(1, n + 1) if n % i == 0]
