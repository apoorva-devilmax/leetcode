"""
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""
from typing import List


def max_subarray(nums: List[int]) -> int:
    cur = float('-inf')
    the_max = float('-inf')
    # print(cur, the_max)
    for i in nums:
        # print(f'cur: {cur}, el: {i}, maximum of element: {i} and addition: {i + cur} ', end=' ==> ')
        cur = max(i, i + cur)
        # print(f'maximum of cur: {cur} and the_max: {the_max} ', end=' ==> ')
        the_max = max(cur, the_max)
        # print(f'the_max: {the_max}')
    # for
    return the_max
# def


solution = max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(solution)
solution = max_subarray([1])
print(solution)
solution = max_subarray([5, 4, -1, 7, 8])
print(solution)
