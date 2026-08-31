def solution(x, n):
    # i번째 칸에 x의 (i+1)배를 넣으면 x부터 x씩 커지는 수 n개가 된다
    answer = [0] * n
    for i in range(n):
        answer[i] = x * (i + 1)
    return answer
