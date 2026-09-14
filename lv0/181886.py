def solution(names):
    # 5칸 간격 슬라이스 [::5]를 쓰면 각 그룹의 맨 앞 사람만 뽑힌다
    return names[::5]
