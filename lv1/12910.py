def solution(arr, divisor):
    # divisor로 나누어 떨어지는 수만 골라 담고 오름차순으로 정렬한다
    answer = []
    for n in arr:
        if not n % divisor:  # 나머지가 0이면 나누어 떨어지는 수
            answer.append(n)
    if not answer:
        answer.append(-1)  # 하나도 없으면 [-1]을 반환
    answer.sort()
    return answer
