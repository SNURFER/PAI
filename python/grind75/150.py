from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculator(left: int, right: int, op: str) -> int:
            if op == '+':
                return left + right
            if op == '-':
                return left - right
            if op == '*':
                return left * right
            if op == '/':
                return int(left / right)


        num_stack = []
        for tkn in tokens:
            if tkn.replace('-','').isnumeric():
                num_stack.append(int(tkn))
            else:
                right: int = num_stack.pop()
                left: int = num_stack.pop()
                cal_val = calculator(left, right, tkn)
                num_stack.append(cal_val)
        return num_stack[-1]


if __name__ == "__main__":
    # tokens = ["2","1","+","3","*"]
    # tokens = ["4", "13", "5", "/", "+"]
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    solution = Solution()
    print(solution.evalRPN(tokens))
