from string import ascii_lowercase


def solution(s, skip, index):
    # skip을 뺀 알파벳 목록을 만들고, 각 문자의 위치에서 index만큼 순환 이동한 문자로 바꾼다 (s의 문자는 skip에 없음이 보장됨)
    # 시간 복잡도: O(26 + S) (S: s의 길이)
    letters = [ch for ch in ascii_lowercase if ch not in skip]
    return "".join(letters[(letters.index(ch) + index) % len(letters)] for ch in s)
