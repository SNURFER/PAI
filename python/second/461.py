class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        result_bin = bin(xor)[2:]

        ret_val = 0
        for num in result_bin:
            if num == '1':
                ret_val += 1

        print(ret_val)
        return ret_val



if __name__ == "__main__":
    x = 1
    y = 4
    solution = Solution()
    solution.hammingDistance(x, y)
