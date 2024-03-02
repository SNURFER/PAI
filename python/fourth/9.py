
from typing import List
class Solution:
    def isPalindrome(self, x: int) -> bool:
        to_str: str = str(x)
        to_list: [] = list(to_str)
        return to_list == to_list[::-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(-121))


