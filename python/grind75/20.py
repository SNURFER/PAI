

class Solution:
    def isValid(self, s: str) -> bool:
        left_br = ['{', '[', '(']
        right_br = ['}', ']', ')']
        stack = []
        for ch in s:
            if ch in left_br:
                stack.append(ch)
            elif ch in right_br and len(stack) > 0:
                matcher_idx = right_br.index(ch)
                if stack.pop() is not left_br[matcher_idx]:
                    return False
            else:
                return False

        if len(stack) > 0:
            return False

        return True


if __name__ == "__main__":
    s = "("
    solution = Solution()
    print(solution.isValid(s))


