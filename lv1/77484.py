def solution(lottos, win_nums):
    # 확실히 맞힌 개수(hit)와 알아볼 수 없는 번호 개수(zero)를 세고, 맞힌 개수를 등수로 바꾼다: 0으로 지워진 번호가 전부 맞으면 최고, 전부 틀리면 최저 순위
    # 시간 복잡도: O(n)
    hit = len(set(lottos) & set(win_nums))
    zero = lottos.count(0)
    rank = [6, 6, 5, 4, 3, 2, 1]  # 맞힌 개수 0~6개를 등수로 변환, 0개와 1개는 모두 6등(낙첨)
    return [rank[hit + zero], rank[hit]]
