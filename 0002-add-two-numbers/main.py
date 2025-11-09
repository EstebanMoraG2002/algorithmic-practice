# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry

            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# Helper functions for testing
def build_list(values):
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head


def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])
    result = sol.addTwoNumbers(l1, l2)
    print_list(result)  # [7, 0, 8]

    # Example 2
    l1 = build_list([0])
    l2 = build_list([0])
    result = sol.addTwoNumbers(l1, l2)
    print_list(result)  # [0]

    # Example 3
    l1 = build_list([9, 9, 9, 9, 9, 9, 9])
    l2 = build_list([9, 9, 9, 9])
    result = sol.addTwoNumbers(l1, l2)
    print_list(result)  # [8, 9, 9, 9, 0, 0, 0, 1]
