def solution(array, height):
    # 비교 결과 True는 1로 계산되므로, 키가 height보다 큰 사람마다 1을 더해 인원수를 센다
    return sum(h > height for h in array)
