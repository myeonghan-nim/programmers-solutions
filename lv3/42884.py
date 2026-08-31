def solution(routes):
    # 진출 지점이 빠른 차량부터 보며, 아직 카메라를 못 만난 차가 나오면 그 차의 진출 지점에 카메라를 세운다(최대한 늦게 세워야 뒤차들도 같이 걸림).
    # 시간 복잡도: O(n log n)
    routes.sort(key=lambda x: x[1])
    cnt = 0
    camera = -30001  # 아직 카메라 없음(가능한 최소 지점보다 작은 값)
    for route in routes:
        if camera < route[0]:  # 마지막 카메라가 이 차의 구간 밖이면 새로 설치
            cnt += 1
            camera = route[1]
    return cnt
