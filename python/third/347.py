import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [item[0] for item in collections.Counter(nums).most_common(k)]


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    solution = Solution()
    print(solution.topKFrequent(nums, k))
