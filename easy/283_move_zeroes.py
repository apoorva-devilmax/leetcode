"""
https://leetcode.com/problems/move-zeroes/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        shift = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                shift += 1
            else:
                nums[i - shift] = nums[i]
                if shift > 0:
                    nums[i] = 0
                # if
            # if/else
            # print("iteration ", i, shift, nums)
        # for
        return nums
    # def
# class


solution = Solution()
print(solution.moveZeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
print(solution.moveZeroes([0, 1]))  # [1, 0]
print(solution.moveZeroes([0]))  # [0]
