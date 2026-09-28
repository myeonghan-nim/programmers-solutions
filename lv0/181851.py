def solution(rank, attendance):
    # 참석 가능한 학생 번호만 모아 등수가 좋은 순서로 정렬한 뒤 앞의 3명(a, b, c)을 골라 10000×a + 100×b + c로 합친다
    a, b, c = sorted((i for i in range(len(rank)) if attendance[i]), key=lambda i: rank[i])[:3]
    return 10000 * a + 100 * b + c
