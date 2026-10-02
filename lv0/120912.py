def solution(array):
    # 모든 수를 문자열로 바꿔 하나로 이어 붙인 뒤 count로 "7"이 몇 번 나오는지 센다
    return "".join(map(str, array)).count("7")
