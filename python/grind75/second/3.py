class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idx_checker = {}
        max_sub_len = 0
        left_idx = 0

        for i in range(len(s)):
            if s[i] in idx_checker and idx_checker[s[i]] >= left_idx:
                sub_len = i - idx_checker[s[i]]
                max_sub_len = max(max_sub_len, sub_len)
                left_idx = idx_checker[s[i]] + 1
                idx_checker[s[i]] = i

            else:
                max_sub_len = max(max_sub_len, i - left_idx + 1)

            idx_checker[s[i]] = i

            print("left idx , max sub len ", left_idx, max_sub_len)

        return max_sub_len


if __name__ == "__main__":
    s = "tmmzuxt"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))