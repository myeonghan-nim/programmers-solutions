def solution(phone_number):
    # 뒤 4자리를 뺀 길이만큼 "*"을 만들고 그 뒤에 원래 뒤 4자리를 붙인다
    # 시간 복잡도: O(len(phone_number))
    return "*" * (len(phone_number) - 4) + phone_number[-4:]
