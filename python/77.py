from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []

        def dfs(cur_num: int, depth: int, combine_list: List[int]):
            if depth == k:
                output.append(combine_list)
                return

            for num in range(cur_num + 1, n + 1):
                if num <= n:
                    update_list = combine_list[:]
                    update_list.append(num)
                    dfs(num, depth + 1, update_list)

        dfs(0, 0, [])

        return output


if __name__ == "__main__":
    solution = Solution()

    n = 4
    k = 2

    print(solution.combine(4, 2))
