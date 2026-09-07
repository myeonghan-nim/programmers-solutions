def solution(arrows):
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    current = (0, 0)
    visited_vertices = {current}
    visited_edges = set()
    rooms = 0

    for arrow in arrows:
        dx, dy = directions[arrow]

        for _ in range(2):
            nxt = (current[0] + dx, current[1] + dy)

            edge = (current, nxt) if current < nxt else (nxt, current)

            if edge not in visited_edges:
                if nxt in visited_vertices:
                    rooms += 1

                visited_edges.add(edge)
                visited_vertices.add(nxt)

            current = nxt

    return rooms
