"""
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""
import re


class Solution:
    def longestPalindrome(self, s: str, length: int = None) -> str:
        length = length if length else len(s)
        start_from = 0
        end_to = start_from + length
        found = False
        result = ''
        while end_to <= len(s):
            sub_str = s[start_from:end_to]
            if self.isPalindrome(sub_str):
                found = True
                result = sub_str
                break
            # if
            start_from += 1
            end_to += 1
        # while
        if found:
            return result
        # if
        return self.longestPalindrome(s, length - 1)
    # def

    def isPalindrome(self, s: str) -> bool:
        clean_s = re.sub('[^A-Za-z0-9]+', '', s)
        if clean_s:
            clean_s_lower = clean_s.lower()
            return clean_s_lower == clean_s_lower[::-1]
        # if
        return True
    # def

    def longestPalindromeV2(self, s: str) -> str:
        res = ''
        res_len = 0
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                print("odd: ", l, r, s[l], s[r])
                if (r - l + 1) > res_len:
                    res = s[l:r+1]
                    print("res assigned odd: ", res)
                    res_len = r - l + 1
                # if
                l -= 1
                r += 1
            # while
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                print("even: ", l, r, s[l], s[r])
                if (r - l + 1) > res_len:
                    res = s[l:r + 1]
                    print("res assigned even: ", res)
                    res_len = r - l + 1
                # if
                l -= 1
                r += 1
            # while
        return res
    # def
# class


solution = Solution()
print(solution.longestPalindrome("babad"))  # bab, aba
print(solution.longestPalindrome("cbbd"))  # bb
print("===========================")
print(solution.longestPalindromeV2("babad"))  # bab, aba
print(solution.longestPalindromeV2("cbbd"))  # bb
