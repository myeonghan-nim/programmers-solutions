def solution(num_list):
    # 마지막 원소가 그전 원소보다 크면 두 값의 차를, 아니면 마지막 원소의 두 배를 뒤에 붙인다
    a, b = num_list[-2], num_list[-1]
    return num_list + [b - a if b > a else 2 * b]
