class Solution:
    def longestPalindrome(self, s: str) -> int:
        single_ch = {}
        ch_counter = {}

        for ch in s:
            if single_ch.get(ch):
                single_ch.pop(ch)
                ch_counter[ch] = 2
            elif ch_counter.get(ch):
                ch_counter[ch] += 1
            else:
                single_ch[ch] = 1

        pd_counter = 0
        single_switch: bool = False
        for _, value in ch_counter.items():
            if value % 2 == 1:
                single_switch = True
                pd_counter += value - 1
            else:
                pd_counter += value

        if single_switch or len(single_ch):
            return pd_counter + 1
        return pd_counter


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("abbbbcde"))
