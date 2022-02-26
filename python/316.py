import collections


class Solution(object):
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        counter = collections.Counter(s)

        for ch in s:
            counter[ch] -= 1
            if ch in stack:
                continue

            while stack and ch < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()

            stack.append(ch)

        return ''.join(stack)



if __name__ == '__main__':
    solution = Solution()
    # input_str = 'cbacdcbc'
    input_str = 'abacb'
    print(solution.removeDuplicateLetters(input_str))
