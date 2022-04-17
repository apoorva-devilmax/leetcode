"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # def

    def __repr__(self):
        return f'{self.val}, {self.next}'
# class


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_list = []
        n, m = len(l1), len(l2)
        i, j, add = 0, 0, 0
        while i < n or j < m:
            add += (l1[i] if i < n else 0) + (l2[j] if j < m else 0)
            if add > 9:
                mod_val = add % 10
                add = int((add - mod_val)/10)
                sum_list.append(mod_val)
            else:
                sum_list.append(add)
                add = 0
            # if/else
            i += 1
            j += 1
        # while
        if add > 0:
            sum_list.append(add)
        # if
        return sum_list
    # def

    def addTwoNumbersUsingLinkedList(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_list = ListNode()
        tmp = sum_list
        add = 0
        while l1 or l2:
            add += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            if add > 9:
                mod_val = add % 10
                add = int((add - mod_val) / 10)
                tmp.next = ListNode(mod_val)
            else:
                tmp.next = ListNode(add)
                add = 0
            # if/else
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            tmp = tmp.next
        # while
        if add > 0:
            tmp.next = ListNode(add)
            # tmp = tmp.next
        # if
        return sum_list.next
# class


solution = Solution()
print(solution.addTwoNumbers([2, 4, 3], [5, 6, 4]))  # [7, 0, 8]
print(solution.addTwoNumbers([0], [0]))  # [0]
print(solution.addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))  # [8, 9, 9, 9, 0, 0, 0, 1]

"""x = [7, 0, 8]
first = True
dummy = ListNode(-1)
test = dummy
for item in x:
    if 0 and first:
        # test = ListNode(item)
        pass
    else:
        # test = test.next
        test.next = ListNode(item)
        # print(test)
        # test.next = test
        test = test.next
    print(test)
    first = False
# for
print(dummy.next)"""
