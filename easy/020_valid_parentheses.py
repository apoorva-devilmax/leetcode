"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


def is_valid(s: str) -> bool:
    valid = False
    valid_pair = ['()', '{}', '[]']
    # print('s1: ', s)
    if s == '':
        return True
    else:
        for pair in valid_pair:
            # print(pair)
            if pair in s:
                valid = True
                s = s.replace(pair, '')
            # if
        # for
        # print('s2: ', s)
        return valid and is_valid(s)
    # if/else
# def


def is_valid_using_stack(s: str) -> bool:
    stack, hm = [], {'(': ')', '{': '}', '[': ']'}
    for ch in s:
        # open bracket
        if ch in hm:
            stack.append(ch)
        # close bracket
        else:
            if not stack or hm[stack[-1]] != ch:
                # stack is empty OR last element in stack (open bracket) is not matched
                # with its closing bracket
                return False
            # if
            # remove last element
            stack.pop()
        # if/else
    # for
    # return true if stack is empty
    return not stack
# def


solution = is_valid("()")
print(solution)
solution = is_valid("()[]{}")
print(solution)
solution = is_valid("(]")
print(solution)
solution = is_valid("{[]}")
print(solution)
solution = is_valid("([)]")
print(solution)
print("===============================")
solution = is_valid_using_stack("()")
print(solution)
solution = is_valid_using_stack("()[]{}")
print(solution)
solution = is_valid_using_stack("(]")
print(solution)
solution = is_valid_using_stack("{[]}")
print(solution)
solution = is_valid_using_stack("([)]")
print(solution)
