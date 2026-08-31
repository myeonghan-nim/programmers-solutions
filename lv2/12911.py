def solution(n):
    # n을 2진수로 바꿨을 때의 1의 개수를 미리 세어 두고, n보다 큰 수를 1씩 늘려 가며 1의 개수가 같은 첫 번째 수를 찾는다. n이 100만 이하로 작아서 하나씩 확인해도 충분히 빠르다.
    count = bin(n)[2:].count("1")
    num = n + 1
    while True:
        if bin(num)[2:].count("1") == count:
            return num
        num += 1
