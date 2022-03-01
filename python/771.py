import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = collections.Counter(stones)

        sum = 0
        for ch in jewels:
            if counter[ch] is not None:
                sum += counter[ch]

        return sum

if __name__ == "__main__":
    solution = Solution()
    J = "aA"
    S = "aAAbbbb"

    print(solution.numJewelsInStones(J, S))
