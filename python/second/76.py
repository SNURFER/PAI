import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needs = collections.Counter(t)
        missing = len(t)

        left = start = end = 0

        for idx, char in enumerate(s, 1):
            missing -= (needs[char] > 0)
            needs[char] -= 1

            if missing == 0:
                right = idx
                while left < right and needs[s[left]] < 0:
                    needs[s[left]] += 1
                    left += 1

                if end == 0 or right - left < end - start:
                    start, end = left, right

                needs[s[left]] += 1
                left += 1
                missing += 1

        return s[start:end]


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    solution = Solution()
    print(solution.minWindow(s, t))

