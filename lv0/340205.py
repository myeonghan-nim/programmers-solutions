# 수를 문자열로 읽어 앞에서부터 2글자씩 잘라 정수로 바꾼 뒤 모두 더한다
number = input()
print(sum(int(number[i:i + 2]) for i in range(0, len(number), 2)))
