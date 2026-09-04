def solution(num_list):
    # 홀수 숫자들과 짝수 숫자들을 각각 문자열로 이어 붙여 수로 만든 뒤 두 수를 더한다
    odd = "".join(str(num) for num in num_list if num % 2 == 1)
    even = "".join(str(num) for num in num_list if num % 2 == 0)
    return int(odd) + int(even)
