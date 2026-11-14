def solution(seoul):
    # "Kim"은 반드시 한 번 나타나므로 index()가 예외 없이 그 위치를 돌려준다
    # 시간 복잡도: O(n), n은 seoul의 길이
    return f"김서방은 {seoul.index('Kim')}에 있다"
