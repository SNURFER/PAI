import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_cnt = collections.Counter(nums)

        sort_list = []
        for key in num_cnt:
            heapq.heappush(sort_list, (-num_cnt[key], key))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(sort_list)[1])

        return result


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    solution = Solution()
    print(solution.topKFrequent(nums, k))