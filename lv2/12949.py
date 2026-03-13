def solution(arr1, arr2):
    answer = [[]]
    reversed_arr2 = list(zip(*arr2))
    for row in arr1:
        for col in reversed_arr2:
            answer[-1].append(sum(a * b for a, b in zip(row, col)))
        answer.append([])
    return answer[:-1]
