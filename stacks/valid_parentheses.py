"""
Problem: Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/

Clarification Questions:
1. Does the string contain only (), {}, [] ? -> Yes
2. Can the string be empty? -> Yes, return True
3. Are there any whitespace or other characters? -> No
4. Is the length always even for a valid string? -> Yes, but don't rely solely on that check

Approach:
1. Use a stack to store opening brackets
2. Use a hashmap to store closing → opening bracket mapping
3. Iterate over characters:
   - If it's an opening bracket, push to stack
   - If it's a closing bracket, pop from stack and check for a match
4. If stack is empty at the end, return True; otherwise False

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')': '(', '}': '{', ']': '['}
        stack = []

        for brac in s:
            if brac not in hashmap:
                # Opening bracket
                stack.append(brac)
            else:
                # Closing bracket
                top = stack.pop() if stack else '#'
                if top != hashmap[brac]:
                    return False

        return not stack


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))       # True
    print(sol.isValid("()[]{}"))   # True
    print(sol.isValid("(]"))       # False
    print(sol.isValid("([)]"))     # False
    print(sol.isValid("{[]}"))     # True

