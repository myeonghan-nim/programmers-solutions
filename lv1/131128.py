def solution(X, Y):
    # 숫자별 등장 횟수를 세어 공통 개수(min)만큼 짝지은 뒤 9부터 0까지 내림차순으로 이어 붙이면 가장 큰 수가 된다
    # 시간 복잡도: O(|X| + |Y|)
    digits = "".join(d * min(X.count(d), Y.count(d)) for d in "9876543210")
    if not digits:
        return "-1"
    return "0" if digits[0] == "0" else digits  # 0만 남으면 "000..."이 아닌 "0"으로 반환
