from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        post_str: List[str] = []
        for ch in s:
            if ch.isalnum():
                post_str.append(ch.lower())

        return post_str == post_str[::-1]


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    solution = Solution()
    print(solution.isPalindrome(s))
