def solution(words):
    # 트라이(글자를 한 글자씩 따라가며 갈라지는 트리)에 모든 단어를 넣으면서 각 마디를 지나는 단어 수를 센다. 지나는 단어가 1개뿐인 마디에 닿는 순간 자동완성이 되므로, 각 단어는 그 지점까지의 글자 수만 입력하면 된다.
    # 시간 복잡도: O(L) (L은 모든 단어 길이의 합)
    root = {}
    for w in words:
        node = root
        for ch in w:
            entry = node.setdefault(ch, [0, {}])
            entry[0] += 1  # 이 글자까지 같은 접두사를 가진 단어 수
            node = entry[1]

    total = 0
    for w in words:
        node = root
        for i, ch in enumerate(w, 1):
            cnt, child = node[ch]
            if cnt == 1:  # 여기까지 입력하면 이 단어 하나로 확정된다
                total += i
                break
            node = child
        else:
            total += len(w)  # 끝까지 다른 단어와 접두사가 겹치면 전부 입력
    return total
