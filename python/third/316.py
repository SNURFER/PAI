import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ch_cnt, stack = collections.Counter(list(s)), []

        for ch in s:
            ch_cnt[ch] -= 1
            if ch in stack:
                continue
            while stack and ch < stack[-1] and ch_cnt[stack[-1]] > 0:
                stack.pop()

            stack.append(ch)

        return ''.join(stack)


if __name__ == '__main__':
    s = "cbacdcbc"
    # s = "bcabc"
    solution = Solution()
    print(solution.removeDuplicateLetters(s))
