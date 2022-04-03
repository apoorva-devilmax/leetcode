"""
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
from typing import List


def longest_common_prefix_v2(strs: List[str]) -> str:
    prefix = []
    for x in zip(*strs):
        if len(set(x)) == 1:
            prefix.append(x[0])
        else:
            break
        # if/else
    return "".join(prefix)
# def


def longest_common_prefix(strs: List[str], prefix_count: int = 1) -> str:
    if prefix_count <= len(strs[0]):
        prefix = strs[0][:prefix_count]
        found = True
        for i in range(len(strs)):
            # if prefix not in strs[i]:
            if not strs[i].startswith(prefix):
                found = False
                break
            # if
        # for
        if found:
            if (prefix_count + 1) <= len(strs[0]):
                return longest_common_prefix(strs, prefix_count + 1)
            else:
                return prefix
            # if/else
        else:
            return strs[0][:prefix_count-1]
        # if/else
    else:
        return strs[0]
    # if/else
# def


solution = longest_common_prefix(["flower", "flow", "flight"])
print(solution)
solution = longest_common_prefix(["dog", "racecar", "car"])
print(solution)
solution = longest_common_prefix(["a"])
print(solution)
solution = longest_common_prefix(["flower", "flower", "flower", "flower"])
print(solution)
solution = longest_common_prefix(["c", "acc", "ccc"])
print(solution)
print("===================================")
solution = longest_common_prefix_v2(["flower", "flow", "flight"])
print(solution)
solution = longest_common_prefix_v2(["dog", "racecar", "car"])
print(solution)
solution = longest_common_prefix_v2(["a"])
print(solution)
solution = longest_common_prefix_v2(["flower", "flower", "flower", "flower"])
print(solution)
solution = longest_common_prefix_v2(["c", "acc", "ccc"])
print(solution)
