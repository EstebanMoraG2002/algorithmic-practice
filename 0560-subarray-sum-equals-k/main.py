from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num
            need = prefix_sum - k

            if need in prefix_count:
                result += prefix_count[need]

            prefix_count[prefix_sum]+=1
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1, 1, 1], 2))   # 2
    print(sol.subarraySum([1, 2, 3], 3))   # 2
    print(sol.subarraySum([1, 2, 1, 2, 1], 3))  # 4