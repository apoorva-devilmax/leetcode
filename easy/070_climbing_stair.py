"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
"""


class Solution:
    def climb_stairs(self, n: int) -> int:
        series = []
        first_num = 1
        second_num = 1
        third_num = 0
        series.append(first_num)
        series.append(second_num)
        if n > 2:
            for index in range(2, n + 1):
                if index > 45:
                    break
                # end if
                third_num = first_num + second_num
                series.append(third_num)
                first_num, second_num = second_num, third_num
            # end for
        # end if
        return series[n]
    # def

# class


solution = Solution()
print(solution.climb_stairs(4))
print(solution.climb_stairs(8))
print(solution.climb_stairs(10))
