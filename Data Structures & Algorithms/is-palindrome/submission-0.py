class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for i in s:
            if 'a' <= i <= 'z' or '0' <= i <= '9':
                res.append(i)
            if 'A' <= i <= 'Z':
                res.append(chr(ord(i)+32))
        return res == list(reversed(res))
            