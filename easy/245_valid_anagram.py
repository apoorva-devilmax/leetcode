"""
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [x for x in s]
        s_list.sort()
        t_list = [x for x in t]
        t_list.sort()
        return s_list == t_list
    # def
# class


solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # true
print(solution.isAnagram("rat", "car"))  # false
