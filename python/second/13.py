class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        ret_val = 0
        for idx, ch in enumerate(s):
            if idx + 1 < len(s) and roman_dict[ch] < roman_dict[s[idx + 1]]:
                ret_val -= roman_dict[ch]
            else:
                ret_val += roman_dict[ch]

        return ret_val


if __name__ == "__main__":
    s = "MCMXCIV"
    solution = Solution()
    print(solution.romanToInt(s))
