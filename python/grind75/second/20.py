class Solution:
    def isValid(self, s: str) -> bool:
        valid_checker = {
            "{": "}",
            "[": "]",
            "(": ")",
        }
        ch_stack = []
        for ch in s:
            if ch in valid_checker:
                ch_stack.append(ch)
            else:
                if len(ch_stack) == 0:
                    return False
                top_element = ch_stack[-1]
                if valid_checker[top_element] == ch:
                    ch_stack.pop()
                else:
                    return False

        if len(ch_stack) > 0:
            return False
        return True


if __name__ == "__main__":
    s: str = "({)"
    solution = Solution()
    print(solution.isValid(s))