class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        rez = ""
        maxl = 0
        for i in range(n):
            l = i - 1
            r = i + 1
            length = 1
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    length += 2
                else:
                    break
                l -= 1
                r += 1
            if length > maxl:
                maxl = length
                rez = s[l+1:r]
            if  i < n - 1 and s[i] == s[i+1]:
                length = 2
                l = i - 1
                r = i + 2
                while l >= 0 and r < n:
                    if s[l] == s[r]:
                        length += 2
                    else:
                        break
                    l -= 1
                    r += 1
                if length > maxl:
                    maxl = length
                    rez = s[l+1:r]
                    
        return rez
                    