class Solution:
    def isPalindrome(self, s: str) -> bool:
        fixed_str = []
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                fixed_str.append(ch.lower())

        return fixed_str == fixed_str[::-1]


if __name__ == "__main__":
    # s = "A man, a plan, a canal: Panama"
    # s = "0A"
    s = "race a car"
    solution = Solution()
    print(solution.isPalindrome(s))