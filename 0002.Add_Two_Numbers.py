"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = new_node = ListNode()
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            new_node.next = ListNode(val)
            new_node = new_node.next
        return root.next

    def practice(self, l1, l2):
        root = l3 = ListNode()
        carry = 0
        while l1 or l2 or carry:
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            val += carry
            if val > 9:
                carry, rem = 1, val - 10
            else:
                carry, rem = 0, val
            l3.next = ListNode(rem)
            l3 = l3.next
        return root


def print_linked_list(l):
    while l:
        print(l.val)
        l = l.next


s = Solution()
ans = s.addTwoNumbers(l1, l2)
ans = s.practice(l1, l2)
print_linked_list(ans)

l1 = ListNode(5)
l2 = ListNode(5)
ans = s.addTwoNumbers(l1, l2)
