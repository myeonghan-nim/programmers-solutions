def solution(n, build_frame):
    # 명령을 그대로 흉내 내되, 일단 반영해 보고 규칙에 어긋나면 되돌리는 방식. 설치는 새로 놓은 구조물 하나만 검사하면 되고(추가는 남을 방해하지 않음), 삭제는 영향을 받을 수 있는 주변 3x3 범위의 구조물만 다시 검사하면 된다.
    # 시간 복잡도: O(명령 수) (명령마다 검사하는 구조물이 상수 개)
    COLUMN = 0
    BEAM = 1

    structure = set()

    def can_exist(x, y, kind):
        if kind == COLUMN:
            # 기둥: 바닥 위이거나, 아래에 기둥이 있거나, 한쪽 끝이 보 위에 있어야 함
            return y == 0 or (x, y - 1, COLUMN) in structure or (x - 1, y, BEAM) in structure or (x, y, BEAM) in structure

        # 보: 한쪽 끝 아래에 기둥이 있거나, 양옆이 모두 보와 연결되어야 함
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
