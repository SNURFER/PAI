class Solution:
    def findComplement(self, num: int) -> int:
        num_bin = bin(num)[2:]
        complement_list = []
        for ch in num_bin:
            if ch == '0':
                complement_list.append('1')
            else:
                complement_list.append('0')

        complement_str = ''.join(complement_list)
        complement_num = int(complement_str, 2)

        return complement_num


if __name__ == "__main__":
    solution = Solution()
    solution.findComplement(5)
