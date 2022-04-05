import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ch_cnt = collections.Counter(list(s))




if __name__ == '__main__':
    s = "cbacdcbc"
    solution = Solution()
    solution.removeDuplicateLetters(s)
