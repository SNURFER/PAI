from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(sum: int, index: int, path: List[int]):
            if sum == 0:
                output.append(path)
                return
            if sum < 0:
                return

            for i in range(index, len(candidates)):
                ######## list + list pretty cool~!
                dfs(sum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])

        return output


if __name__ == "__main__":
    solution = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(solution.combinationSum(candidates, target))