class Solution:
    def freqAlphabets(self, s: str) -> str:
        ret_str = ''

        length = len(s)
        i = 0
        while i < length:
            if i < length - 2 and s[i + 2] == '#':
                ret_str += chr(96 + int(s[i] + s[i + 1]))
                i += 3
            else:
                ret_str += chr(96 + int(s[i]))
                i += 1
        return ret_str


if __name__ == "__main__":
    s = "10#11#12"
    solution = Solution()
    print(solution.freqAlphabets(s))
