def solution(num_list):
    # 앞에서부터 차례로 살펴보다 처음 만나는 음수의 인덱스를 돌려주고, 끝까지 없으면 -1을 돌려준다
    for i, num in enumerate(num_list):
        if num < 0:
            return i
    return -1
