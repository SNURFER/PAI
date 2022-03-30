from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = remain_fuel = 0
        for idx in range(len(gas)):
            if gas[idx] + remain_fuel < cost[idx]:
                start = idx + 1
                remain_fuel = 0
            else:
                remain_fuel += gas[idx] - cost[idx]

        return start


if __name__ == "__main__":
    # gas = [1, 2, 3, 4, 5]
    # cost = [3, 4, 5, 1, 2]
    gas = [5, 1, 2, 3, 4]
    cost = [4, 4, 1, 5, 1]

    solution = Solution()
    print(solution.canCompleteCircuit(gas, cost))