class Solution(object):
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s[::-1] == s:
            return s

        def expect(left:int, right:int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1:right]

        result = ''
        for i in range(0, len(s) - 1):
            result = max(result, expect(i, i + 1), expect(i, i + 2), key=len)

        return result


if __name__ == "__main__":
    s = "babad"
    solution = Solution()
    # print(solution.longestPalindrome(s))

    test ="abcdefg"
    print(test[::-1])
    print(test[6:0:-1])
