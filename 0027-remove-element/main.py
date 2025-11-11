class Solution:
    def removeElement(self, nums, val):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow

if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 2, 3]
    length = sol.removeElement(nums, 3)
    print("New length:", length)      # 2
    print("Array:", nums[:length])    # [2, 2]