def solution(n, costs):
    # 다리를 비용 오름차순으로 보며, 아직 연결 안 된 두 그룹을 잇는 다리만 채택한다(크루스칼: 최소 비용으로 모든 섬을 잇는 표준 방법). 같은 그룹인지는 유니온 파인드(각 섬이 속한 그룹의 대표를 찾는 구조)로 판별.
    # 시간 복잡도: O(E log E) (E = len(costs))
    parent = list(range(n))

    def find(x):
        # 그룹 대표를 찾으며 지나온 노드를 대표에 바로 붙인다(경로 압축)
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    answer = count = 0
    for a, b, cost in sorted(costs, key=lambda x: x[2]):
        a, b = find(a), find(b)
        if a != b:  # 다른 그룹이면 이 다리를 채택하고 그룹을 합친다
            parent[b] = a
            answer += cost
            count += 1
            if count == n - 1:  # 다리 n-1개면 모든 섬이 연결됨
                break

    return answer
