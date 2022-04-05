"""
https://leetcode.com/problems/power-of-three/

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.



Example 1:

Input: n = 27
Output: true
Example 2:

Input: n = 0
Output: false
Example 3:

Input: n = 9
Output: true


Constraints:

-231 <= n <= 231 - 1


Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        # if
        result = False
        # print(type(n) is int)
        while n != 0 and n != 1 and (type(n) is int or n.is_integer()):
            n = n/3
            # print(n.is_integer())
            if n == 1:
                result = True
            # if
        # while
        return result
    # def

    def isPowerOfThreeRec(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            return n % 3 == 0 and self.isPowerOfThreeRec(n/3)
        # if/else
    # def

    def isPowerOfThreeNoLoop(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            # 3 max power (31) within range is 1162261467
            return 1162261467 % n == 0
        # if/else
    # def
# class


solution = Solution()
print(solution.isPowerOfThree(27))  # true
print(solution.isPowerOfThree(0))  # false
print(solution.isPowerOfThree(9))  # true
print(solution.isPowerOfThree(15))  # false
print(solution.isPowerOfThree(1))  # true
print("================================")
print(solution.isPowerOfThreeRec(27))  # true
print(solution.isPowerOfThreeRec(0))  # false
print(solution.isPowerOfThreeRec(9))  # true
print(solution.isPowerOfThreeRec(15))  # false
print(solution.isPowerOfThreeRec(1))  # true
print("================================")
print(solution.isPowerOfThreeNoLoop(27))  # true
print(solution.isPowerOfThreeNoLoop(0))  # false
print(solution.isPowerOfThreeNoLoop(9))  # true
print(solution.isPowerOfThreeNoLoop(15))  # false
print(solution.isPowerOfThreeNoLoop(1))  # true
