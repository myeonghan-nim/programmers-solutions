def solution(numbers):
    # 0부터 9까지의 총합 45에서 주어진 숫자들의 합을 빼면 없는 숫자들의 합이 된다: numbers에 중복이 없어 그대로 뺄 수 있다
    # 시간 복잡도: O(n)
    return 45 - sum(numbers)
