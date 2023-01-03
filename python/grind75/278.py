# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    if version > 1:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        mid = r + (l - r) // 2

        while l <= r:
            mid = r + (l - r) // 2
            if isBadVersion(mid):
                if mid - 1 > 0 and isBadVersion(mid - 1):
                    r = mid - 1
                else:
                    break
            else:
                l = mid + 1

        return mid


if __name__ == "__main__":
    solution = Solution()
    print(solution.firstBadVersion(3))
