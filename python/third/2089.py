from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        cnt = nums.count(target)
        if cnt:
            idx = nums.index(target)
            return [idx + i for i in range(0, cnt)]
        return []


if __name__ == "__main__":
    nums = [1, 2, 5, 2, 3]
    target = 4
    solution = Solution()
    print(solution.targetIndices(nums, target))
