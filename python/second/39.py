from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum: int, index: int, path: []):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])

        return result


if __name__ == "__main__":
    # candidates = [2, 3, 6, 7]
    # target = 7
    candidates = [0]
    target = 0
    solution = Solution()
    print(solution.combinationSum(candidates, target))