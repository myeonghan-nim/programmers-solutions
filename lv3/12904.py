def solution(s):
    t = "#" + "#".join(s) + "#"
    n = len(t)
    radius = [0] * n

    center = 0
    right = 0

    for i in range(n):
        mirror = 2 * center - i

        if i < right:
            radius[i] = min(right - i, radius[mirror])

        while i - radius[i] - 1 >= 0 and i + radius[i] + 1 < n and t[i - radius[i] - 1] == t[i + radius[i] + 1]:
            radius[i] += 1

        if i + radius[i] > right:
            center = i
            right = i + radius[i]

    return max(radius)
