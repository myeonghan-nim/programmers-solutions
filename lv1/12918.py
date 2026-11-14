def solution(s):
    # 길이 조건과 숫자 조건을 각각 확인한다. isdigit()은 부호나 공백이 섞이면 False라서 "-123"이나 "1e22" 같은 입력도 걸러진다
    # 시간 복잡도: O(n), n은 s의 길이
    return len(s) in (4, 6) and s.isdigit()
