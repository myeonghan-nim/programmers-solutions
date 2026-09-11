def solution(n, slicer, num_list):
    # n 값에 따라 슬라이스의 시작·끝·간격만 달라지므로 경우별로 알맞게 잘라 돌려준다
    a, b, c = slicer
    if n == 1:
        return num_list[:b + 1]
    if n == 2:
        return num_list[a:]
    if n == 3:
        return num_list[a:b + 1]
    return num_list[a:b + 1:c]
