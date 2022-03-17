import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap_list = []
        for num in nums:
            heapq.heappush(heap_list, -num)

        for _ in range(k):
            ret_val = heapq.heappop(heap_list)

        return -ret_val


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    solution = Solution()
    print(solution.findKthLargest(nums, k))

