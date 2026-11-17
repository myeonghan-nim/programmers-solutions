def solution(players, m, k):
    # 시간 순서대로 보면서 지금 필요한 서버 수(이용자 // m)보다 운영 중인 서버가 모자랄 때만 모자란 만큼 증설한다. 미리 증설하면 반납만 빨라질 뿐 이득이 없으므로 이 방법이 최소다
    # 시간 복잡도: O(len(players))
    added_servers = [0] * len(players)  # 시각별로 증설한 서버 수. k시간 뒤에 반납할 양을 알기 위해 적어 둔다
    running_servers = 0
    for hour, player_count in enumerate(players):
        if hour >= k:
            running_servers -= added_servers[hour - k]
        shortage = player_count // m - running_servers
        if shortage > 0:
            added_servers[hour] = shortage
            running_servers += shortage
    return sum(added_servers)
