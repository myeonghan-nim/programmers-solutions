def solution(arr):
    # 첫 2의 위치부터 마지막 2의 위치까지 자르면 모든 2를 포함하는 가장 짧은 구간이 되고, 2가 없으면 [-1]을 돌려준다
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2):len(arr) - arr[::-1].index(2)]
