"""
https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        min_limit = - pow(2, 31)
        max_limit = pow(2, 31) - 1
        reverse_digit = sign * int(str(abs(x))[::-1])
        if reverse_digit < min_limit or reverse_digit > max_limit:
            return 0
        return reverse_digit
    # def
# class


solution = Solution()
print(solution.reverse(123))  # 321
print(solution.reverse(-123))  # -321
print(solution.reverse(120))  # 21
print(solution.reverse(1534236469))  # 0
