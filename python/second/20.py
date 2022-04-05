class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        bracket_form = {
            ')' : '(',
            '}': '{',
            ']': '[',
        }

        for br in list(s):
            if br == '{' or br == '(' or br == '[':
                bracket_stack.append(br)
            else:
                if not bracket_stack:
                    return False

                if bracket_form[br] == bracket_stack[-1]:
                    bracket_stack.pop()
                else:
                    return False

        if bracket_stack:
            return False

        return True


if __name__ == '__main__':
    s = "()[]{}"
    solution = Solution()
    print(solution.isValid(s))
