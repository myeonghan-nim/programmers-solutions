def solution(my_string, indices):
    # 지울 인덱스들을 집합에 담아 두고, 집합에 없는 인덱스의 글자만 순서대로 이어 붙인다
    removed = set(indices)
    return "".join(ch for i, ch in enumerate(my_string) if i not in removed)
