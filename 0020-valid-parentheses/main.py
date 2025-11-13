class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = "([{"
        close_brackets = ")]}"
        stack = []

        for c in s:

            # If character is an opening bracket
            if c in open_brackets:
                stack.append(c)
                continue

            # If character is a closing bracket
            if c in close_brackets:
                pos = close_brackets.index(c)  # corresponding opening index

                if not stack:        # nothing to match
                    return False

                if stack[-1] != open_brackets[pos]:  # mismatch
                    return False

                stack.pop()
                continue

            # invalid character (optional)
            return False

        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))          # True
    print(sol.isValid("()[]{}"))      # True
    print(sol.isValid("(]"))          # False
    print(sol.isValid("([)]"))        # False
    print(sol.isValid("{[]}"))        # True
    print(sol.isValid("]"))           # False
    print(sol.isValid("("))           # False
