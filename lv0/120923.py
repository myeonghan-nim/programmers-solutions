def solution(num, total):
    # 첫 수를 x라 하면 합은 x*num + (0+1+...+(num-1))이므로, total에서 그 등차 합을 빼고 num으로 나누면 첫 수가 나온다
    start = (total - num * (num - 1) // 2) // num
    return [start + i for i in range(num)]
