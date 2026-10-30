def solution(food):
    # 음식마다 절반 개수만큼 번호를 이어 왼쪽 절반을 만들고 물과 뒤집은 절반을 붙인다
    # 시간 복잡도: O(S) (S: 결과 문자열의 길이)
    left = "".join(str(i) * (n // 2) for i, n in enumerate(food) if i)
    return left + "0" + left[::-1]
