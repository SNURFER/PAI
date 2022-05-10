import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = collections.Counter()

        ret_val = left = 0

        for right in range(len(s)):
            counter[s[right]] += 1
            most_common_ch = counter.most_common(1)[0][1]

            if right - left + 1 - most_common_ch > k:
                counter[s[left]] -= 1
                left += 1
            ret_val = max(right + 1 - left, ret_val)

        return ret_val


if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    # s = "ABAB"
    # k = 2
    solution = Solution()
    print(solution.characterReplacement(s, k))
