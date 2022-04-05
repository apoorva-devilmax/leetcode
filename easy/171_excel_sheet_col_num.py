"""
https://leetcode.com/problems/excel-sheet-column-number/

Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701


Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
"""


class Solution:

    def __init__(self):
        self.ascii_diff = 64
    # def

    def getExcelNumber(self, columnName: str) -> int:
        return ord(columnName) - self.ascii_diff
    # def

    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        n = len(columnTitle)
        for index in range(n):
            # print(index, columnTitle[index])
            num += self.getExcelNumber(columnTitle[index]) * pow(26, n - 1 - index)
        # for
        return num
    # def

# class


solution = Solution()
print(solution.titleToNumber("A"))  # 1
print(solution.titleToNumber("AB"))  # 28
print(solution.titleToNumber("ZY"))  # 701
print(solution.titleToNumber("ABC"))  # 731
