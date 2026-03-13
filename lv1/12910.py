def solution(arr, divisor):
    answer = []
    for n in arr:
        if not n % divisor:
            answer.append(n)
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer
