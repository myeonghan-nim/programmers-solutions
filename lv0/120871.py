def solution(n):
    # 1부터 하나씩 세면서 3의 배수이거나 3이 들어간 수는 건너뛰고, n번째로 세어진 수를 돌려준다
    village = 0
    for _ in range(n):
        village += 1
        while village % 3 == 0 or "3" in str(village):
            village += 1
    return village
