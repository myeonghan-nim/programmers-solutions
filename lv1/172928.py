def solution(park, routes):
    # 시작점 S에서 출발해 명령마다 한 칸씩 미리 가 보고, 공원을 벗어나거나 장애물을 만나면 그 명령은 통째로 무시한다
    # 시간 복잡도: O(H × W + R × D) (R: routes의 길이, D: 최대 이동 거리)
    height, width = len(park), len(park[0])
    h, w = next((i, row.index("S")) for i, row in enumerate(park) if "S" in row)
    moves = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
    for route in routes:
        direction, distance = route.split()
        dh, dw = moves[direction]
        nh, nw = h, w
        for _ in range(int(distance)):
            nh, nw = nh + dh, nw + dw
            if not (0 <= nh < height and 0 <= nw < width) or park[nh][nw] == "X":
                break
        else:  # 중간에 막히지 않고 끝까지 갔을 때만 이동을 확정한다
            h, w = nh, nw
    return [h, w]
