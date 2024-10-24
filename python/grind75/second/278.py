# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left: int = 1
        right: int = n

        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    solution = Solution()
    print(solution.firstBadVersion(5))
