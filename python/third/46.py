from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(depth: int, sub_list: List[int]):
            if depth == len(nums):
                result.append(sub_list)
                return

            for num in nums:
                if num not in sub_list:
                    dfs(depth + 1, sub_list + [num])

        dfs(0, [])

        return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.permute(nums))

