def solution(s):
    # 아스키 코드에서 대문자(65~90)가 소문자(97~122)보다 작으므로, 문자 그대로 내림차순 정렬하면 "대문자는 소문자보다 작다"는 조건이 저절로 맞는다
    # 시간 복잡도: O(n log n), n은 s의 길이
    return "".join(sorted(s, reverse=True))
