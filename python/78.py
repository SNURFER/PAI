from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dfs(index: int, path: List[int]):
            if index == len(nums):
                output.append(path)
                return

            dfs(index + 1, path + [nums[index]])
            dfs(index + 1, path)

        dfs(0, [])

        return output


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.subsets(nums))
