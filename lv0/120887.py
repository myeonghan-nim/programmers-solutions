def solution(i, j, k):
    # i부터 j까지 각 수를 문자열로 바꿔 k라는 숫자 글자가 몇 번 나오는지 세어 모두 더한다
    return sum(str(num).count(str(k)) for num in range(i, j + 1))
