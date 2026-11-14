def solution(strings, n):
    # 정렬 키를 (n번째 글자, 문자열 전체) 튜플로 주면 n번째 글자가 같을 때 사전순으로 앞선 문자열이 앞에 온다
    # 시간 복잡도: O(m log m), m은 strings의 길이
    return sorted(strings, key=lambda string: (string[n], string))
