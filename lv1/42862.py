def solution(n, lost, reserve):
    # 여벌이 있으면서 도난당한 학생은 자기 것을 입으므로 양쪽에서 먼저 뺀다. 남은 도난 학생을 번호 순으로 보며 앞번호 여벌부터 빌리면 뒷번호 여벌이 다음 학생 몫으로 남아 최적이다
    # 시간 복잡도: O(n log n)
    lost, reserve = set(lost) - set(reserve), set(reserve) - set(lost)
    for student in sorted(lost):
        for lender in (student - 1, student + 1):
            if lender in reserve:
                reserve.discard(lender)
                lost.discard(student)
                break
    return n - len(lost)
