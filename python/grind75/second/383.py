import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        item_dic = collections.defaultdict(int)

        # gen dic
        for ch in magazine:
            item_dic[ch] += 1

        # check ransomNote
        for ch in ransomNote:
            if item_dic[ch] <= 0:
                return False
            item_dic[ch] -= 1

        return True


if __name__ == "__main__":
    ransomNote: str = "ac"
    magazine: str = "badadad"
    solution = Solution()

    print(solution.canConstruct(ransomNote, magazine))
