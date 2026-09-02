def solution(storage, usage, change):
    # 매달 사용량을 전달보다 change[i]%만큼 늘리거나 줄이고(소수점 버림) 누적해 가다가, 누적 사용량이 저장량을 넘는 달의 번호(이번 달이 0)를 돌려준다. 끝까지 안 넘으면 -1
    total = 0
    for month, rate in enumerate(change):
        usage += usage * rate // 100
        total += usage
        if total > storage:
            return month
    return -1
