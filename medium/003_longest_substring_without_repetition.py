"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str, length: int = None) -> int:
        length = length if length else len(s)
        start_from = 0
        end_to = start_from + length
        found = False
        while end_to <= len(s):
            sub_str = s[start_from:end_to]
            if self.isUnique(sub_str):
                found = True
                break
            # if
            start_from += 1
            end_to += 1
        # while
        if found:
            return length
        # if
        return self.lengthOfLongestSubstring(s, length - 1)
    # def

    def isUnique(self, s:str) -> bool:
        s_list = [x for x in s]
        if len(s_list) == len(set(s_list)):
            return True
        # if
        return False
    # def

    def lengthOfLongestSubstringV2(self, s: str) -> int:
        ans = 0
        i = -1
        j = -1
        char_map = {}
        while True:
            f1 = False
            f2 = False
            # acquire
            while i < (len(s) - 1):
                f1 = True
                i += 1
                if s[i] in char_map:
                    char_map[s[i]] += 1
                else:
                    char_map[s[i]] = 1
                # if/else
                if char_map[s[i]] == 2:
                    break
                else:
                    length = i - j
                    if length > ans:
                        ans = length
                    # if
                # if/else
            # while
            # release
            while j < i:
                f2 = True
                j += 1
                if s[j] in char_map:
                    char_map[s[j]] -= 1
                # else:
                #    char_map[s[j]] = 1
                # if/else
                if char_map[s[j]] == 1:
                    break
                # if
            # while
            if not f1 and not f2:
                break
            # if
        # while
        return ans
    # def
# class


solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  # 3
print(solution.lengthOfLongestSubstring("bbbbb"))  # 1
print(solution.lengthOfLongestSubstring("pwwkew"))  # 3
print("===========================")
print(solution.lengthOfLongestSubstringV2("abcabcbb"))  # 3
print(solution.lengthOfLongestSubstringV2("bbbbb"))  # 1
print(solution.lengthOfLongestSubstringV2("pwwkew"))  # 3
# 8 - abcabcbb
# 7 - abcabcb, bcabcbb
# 6 - abcabc, bcabcb, cabcbb
# 5 - abcab, bcabc, cabcb, abcbb

