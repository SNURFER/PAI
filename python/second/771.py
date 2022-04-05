import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_cnt = collections.Counter(stones)

        jew_sum = 0
        for jewel in jewels:
            jew_sum += stone_cnt[jewel]

        return jew_sum


if __name__ == "__main__":
    jewels = "aA"
    stones = "aAAbbbb"
    solution = Solution()
    print(solution.numJewelsInStones(jewels, stones))
