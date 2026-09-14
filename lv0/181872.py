def solution(my_string, pat):
    # pat이 마지막으로 나온 위치(rindex)까지 앞부분을 통째로 자르면 pat으로 끝나는 가장 긴 부분 문자열이 된다
    return my_string[:my_string.rindex(pat) + len(pat)]
