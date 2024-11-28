class Solution:
    def longestPalindrome(self, s: str) -> str:

        ret_str = ""

        for i in range(len(s)):
            odd_li = i
            odd_ri = i
            even_li = i
            even_ri = i + 1

            while odd_li >= 0 and odd_ri < len(s) and s[odd_li] == s[odd_ri]:
                if len(ret_str) < odd_ri - odd_li + 1:
                    ret_str = s[odd_li:odd_ri + 1]

                odd_li = odd_li - 1
                odd_ri = odd_ri + 1


            while even_li >= 0 and even_ri < len(s) and s[even_li] == s[even_ri]:
                if len(ret_str) < even_ri - even_li + 1:
                    ret_str = s[even_li:even_ri + 1]
                even_li = even_li - 1
                even_ri = even_ri + 1

        return ret_str


if __name__ == "__main__":

    s = "cbbd"
    solution = Solution()
    print(solution.longestPalindrome(s))
