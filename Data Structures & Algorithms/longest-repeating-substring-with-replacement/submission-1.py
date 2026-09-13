class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        left = lmax = 0
        for r in s:
            d[r] += 1
            if sum(d.values()) - max(d.values()) > k:
                lmax = max(lmax,sum(d.values())-1)
                while sum(d.values()) - max(d.values()) > k :
                    d[s[left]] -= 1
                    if d[s[left]] == 0:
                        del d[s[left]]
                    left += 1
        lmax = max(lmax,sum(d.values()))  
        return lmax 