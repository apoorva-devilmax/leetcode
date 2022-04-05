"""
https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        char_data = {}
        for i in range(n):
            if s[i] in char_data:
                char_data[s[i]]['count'] += 1
            else:
                char_data[s[i]] = {
                    'index': i,
                    'count': 1,
                }
            # if/else
        # for
        #print(char_data)
        for item in char_data:
            if char_data[item]['count'] == 1:
                return char_data[item]['index']
            # if
        # for
        return -1
    # def
# class


solution = Solution()
print(solution.firstUniqChar("leetcode"))  # 0
print(solution.firstUniqChar("loveleetcode"))  # 2
print(solution.firstUniqChar("aabb"))  # -1
