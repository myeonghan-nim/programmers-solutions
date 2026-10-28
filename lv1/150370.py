def solution(today, terms, privacies):
    # 모든 달이 28일이므로 날짜를 총 일 수 하나로 바꾸고, 수집일 + 유효기간(달 × 28)이 오늘 이하이면 파기 대상이다
    # 시간 복잡도: O(T + P) (T: terms의 길이, P: privacies의 길이)
    def to_days(date):
        y, m, d = map(int, date.split("."))
        return y * 12 * 28 + m * 28 + d

    months = {kind: int(month) for kind, month in (term.split() for term in terms)}
    now = to_days(today)
    return [i for i, privacy in enumerate(privacies, 1) if to_days(privacy[:10]) + months[privacy[11:]] * 28 <= now]
