import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        s_idx = 0
        sub_cnt = collections.Counter([])
        for i in range(len(s)):
            sub_cnt[s[i]] += 1

            if sub_cnt.most_common(1)[0][1] > 1:

                while sub_cnt.most_common(1)[0][1] > 1:
                    sub_cnt[s[s_idx]] -= 1
                    s_idx += 1

            max_len = max(max_len, i - s_idx + 1)

        return max_len


if __name__ == "__main__":
    s = "abcabcbb"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))
