def solution(players, callings):
    # 이름별 현재 등수를 딕셔너리로 들고 있다가, 불린 선수와 바로 앞 선수의 자리와 등수를 맞바꾼다 (list.index로 매번 찾으면 O(N)이라 시간 초과)
    # 시간 복잡도: O(N + C) (N: players의 길이, C: callings의 길이)
    rank = {player: i for i, player in enumerate(players)}
    for player in callings:
        i = rank[player]
        front = players[i - 1]
        players[i - 1], players[i] = player, front
        rank[player], rank[front] = i - 1, i
    return players
