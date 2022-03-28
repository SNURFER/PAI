import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needs = collections.Counter(t)
        remain_length = len(t)

        left = start = end = 0

        for right, ch in enumerate(s, 1):
            if needs[ch] > 0:
                remain_length -= 1
            needs[ch] -= 1

            # all t string is included
            # in range left ~ right
            if remain_length == 0:
                while left < right and needs[s[left]] < 0:
                    needs[s[left]] += 1
                    left += 1

                if (end == 0) or right - left < end - start:
                    end, start = right, left

                # update left + 1 to search next shortest
                needs[s[left]] += 1
                left += 1
                remain_length += 1

        return s[start:end]


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    # s = "A"
    # t = "A"
    solution = Solution()
    print(solution.minWindow(s, t))
