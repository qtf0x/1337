"""
@author  Aster Marias <aster@bitangent.org>
@date    09/16/2025

@brief   You are given two non-empty linked lists representing two
         non-negative integers. The digits are stored in reverse order, and
         each of their nodes contains a single digit. Add the two numbers and
         return the sum as a linked list. You may assume the two numbers do
         not contain any leading zero, except the number 0 itself.
@details <https://leetcode.com/problems/add-two-numbers/description/>
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        digit1 = 0
        digit2 = 0
        soln_digit = 0
        carry = 0

        sum = ListNode()
        sum_it = sum

        while l1 or l2 or carry:
            digit1 = 0
            digit2 = 0

            if l1:
                digit1 = l1.val
                l1 = l1.next
            if l2:
                digit2 = l2.val
                l2 = l2.next

            soln_digit = digit1 + digit2 + carry
            carry = soln_digit > 9

            sum_it.next = ListNode(soln_digit % 10)
            sum_it = sum_it.next

        return sum.next
