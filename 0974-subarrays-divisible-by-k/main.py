from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums, k):
        remainder_count = defaultdict(int)
        remainder_count[0] = 1  # base case: one way to have sum % k == 0

        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            # handle negative remainders (Python handles negatives differently than C++)
            if remainder < 0:
                remainder += k

            # if we've seen this remainder before, add its frequency
            if remainder in remainder_count:
                result += remainder_count[remainder]

            # record the current remainder
            remainder_count[remainder] += 1

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))  # Expected: 7
    print(sol.subarraysDivByK([5], 9))                   # Expected: 0
    print(sol.subarraysDivByK([7, 4, -10], 5))           # Expected: 1
