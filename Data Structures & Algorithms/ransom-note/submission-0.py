class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countr = Counter(ransomNote)
        countm = Counter(magazine)
        for k in countr.keys():
            if countr[k] > countm[k]:
                return False
        return True