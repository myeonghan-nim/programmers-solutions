def solution(key, lock):
    # 열쇠를 4가지 방향으로 회전시키며, 자물쇠와 겹칠 수 있는 모든 위치에 놓아 본다. 자물쇠의 모든 칸에서 (자물쇠 값 + 겹친 열쇠 값)이 정확히 1이면 홈이 전부 채워지고 돌기끼리 부딪히지도 않는 것이므로 열 수 있다.
    # 시간 복잡도: O(4 * (N+M)^2 * N^2) (크기가 최대 20이라 충분히 빠름)
    m, n = len(key), len(lock)

    def rotate(matrix):
        # 시계 방향으로 90도 회전한 새 배열을 만든다
        size = len(matrix)
        return [[matrix[size - 1 - r][c] for r in range(size)] for c in range(size)]

    def can_open(rotated_key):
        for row_offset in range(-(m - 1), n):
            for col_offset in range(-(m - 1), n):
                valid = True

                for r in range(n):
                    for c in range(n):
                        # 자물쇠 칸 (r, c) 위에 겹쳐진 열쇠 칸의 위치
                        key_r = r - row_offset
                        key_c = c - col_offset

                        key_value = 0  # 열쇠 범위 밖이면 아무것도 겹치지 않음
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
