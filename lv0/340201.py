def solution(seat, passengers):
    # 정거장마다 탄 사람(On) 수는 더하고 내린 사람(Off) 수는 빼서 버스에 남은 승객을 구한 뒤, 전체 좌석에서 빼면 빈 좌석 수가 된다(모자라면 0)
    riding = 0
    for station in passengers:
        riding += station.count("On") - station.count("Off")
    return max(0, seat - riding)
