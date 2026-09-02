def solution(mode_type, humidity, val_set):
    # auto 모드는 습도가 10 오를 때마다 5단계에서 한 단계씩 내려가고(50 이상이면 0), target과 minimum 모드는 습도가 설정값보다 낮은지에 따라 정해진 단계를 준다
    if mode_type == "auto":
        return max(0, 5 - humidity // 10)
    if mode_type == "target":
        return 3 if humidity < val_set else 1
    return 1 if humidity < val_set else 0
