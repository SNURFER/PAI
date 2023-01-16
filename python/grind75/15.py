from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        length = len(nums)

        def dfs(idx: int, triplet: List[int]):
            if len(triplet) == 3:
                if sum(triplet) == 0:
                    triplets.append(sorted(triplet))
                return

            for i in range(idx + 1, length):
                dfs(i, triplet + [nums[i]])

        for i in range(length - 2):
            dfs(i, [nums[i]])

        return list(set(list(map(tuple, triplets))))


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    print(solution.threeSum(nums))
