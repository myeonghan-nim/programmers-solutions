def solution(message, spoiler_ranges):
    # 구간이 겹치지 않고 정렬되어 있어 스포 단어가 완전히 공개되는 순서는 단어 순서와 같으므로, 답은 스포 단어 중 비스포 구간에 등장한 적 없는 서로 다른 단어의 수(스포 단어 집합 - 비스포 단어 집합)다
    # 시간 복잡도: O(len(message))
    spoiled = [False] * len(message)
    for start, end in spoiler_ranges:
        spoiled[start : end + 1] = [True] * (end - start + 1)

    hidden, shown = set(), set()
    pos = 0  # 현재 단어의 시작 인덱스
    for word in message.split(" "):
        (hidden if any(spoiled[pos : pos + len(word)]) else shown).add(word)  # 문자 하나라도 스포 구간에 있으면 스포 단어
        pos += len(word) + 1  # 단어 길이 + 공백 하나
    return len(hidden - shown)
