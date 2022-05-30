class Solution:
    def isValid(self, s: str) -> bool:
        paren_dic = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        paren_stack = []

        for ch in s:
            if ch in paren_dic:
                if not paren_stack:
                    return False

                if paren_stack[-1] == paren_dic[ch]:
                    paren_stack.pop()
                else:
                    return False
            else:
                paren_stack.append(ch)

        if paren_stack:
            return False
        return True


if __name__ == '__main__':
    # s = "()[]{}"
    s = "(){()}"
    solution = Solution()
    print(solution.isValid(s))
