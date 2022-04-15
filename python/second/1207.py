import collections
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        return len(c) == len(set(c.values()))

if __name__ == "__main__":
    arr = [1, 2, 2, 1, 1, 3]
    solution = Solution()
    print(solution.uniqueOccurrences(arr))