from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left: List[int], right: List[int], val: str) -> List[int]:
            result = []
            for l in left:
                for r in right:
                    result.append(eval(str(l) + val + str(r)))
            return result

        if expression.isdigit():
            return [int(expression)]

        results = []
        for index, value in enumerate(expression):
            if value in '-+*':
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index + 1:])
                results.extend(compute(left, right, value))

        return results


if __name__ == "__main__":
    expression = "2*3-4*5"
    # expression = "2-1-1"
    solution = Solution()
    print(solution.diffWaysToCompute(expression))

