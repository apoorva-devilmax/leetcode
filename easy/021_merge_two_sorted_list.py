"""
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: List[int], list2: List[int]) -> List[int]:
    list3 = []
    i, j = 0, 0
    while i < len(list1) or j < len(list2):
        if i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                list3.append(list1[i])
                i += 1
            else:
                list3.append(list2[j])
                j += 1
            # if/else
        elif i < len(list1):
            list3.append(list1[i])
            i += 1
        elif j < len(list2):
            list3.append(list2[j])
            j += 1
        else:
            break
        # if/else
    # while
    return list3
# def


def merge_two_lists_using_node(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    cur = dummy = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1, cur = list1.next, list1
        else:
            cur.next = list2
            list2, cur = list2.next, list2
        # if/else
    # while
    if list1 or list2:
        cur.next = list1 if list1 else list2
    # if
    return dummy.next
# def


solution = merge_two_lists([1, 2, 4], [1, 3, 4])
print(solution)
solution = merge_two_lists([], [])
print(solution)
solution = merge_two_lists([], [0])
print(solution)
