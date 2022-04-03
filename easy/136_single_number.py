"""
https://leetcode.com/problems/single-number/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1


Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        storage = {}
        for item in nums:
            if item in storage:
                del storage[item]
            else:
                storage[item] = item
            # if/else
        # for
        return list(storage.keys())[0]
    # def
# class


solution = Solution()
print(solution.singleNumber([2, 2, 1]))
print(solution.singleNumber([4, 1, 2, 1, 2]))
print(solution.singleNumber([1]))
