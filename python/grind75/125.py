class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_arr = []
        for ch in s:
            if ch.isalnum():
                filtered_arr.append(ch.lower())

        return filtered_arr == filtered_arr[::-1]


if __name__ == "__main__":
    # s = "A man, a plan, a canal: Panama"
    s = "0P"
    solution = Solution()
    print(solution.isPalindrome(s))
