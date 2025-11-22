import math

class Solution:
    def canEat(self, piles, h, k):
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        return hours <= h

    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            if self.canEat(piles, h, mid):
                right = mid        # try smaller speed
            else:
                left = mid + 1     # speed too slow

        return left


if __name__ == "__main__":
    s = Solution()
    print(s.minEatingSpeed([3,6,7,11], 8))  # 4
