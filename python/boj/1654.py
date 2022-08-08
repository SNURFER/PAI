import sys
from typing import List

input = sys.stdin.readline

def solution():
    k, n = map(int, input().split())
    k_nums: List[int] = []
    for _ in range(k):
        k_nums.append(int(input()))

    k_nums.sort()

    ret_n = 0
    left, right = 1, k_nums[-1]
    while left <= right:
        mid = left + (right - left) // 2
        cal_n = 0
        for num in k_nums:
            cal_n += num // mid

        if cal_n > n:
            ret_n = mid
            left = mid + 1
        elif cal_n < n:
            right = mid - 1
        else:
            ret_n = mid
            left = mid + 1

    return ret_n


if __name__ == "__main__":
    print(solution())
