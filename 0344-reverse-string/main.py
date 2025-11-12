class Solution:
    def reverseString(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

if __name__ == "__main__":
    sol = Solution()
    s = ["h", "e", "l", "l", "o"]
    print("Original:", s)
    sol.reverseString(s)
    print("Reversed:", s)  # ['o', 'l', 'l', 'e', 'h']

    s2 = ["E", "s", "t", "e", "b", "a", "n"]
    sol.reverseString(s2)
    print("Reversed:", s2)  # ['n', 'a', 'b', 'e', 't', 's', 'E']