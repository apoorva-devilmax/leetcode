"""
https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.



Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.


Constraints:

0 <= x <= 231 - 1
"""


class Solution:
    def my_sqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x <= 3:
            return 1
        else:
            r = 2
            for v in range(2, int(x/2)):
                if self.is_square(v, x) is True:
                    r = v
                else:
                    break
                # if/else
            # for
            return r
        # if/else
    # def

    def is_square(self, num, target):
        return (num * num) <= target
    # def
# class


solution = Solution()
print(solution.my_sqrt(4))
print(solution.my_sqrt(8))
