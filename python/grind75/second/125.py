class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_idx = 0
        right_idx = len(s) - 1

        while left_idx < right_idx:
            if not s[left_idx].isalnum():
                left_idx += 1
                continue
            if not s[right_idx].isalnum():
                right_idx -= 1
                continue

            if s[left_idx].lower() != s[right_idx].lower():
                return False

            left_idx += 1
            right_idx -= 1

        return True


if __name__ == "__main__":
    s = "A man, a plan, a canal:p Panama"
    solution = Solution()
    print(solution.isPalindrome(s))

