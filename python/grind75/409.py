import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ch_counter = collections.Counter(s)
        length = 0
        has_odd = False
        for ch in ch_counter:
            if ch_counter[ch] % 2 == 0:
                length += ch_counter[ch]
            else:
                has_odd = True
                length += (ch_counter[ch] - 1)

        return length + 1 if has_odd else length


if __name__ == "__main__":
    # test = "aaaadddddcdss"
    test = "ccc"
    solution = Solution()
    print(solution.longestPalindrome(test))
