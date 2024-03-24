class Solution:
    def isValid(self, s: str) -> bool:
        ch_stack = []
        pair_dic = {
            '}': '{',
            ']': '[',
            ')': '(',
        }
        for ch in s:
            if ch == '{' or ch == '[' or ch == '(':
                ch_stack.append(ch)
            else:
                if len(ch_stack) == 0:
                    return False
                if pair_dic[ch] != ch_stack.pop():
                    return False

        if len(ch_stack) != 0:
            return False

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("("))
