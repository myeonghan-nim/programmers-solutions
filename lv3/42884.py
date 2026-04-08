def solution(routes):
    routes.sort(key=lambda x: x[1])
    cnt = 0
    camera = -30001
    for route in routes:
        if camera < route[0]:
            cnt += 1
            camera = route[1]
    return cnt
