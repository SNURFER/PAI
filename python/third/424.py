import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0

        ch_counter = collections.Counter()
        max_len = 0
        for right in range(0, len(s)):
            ch_counter[s[right]] += 1

            max_common = ch_counter.most_common(1)[0][1]
            if (right - left + 1) - max_common > k:
                ch_counter[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    # s = "ABAB"
    # k = 2
    # s = "AABABBA"
    # k = 1
    s = "ABAA"
    k = 0
    solution = Solution()
    print(solution.characterReplacement(s, k))
