import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []

        result = []
        for idx, num in enumerate(nums):
            heapq.heappush(window, (-num, idx))

            if idx >= k - 1:
                while idx - window[0][1] >= k:
                    heapq.heappop(window)
                result.append(-window[0][0])

        return result


if __name__ == "__main__":
    # nums = [1, 3, -1, -3, 5, 3, 6, 7]
    # k = 3
    nums = [1]
    k = 1
    solution = Solution()
    print(solution.maxSlidingWindow(nums, k))

