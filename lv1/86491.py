def solution(sizes):
    # 모든 명함을 긴 쪽이 가로가 되도록 눕혀 놓으면, 가로 최댓값 × 세로 최댓값이 최소 지갑 크기가 된다
    # 시간 복잡도: O(n)
    return max(max(w, h) for w, h in sizes) * max(min(w, h) for w, h in sizes)
