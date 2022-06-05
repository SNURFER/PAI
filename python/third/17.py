from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        num_letter = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z'],
        }
        ret_val = []

        def dfs(depth: int, path: str):
            if depth == len(digits) - 1:
                ret_val.append(path)
                return

            for ch in num_letter[digits[depth + 1]]:
                dfs(depth + 1, path + ch)

        for ch in num_letter[digits[0]]:
            dfs(0, ch)
        return ret_val


if __name__ == "__main__":
    digits = "23"
    solution = Solution()
    print(solution.letterCombinations(digits))
