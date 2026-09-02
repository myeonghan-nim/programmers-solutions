# 한국식 나이는 2030 - 출생 연도 + 1, 연 나이는 2030 - 출생 연도다
year = int(input())
age_type = input()
print(2030 - year + 1 if age_type == "Korea" else 2030 - year)
