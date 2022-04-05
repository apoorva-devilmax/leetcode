"""
https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false


Constraints:

1 <= n <= 231 - 1
"""


class Solution:
    def __init__(self):
        self.sum_dict = {}
    # def

    def clean_dict(self):
        self.sum_dict = {}
    # def

    def isHappy(self, n: int) -> bool:
        if n == 1:
            self.clean_dict()
            return True
        # if
        sum_square = 0
        for digit in str(n):
            sum_square += int(digit) ** 2
        # for
        # print(sum_square)
        if sum_square in self.sum_dict:
            self.clean_dict()
            return False
        else:
            self.sum_dict[sum_square] = sum_square
            # print("========= ", sum_square, sum_dict)
            return self.isHappy(sum_square)
        # if/else
    # def
# class


solution = Solution()
print(solution.isHappy(19))  # true
print(solution.isHappy(2))  # false
print(solution.isHappy(13))  # true
