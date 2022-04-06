from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        result = []

        def dfs(depth: int, path: str):
            if depth == len(digits):
                if path:
                    result.append(path)
                return

            avail_chs = num_dic[digits[depth]]
            for ch in avail_chs:
                dfs(depth + 1, path + ch)

        dfs(0, '')

        return result


if __name__ == "__main__":
    # digits = "23"
    digits = ""
    solution = Solution()
    print(solution.letterCombinations(digits))
