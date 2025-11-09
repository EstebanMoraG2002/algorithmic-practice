class Solution:
    def containsDuplicate(self, nums):
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                return True
            
        return False
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 1]))  # True
    print(sol.containsDuplicate([1, 2, 3, 4]))  # False
    print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True