from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret_val = []

        def dfs(n_l: int, n_r: int, path: str):
            if n_l == n and n_r == n:
                ret_val.append(path)
                return

            if n_l > n_r:
                if n_l < n:
                    dfs(n_l + 1, n_r, path + "(")
                dfs(n_l, n_r + 1, path + ")")
            else:
                dfs(n_l + 1, n_r, path + "(")

        dfs(1, 0, "(")

        return ret_val


if __name__ == "__main__":
    n = 3
    solution = Solution()
    print(solution.generateParenthesis(3))
