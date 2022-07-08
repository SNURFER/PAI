import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret_val = []
        window = []
        for i in range(0, len(nums)):
            heapq.heappush(window, (-nums[i], i))
            if i >= k - 1:
                while not i - k + 1 <= window[0][1] <= i:
                    heapq.heappop(window)

                ret_val.append(-window[0][0])

        return ret_val


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    solution = Solution()
    print(solution.maxSlidingWindow(nums, k))
