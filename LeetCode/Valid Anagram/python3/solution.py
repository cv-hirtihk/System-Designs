class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = [0] * 26

        for char in s:
            counter[ord(char) - ord('a')] += 1

        for char in t:
            if counter[ord(char) - ord('a')] == 0:
                return False
            counter[ord(char) - ord('a')] -= 1
        return True

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false
