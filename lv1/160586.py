def solution(keymap, targets):
    # 문자마다 모든 키를 통틀어 가장 적게 눌러도 되는 횟수를 미리 구해 두고, 목표 문자열마다 그 값을 더한다 (없는 문자가 있으면 -1)
    # 시간 복잡도: O(K + T) (K: keymap의 모든 문자 수의 합, T: targets의 모든 문자 수의 합)
    presses = {}
    for key in keymap:
        for i, ch in enumerate(key, 1):
            presses[ch] = min(presses.get(ch, i), i)
    answer = []
    for target in targets:
        answer.append(sum(presses[ch] for ch in target) if all(ch in presses for ch in target) else -1)
    return answer
