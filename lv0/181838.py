def solution(date1, date2):
    # 리스트끼리 비교하면 앞 원소부터 차례로 비교하므로 [연, 월, 일] 꼴 그대로 어느 날짜가 앞서는지 판단할 수 있다
    return int(date1 < date2)
