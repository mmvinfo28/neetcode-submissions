class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        let = set()
        lmax = 0
        left = 0
        for r in s:
            if r in let:
                lmax = max(len(let),lmax)
                while r in let:
                    let.remove(s[left])
                    left += 1
            let.add(r)
        lmax = max(len(let),lmax)
        return lmax