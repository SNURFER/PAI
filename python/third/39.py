from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(depth: int, path: List[int], path_sum: int):
            if path_sum > target:
                return
            if path_sum == target:
                result.append(path)
                return

            for i in range(depth, len(candidates)):
                dfs(i, path + [candidates[i]], path_sum + candidates[i])

        dfs(0, [], 0)
        return result


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    solution = Solution()
    print(solution.combinationSum(candidates, target))