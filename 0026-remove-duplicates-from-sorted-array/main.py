class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        slow = 0
        fast = 0

        while fast < len(nums) -1:
            if nums[slow] != nums[fast + 1]:
                slow += 1
                nums[slow] = nums[fast + 1]
            fast += 1

        return slow + 1

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 2, 2, 3]
    length = sol.removeDuplicates(nums)
    print("New length:", length)
    print("Array:", nums[:length])