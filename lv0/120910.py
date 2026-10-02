def solution(n, t):
    # 1시간마다 2배가 되므로 t시간 후에는 처음 마리수에 2를 t번 곱한 n * 2^t 마리가 된다
    return n * 2 ** t
