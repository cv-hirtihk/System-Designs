class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""
        for ch in s:
            if 65 <= ord(ch) <= 90:
                result += chr(ord(ch) + 32)
            else:
                result += ch
        return result

# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

# Example 1:
# Input: s = "Hello"
# Output: "hello"

# Example 2:
# Input: s = "here"
# Output: "here"

# Example 3:
# Input: s = "LOVELY"
# Output: "lovely"
