import collections
import sys
from typing import List


# TODO) timeout. need to solve with another solution
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        max_num = -sys.maxsize

        window = collections.deque()

        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            if max_num == -sys.maxsize:
                max_num = max(window)
            elif max_num < v:
                max_num = v

            result.append(max_num)

            if max_num == window.popleft():
                max_num = -sys.maxsize

        return result


if __name__ == "__main__":
    # nums = [1]
    # k = 1

    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    solution = Solution()
    print(solution.maxSlidingWindow(nums, k))