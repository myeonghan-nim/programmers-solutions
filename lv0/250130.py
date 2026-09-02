# 첫 달 저축액에서 시작해 70만 원이 되기 전에는 before, 그 후에는 after씩 더하며 100만 원 이상이 될 때까지 걸린 개월 수를 센다
money = int(input())
before = int(input())
after = int(input())
month = 1
while money < 100:
    month += 1
    money += before if money < 70 else after
print(month)
