def solution(n, build_frame):
    COLUMN = 0
    BEAM = 1

    structure = set()

    def can_exist(x, y, kind):
        if kind == COLUMN:
            return y == 0 or (x, y - 1, COLUMN) in structure or (x - 1, y, BEAM) in structure or (x, y, BEAM) in structure

        return (x, y - 1, COLUMN) in structure or (x + 1, y - 1, COLUMN) in structure or ((x - 1, y, BEAM) in structure and (x + 1, y, BEAM) in structure)

    def affected_parts(x, y):
        parts = set()
        for nx in range(x - 1, x + 2):
            for ny in range(y - 1, y + 2):
                for kind in (COLUMN, BEAM):
                    part = (nx, ny, kind)
                    if part in structure:
                        parts.add(part)
        return parts

    for x, y, kind, command in build_frame:
        part = (x, y, kind)

        if command == 1:
            structure.add(part)
            if not can_exist(x, y, kind):
                structure.remove(part)
        else:
            structure.remove(part)
            if not all(can_exist(*candidate) for candidate in affected_parts(x, y)):
                structure.add(part)

    return [list(part) for part in sorted(structure)]
