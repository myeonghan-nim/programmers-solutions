# 별 n개로 된 한 줄을 만들어 m번 출력한다 (이 문제는 solution 함수 없이 표준 입력을 읽고 표준 출력으로 답한다)
# 시간 복잡도: O(n * m)
n, m = map(int, input().split())
for _ in range(m):
    print("*" * n)
