def solution(key, lock):
    m, n = len(key), len(lock)

    def rotate(matrix):
        size = len(matrix)
        return [[matrix[size - 1 - r][c] for r in range(size)] for c in range(size)]

    def can_open(rotated_key):
        for row_offset in range(-(m - 1), n):
            for col_offset in range(-(m - 1), n):
                valid = True

                for r in range(n):
                    for c in range(n):
                        key_r = r - row_offset
                        key_c = c - col_offset

                        key_value = 0
                        if 0 <= key_r < m and 0 <= key_c < m:
                            key_value = rotated_key[key_r][key_c]

                        if lock[r][c] + key_value != 1:
                            valid = False
                            break

                    if not valid:
                        break

                if valid:
                    return True

        return False

    rotated_key = key

    for _ in range(4):
        if can_open(rotated_key):
            return True
        rotated_key = rotate(rotated_key)

    return False
