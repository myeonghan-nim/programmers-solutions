from bisect import bisect_left, bisect_right
from collections import defaultdict


def count_by_range(words, left_value, right_value):
    left_index = bisect_left(words, left_value)
    right_index = bisect_right(words, right_value)
    return right_index - left_index


def solution(words, queries):
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

        if query[0] == '?':
            converted_query = query[::-1]
            target_words = reversed_words[length]
        else:
            converted_query = query
            target_words = forward_words[length]

        left_value = converted_query.replace('?', 'a')
        right_value = converted_query.replace('?', 'z')

        count = count_by_range(target_words, left_value, right_value)

        answer.append(count)

    return answer
