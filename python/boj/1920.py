import sys
from typing import List

input = sys.stdin.readline


def in_n(target: int, n_list: List[int]) -> bool:
    def binary_search(left: int, right: int) -> bool:
        if left <= right:
            mid = left + (right - left) // 2
            if n_list[mid] < target:
                return binary_search(mid + 1, right)
            elif n_list[mid] > target:
                return binary_search(left, mid - 1)
            else:
                return True
        return False

    return binary_search(0, len(n_list) - 1)


def solution():
    n = int(input())
    n_list = list(map(int, input().split()))
    n_list.sort()

    m = int(input())
    m_list = list(map(int, input().split()))

    for num in m_list:
        if in_n(num, n_list):
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    solution()
