class Solution:
    def isAnagram(self, s: str, t: str) -> bool: return __import__('collections').Counter(s) == __import__('collections').Counter(t)