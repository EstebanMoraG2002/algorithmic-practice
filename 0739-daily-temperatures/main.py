class Solution:
    def dailyTemperatures(self, t):
        ans = [0]*len(t)
        stack = []

        for i, temp in enumerate(t):
            while stack and temp > t[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)

        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
    # [1,1,4,2,1,1,0,0]