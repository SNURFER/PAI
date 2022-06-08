from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(depth: int, path: List[int]):
            if depth == len(nums) - 1:
                result.append(path)
                return

            dfs(depth + 1, path)
            dfs(depth + 1, path + [nums[depth + 1]])

        dfs(-1, [])

        return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.subsets(nums))
