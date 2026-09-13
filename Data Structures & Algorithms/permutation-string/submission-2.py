class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        left = 0
        for s in s1:
            d1[s] += 1
        for s in s2:
            if d1 == d2:
                return True
            d2[s] += 1
            while d2[s] > d1[s]:
                d2[s2[left]] -= 1
                if d2[s2[left]] == 0:
                    del d2[s2[left]]
                left += 1
        return d1 == d2
