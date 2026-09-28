def solution(arr, flag):
    # flag가 true면 arr[i]를 arr[i]×2번 뒤에 붙이고, false면 뒤에서 arr[i]개를 지운다
    x = []
    for a, f in zip(arr, flag):
        if f:
            x += [a] * (a * 2)
        else:
            del x[-a:]
    return x
