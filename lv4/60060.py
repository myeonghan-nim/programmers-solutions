from bisect import bisect_left, bisect_right
from collections import defaultdict


def count_by_range(words, left_value, right_value):
    # 정렬된 목록에서 left_value 이상 right_value 이하인 단어 수를 이분 탐색으로 센다
    left_index = bisect_left(words, left_value)
    right_index = bisect_right(words, right_value)
    return right_index - left_index


def solution(words, queries):
    # 단어를 길이별로 모아 정렬해 두면 "fro??"는 "froaa" 이상 "frozz" 이하의 범위 검색으로 바뀐다. '?'가 앞에 붙은 검색어는 단어를 뒤집어 둔 목록에서 같은 방식으로 찾는다.
    # 시간 복잡도: O(W log W + Q log W) (W: 단어 수, Q: 검색어 수)
    forward_words = defaultdict(list)
    reversed_words = defaultdict(list)

    for word in words:
        length = len(word)

        forward_words[length].append(word)
        reversed_words[length].append(word[::-1])

    for word_list in forward_words.values():
        word_list.sort()

    for word_list in reversed_words.values():
        word_list.sort()

    answer = []
    for query in queries:
        length = len(query)

        if query[0] == '?':  # '?'가 앞쪽이면 뒤집어서 접미사 문제를 접두사 문제로 바꾼다
            converted_query = query[::-1]
            target_words = reversed_words[length]
        else:
            converted_query = query
            target_words = forward_words[length]

        left_value = converted_query.replace('?', 'a')  # 범위의 가장 작은 단어
        right_value = converted_query.replace('?', 'z')  # 범위의 가장 큰 단어

        count = count_by_range(target_words, left_value, right_value)

        answer.append(count)

    return answer
