"""
https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        for index in range(1, numRows):
            index_set = []
            # print(pascal)
            for item in range(index+1):
                i = index - 1
                j = item - 1
                # print(item, i, j, pascal[i], 0 <= item < len(pascal[i]), end=' === ')
                num = (pascal[i][j] if 0 <= j < len(pascal[i]) else 0)
                num += (pascal[i][item] if 0 <= item < len(pascal[i]) else 0)
                # num = (pascal[i][item] if item in pascal[i] else 0)
                # print(num, pascal[i][item])
                index_set.append(num)
                # print("=================")
            # inner for
            pascal.append(index_set)
            # print('===== ', pascal)
        # outer for
        return pascal
    # def
# class


solution = Solution()
print(solution.generate(5))
print(solution.generate(1))
