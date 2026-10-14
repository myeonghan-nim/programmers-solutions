# 표준입력으로 n을 받아 i번째 줄에 별을 i개씩 찍으면 높이와 너비가 n인 직각 이등변 삼각형이 된다
n = int(input())
for i in range(1, n + 1):
    print("*" * i)
