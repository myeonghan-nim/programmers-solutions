def solution(n, a, b):
    # 한 라운드가 끝나면 번호 x는 (x + 1) // 2 가 된다. (1,2번 → 1번, 3,4번 → 2번, ...) 두 번호가 같아지는 순간이 서로 만나는 라운드이므로 그때까지의 횟수를 센다.
    # 시간 복잡도: O(log n)
    answer = 0
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1
    return answer
