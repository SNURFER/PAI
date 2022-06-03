import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_dict = collections.Counter(stones)

        ret_val = 0
        for jewel in list(jewels):
            ret_val += stone_dict[jewel]

        return ret_val


if __name__ == "__main__":
    jewels = "aA"
    stones = "aAAbbbb"

    solution = Solution()
    print(solution.numJewelsInStones(jewels, stones))
