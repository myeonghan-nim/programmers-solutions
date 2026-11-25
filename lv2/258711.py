from collections import Counter


def solution(edges):
    # 그래프를 따라가 보지 않고 정점의 들어오는·나가는 간선 수만으로 구분한다. 생성한 정점은 들어오는 간선이 없고 나가는 간선이 2개 이상인 유일한 정점이며, 그 나가는 간선 수가 곧 전체 그래프 수다
    # 시간 복잡도: O(간선 수)
    out_degree = Counter(source for source, _ in edges)
    in_degree = Counter(target for _, target in edges)
    created = next(vertex for vertex, degree in out_degree.items() if degree >= 2 and vertex not in in_degree)
    # 막대 모양 그래프마다 나가는 간선이 없는 끝 정점이 정확히 하나 있다
    stick_count = sum(1 for vertex in in_degree if vertex not in out_degree)
    # 8자 모양 그래프마다 나가는 간선이 2개인 가운데 정점이 정확히 하나 있다. 생성한 정점도 나가는 간선이 2개일 수 있어 들어오는 간선이 있는 정점만 센다
    eight_count = sum(1 for vertex, degree in out_degree.items() if degree == 2 and vertex in in_degree)
    donut_count = out_degree[created] - stick_count - eight_count
    return [created, donut_count, stick_count, eight_count]
