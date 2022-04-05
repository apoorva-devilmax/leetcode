"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 is None or nums2 is None or len(nums1) == 0 or len(nums2) == 0:
            return []
        # if
        nums1Element = {}
        for num in nums1:
            if num in nums1Element:
                nums1Element[num] += 1
            else:
                nums1Element[num] = 1
            # if/else
        # for
        intersection = []
        for num in nums2:
            if num in nums1Element and nums1Element[num] >= 1:
                nums1Element[num] -= 1
                intersection.append(num)
            # if
        # for
        return intersection
    # def
# class


solution = Solution()
print(solution.intersect([1, 2, 2, 1], [2, 2]))  # [2, 2]
print(solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # [4, 9]
