class Solution:
    def findMaxAverage(self, nums, k):
        if not nums:
            return 0.0

        left = 0
        total = 0.0
        max_avg = float("-inf")

        for right in range(len(nums)):
            total += nums[right]

            if right - left + 1 == k:
                max_avg = max(max_avg, total / k)
                total -= nums[left]
                left += 1

        return max_avg


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # 12.75
    print(sol.findMaxAverage([5], 1))                     # 5.0
    print(sol.findMaxAverage([0, 1, 1, 3, 3], 4))         # 2.0
    print(sol.findMaxAverage([-1, -2, -3, -4], 2))        # -1.5
