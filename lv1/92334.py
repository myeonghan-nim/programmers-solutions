def solution(id_list, report, k):
    # 중복 신고를 집합으로 걷어낸 뒤 유저별 신고당한 횟수를 세고, 각 유저가 신고한 대상 중 k번 이상 신고된 유저 수를 메일 횟수로 돌려준다
    # 시간 복잡도: O(n + m), n은 유저 수, m은 신고 수
    reported = {user: set() for user in id_list}  # 신고당한 유저 → 신고한 유저 집합
    for line in set(report):
        reporter, target = line.split()
        reported[target].add(reporter)
    mail = {user: 0 for user in id_list}
    for reporters in reported.values():
        if len(reporters) >= k:  # 정지된 유저를 신고한 모두에게 메일 1통씩
            for reporter in reporters:
                mail[reporter] += 1
    return [mail[user] for user in id_list]
