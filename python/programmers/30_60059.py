from typing import List


def solution(key, lock):
    m = len(key)
    hom_range = getHomRange(lock)

    # check if hom range is larger than key.
    if hom_range[1][0] - hom_range[0][0] + 1 > m or \
            hom_range[1][1] - hom_range[0][1] + 1 > m:
        return False

    i_min, j_min, i_max, j_max = hom_range[0][0], hom_range[0][1], hom_range[1][0], hom_range[1][1]

    # fix position of right bottom key idx to real lock idx
    for i in range(i_max, i_min + m):
        for j in range(j_max, j_min + m):
            for _ in range(4):
                if check(lock, key, i, j):
                    return True
                rotateQuarter(key)

    return False


def rotateQuarter(key: List[List[int]]):
    key.reverse()
    for i in range(len(key)):
        for j in range(i, len(key)):
            key[i][j], key[j][i] = key[j][i], key[i][j]


def getHomRange(lock: List[List[int]]) -> List[int]:
    hom_x: List[int] = []
    hom_y: List[int] = []

    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                hom_x.append(i)
                hom_y.append(j)

    return [[min(hom_x), min(hom_y)], [max(hom_x), max(hom_y)]]


def check(lock: List[List[int]], key: List[List[int]], rb_i: int, rb_j: int) -> bool:
    shift_i = (len(key) - 1) - rb_i
    shift_j = (len(key) - 1) - rb_j

    for i in reversed(range(rb_i + 1)):
        for j in reversed(range(rb_j + 1)):
            if not 0 <= i < len(lock) or not 0 <= j < len(lock):
                continue
            if not 0 <= i + shift_i < len(key) or not 0 <= j + shift_j < len(key):
                continue
            if key[i + shift_i][j + shift_j] is lock[i][j]:
                return False
    return True


if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [1, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))
