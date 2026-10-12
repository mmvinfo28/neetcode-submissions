class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        l = [0] * (len(words)+1)
        i = 1
        s = set("aeiou")
        for w in words:
            if w[0] in s and w[-1] in s:
                l[i] += l[i-1]+1
            else:
                l[i] = l[i-1]
            i+=1
        rez = []
        for s,e in queries:
            rez.append(l[e+1]-l[s])
        return rez
