class Solution:
    def minSubArrayLen(self, target, nums):
        if not nums:
            return 0

        left = 0
        total = 0
        result = float("inf")

        for right in range(len(nums)):
            total += nums[right]

            # shrink window while the sum condition is satisfied
            while total >= target:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if result == float("inf") else result


if __name__ == "__main__":
    sol = Solution()
    print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # Expected: 2 ([4,3])
    print(sol.minSubArrayLen(11, [1, 2, 3, 4, 5]))     # Expected: 3 ([3,4,5])
    print(sol.minSubArrayLen(4, [1, 4, 4]))            # Expected: 1 ([4])
    print(sol.minSubArrayLen(15, [1, 2, 3, 4, 5]))     # Expected: 5 ([1,2,3,4,5])
