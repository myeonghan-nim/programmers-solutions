def solution(t, p):
    # p와 길이가 같은 부분 문자열을 모두 잘라 정수로 바꾼 뒤 p 이하인 개수를 센다
    # 시간 복잡도: O(T × P) (T: t의 길이, P: p의 길이)
    return sum(int(t[i : i + len(p)]) <= int(p) for i in range(len(t) - len(p) + 1))
