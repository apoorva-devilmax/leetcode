"""
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List


class Solution:
    def containsDuplicateV0(self, nums: List[int]) -> bool:
        dup_list = {}
        for item in nums:
            if item in dup_list:
                return True
            else:
                dup_list[item] = item
            # if/else
        # for
        return False
    # def

    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        return len(num_set) != len(nums)
    # def
# class


solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))  # true
print(solution.containsDuplicate([1, 2, 3, 4]))  # false
print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # true
