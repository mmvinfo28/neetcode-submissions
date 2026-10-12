class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        cnt =0 
        for i in range(n):
            s1 = words[i]
            ls1 = len(s1)
            for j in range(i+1,n):
                s2 = words[j]
                ls2 = len(s2)
                if s1<=s2 and s1 == s2[:ls1] and s1 == s2[ls2-ls1:]:
                    cnt += 1
        return cnt