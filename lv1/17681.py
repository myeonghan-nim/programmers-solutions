def solution(n, arr1, arr2):
    # 두 지도 중 하나라도 벽이면 벽이므로 같은 줄끼리 비트 OR 한 뒤, n자리 이진 문자열로 바꿔 1은 "#", 0은 " "로 치환한다
    # 시간 복잡도: O(n^2)
    return [format(a | b, f"0{n}b").translate(str.maketrans("10", "# ")) for a, b in zip(arr1, arr2)]
