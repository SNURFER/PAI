import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freqs = collections.Counter(nums)
        # freqs_heap = []
        # for f in freqs:
        #     heapq.heappush(freqs_heap, (-freqs[f], f))
        #
        # topk = list()
        # for _ in range(k):
        #     topk.append(heapq.heappop(freqs_heap)[1])
        #
        # return topk
        counter = collections.Counter(nums)

        output_list = []
        temp_list = []

        for num in counter:
            temp_list.append((num, counter[num]))

        temp_list.sort(key=lambda x: -x[1])

        for i in range(k):
            output_list.append(temp_list[i][0])

        return output_list


if __name__ == "__main__":
    solution = Solution()
    # input_nums = [1, 1, 1, 2, 2, 3]
    # k = 2
    input_nums = [1, 2, 2, 3, 4, 4, 4]
    k = 2

    print(solution.topKFrequent(input_nums, k))
