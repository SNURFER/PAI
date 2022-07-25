
class Solution:
    path_cnt = 0

    def solve(self, n: int, k: int, nums: []) -> int:
        for i in range(len(nums)):
            nums[i] -= k

        def dfs(depth: int, sum: int, path: []):
            if depth == n:
                self.path_cnt += 1
                return

            for i in range(len(nums)):
                if nums[i] + sum >= 0 and i not in path:
                    dfs(depth + 1, nums[i] + sum, path + [i])

        dfs(0, 0, [])
        return self.path_cnt


if __name__ == "__main__":
    N, K = [int(item) for item in input().split()]
    nums = [int(x) for x in input().split()]

    solution = Solution()
    print(solution.solve(N, K, nums))
