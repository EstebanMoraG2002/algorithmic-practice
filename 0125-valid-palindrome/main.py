class Solution:
    def isPalindrome(self, s: str) -> bool:
        dummy = ""
        for c in s:
            if c.isalnum():
                dummy += c.lower()

        left, right = 0, len(dummy) - 1
        while left < right:
            if dummy[left] != dummy[right]:
                return False
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(sol.isPalindrome("race a car"))                      # False
    print(sol.isPalindrome("No lemon, no melon!"))             # True
