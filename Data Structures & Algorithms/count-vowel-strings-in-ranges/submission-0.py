class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        l = [0] * (len(words)+1)
        i = 1
        for w in words:
            if (w[0] == 'a' or w[0] == 'e' or w[0] == 'i' or w[0] == 'o' or w[0] == 'u') and (w[-1] == 'a' or w[-1] == 'e' or w[-1] == 'i' or w[-1] == 'o' or w[-1] == 'u'):
                l[i] += l[i-1]+1
            else:
                l[i] = l[i-1]
            i+=1
        rez = []
        for s,e in queries:
            rez.append(l[e+1]-l[s])
        return rez
