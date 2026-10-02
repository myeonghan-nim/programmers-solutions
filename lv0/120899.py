def solution(array):
    # max로 가장 큰 수를 찾고, index로 그 수가 몇 번째 칸(0부터 셈)에 있는지 찾아 [값, 인덱스] 꼴로 돌려준다
    biggest = max(array)
    return [biggest, array.index(biggest)]
