class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = start_idx = 0
        used_map = {}

        for idx, ch in enumerate(s):
            #if not defined key in dictionary get runtime error used_map[ch]
            if used_map.get(ch) is not None and used_map[ch] >= start_idx:
                start_idx = used_map[ch] + 1
            else:
                max_length = max(max_length, idx - start_idx + 1)
            used_map[ch] = idx

        return max_length


if __name__ == "__main__":
    solution = Solution()
    input_str = "abcabcbb"

    print(solution.lengthOfLongestSubstring(input_str))
