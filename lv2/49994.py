def solution(dirs):
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
