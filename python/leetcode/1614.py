from typing import List


class Solution:
    def maxDepth(self, s: str) -> int:
        stack: List[int] = []
        max_depth: int = 0
        depth_count: int = 0

        for ch in s:
            if ch == "(":
                depth_count += 1
                max_depth = max(depth_count, max_depth)
                stack.append(ch)
            elif ch == ")":
                if stack[-1] == "(":
                    depth_count -= 1
                    stack.pop()

        return max_depth


if __name__ == "__main__":
    # s = "(1+(2*3)+((8)/4))+1"
    s = "(1)+((2))+(((3)))"
    solution = Solution()
    print(solution.maxDepth(s))
