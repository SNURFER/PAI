import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0

        counter = collections.Counter()
        for right in range(1, len(s) + 1):
            counter[s[right - 1]] += 1
            most_common_cnt = counter.most_common()[0][1]

            if right - left - most_common_cnt > k:
                counter[s[left]] -= 1
                left += 1

        return right - left


if __name__ == "__main__":
    # s = "AABABBA"
    # k = 1
    s = "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
    k = 4
    solution = Solution()
    print(solution.characterReplacement(s, k))
