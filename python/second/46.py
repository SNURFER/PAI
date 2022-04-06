from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(depth: int, visit: []):
            if depth == len(nums):
                result.append(visit)
                return

            for num in nums:
                if num not in visit:
                    dfs(depth + 1, visit + [num])

        dfs(0, [])

        return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.permute(nums))

