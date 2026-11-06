import re


def solution(new_id):
    # 문제의 7단계를 순서대로 적용한다. 4단계 뒤에는 첫 글자가 마침표일 수 없어, 6단계에서 15자로 자르고 끝 마침표를 떼어도 최소 한 글자가 남는다
    # 시간 복잡도: O(n)
    new_id = re.sub(r"[^a-z0-9\-_.]", "", new_id.lower())  # 1~2단계: 소문자로 바꾸고 허용되지 않는 문자 제거
    new_id = re.sub(r"\.{2,}", ".", new_id).strip(".")  # 3~4단계: 연속 마침표를 하나로 줄이고 양끝 마침표 제거
    new_id = (new_id or "a")[:15].rstrip(".")  # 5~6단계: 빈 문자열이면 "a", 15자로 자른 뒤 끝 마침표 제거
    return new_id.ljust(3, new_id[-1])  # 7단계: 3자가 될 때까지 마지막 문자를 붙임
