class Solution:
    def isPalindrome(self, s: str) -> bool: return (lambda t: t == t[::-1])([c.lower() for c in s if c.isalnum()])