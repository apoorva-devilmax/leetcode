"""
https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.



Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(int(n/2)):
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]
        # for
        return s
    # def
# class


solution = Solution()
print(solution.reverseString(["h", "e", "l", "l", "o"]))  # ["o", "l", "l", "e", "h"]
print(solution.reverseString(["H", "a", "n", "n", "a", "h"]))  # ["h", "a", "n", "n", "a", "H"]
