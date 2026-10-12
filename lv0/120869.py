def solution(spell, dic):
    # 글자를 한 번씩만 모두 쓴 단어는 정렬했을 때 spell을 정렬한 것과 같으므로, 그런 단어가 사전에 있는지 확인한다
    return 1 if any(sorted(word) == sorted(spell) for word in dic) else 2
