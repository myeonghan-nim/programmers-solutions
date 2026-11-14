from datetime import date


def solution(a, b):
    # 표준 라이브러리 date가 윤년(2016년 2월은 29일)까지 계산해 주므로 요일 번호만 이름으로 바꾼다
    # 시간 복잡도: O(1)
    day_names = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]  # weekday()는 월요일이 0
    return day_names[date(2016, a, b).weekday()]
