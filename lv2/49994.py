def solution(dirs):
    # 지나간 "길"을 (출발점, 도착점) 묶음으로 집합에 저장해 처음 걸은 길만 세어지게 한다. 같은 길은 반대 방향으로 지나도 한 길이므로 양방향 두 개를 함께 넣고 마지막에 2로 나눈다. 좌표 범위(-5~5)를 벗어나는 명령은 무시한다.
    # 시간 복잡도: O(n)
    route = set()
    x = y = nx = ny = 0
    for d in dirs:
        if d == "U":
            ny = y + 1
        elif d == "D":
            ny = y - 1
        elif d == "L":
            nx = x - 1
        else:
            nx = x + 1
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            route.add((x, y, nx, ny))
            route.add((nx, ny, x, y))
        else:
            nx, ny = x, y
        x, y = nx, ny
    return len(route) // 2
