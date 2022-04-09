from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def dfs(depth: int, path: []):
            if depth == len(nums) - 1:
                output.append(path)
                return

            dfs(depth + 1, path + [nums[depth + 1]])
            dfs(depth + 1, path)

        dfs(-1, [])

        return output


if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.subsets(nums))
