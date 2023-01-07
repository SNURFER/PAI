import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ch_counter = collections.defaultdict(int)


        # https://www.geeksforgeeks.org/operations-on-python-counter/
        str1 = collections.Counter(ransomNote)
        str2 = collections.Counter(magazine)
        print(str1 & str2 == str1)

        for ch in magazine:
            ch_counter[ch] += 1

        for ch in ransomNote:
            ch_counter[ch] -= 1
            if ch_counter[ch] < 0:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    ransomNote = "aabs"
    magazine = "sdvsaabs"
    print(solution.canConstruct(ransomNote, magazine))
