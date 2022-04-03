"""
https://leetcode.com/problems/majority-element/

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = int(len(nums) / 2)
        major_el = {}
        for item in nums:
            if item in major_el:
                major_el[item] += 1
            else:
                major_el[item] = 1
            # if/else
            if major_el[item] > n:
                return item
            # if
        # for
        return 0
    # def

    def majorityElementV2(self, nums: List[int]) -> int:
        """
        Boyer–Moore majority vote algorithm.
        :param nums:
        :return:
        """
        el = 0
        cnt = 0
        for item in nums:
            if cnt == 0:
                el = item
            # if
            if el == item:
                cnt += 1
            else:
                cnt -= 1
            # if/else
        # for
        return el
    # def

# class


solution = Solution()
print(solution.majorityElement([3, 2, 3]))
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print("==================")
print(solution.majorityElementV2([3, 2, 3]))
print(solution.majorityElementV2([2, 2, 1, 1, 1, 2, 2]))
