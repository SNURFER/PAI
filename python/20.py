from typing import List


class Solution():
    def isValid(self, s: str) -> bool:
        stack: List = []
        table = {
            '{': '}',
            '[': ']',
            '(': ')',
        }

        for ch in s:
            if ch not in table:
                if len(stack) == 0 or table[stack.pop()] != ch:
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0

if __name__ == "__main__":
    input_str: str = '('
    solution = Solution()

    print(solution.isValid(input_str))
