from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index: int, path: str):
            if len(path) == len(digits):
                ret_str.append(path)
                return

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)


        ret_str = []
        if len(digits) == 0:
            return ret_str

        dic = {
            '2': ['a'],
            '3': ['d'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        dfs(0, '')
        return ret_str


if __name__ == "__main__":
    solution = Solution()

    digits = '789'

    print(solution.letterCombinations(digits))
