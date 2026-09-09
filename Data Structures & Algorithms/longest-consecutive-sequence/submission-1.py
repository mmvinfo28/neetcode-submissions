class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        lmax = 0
        for x in nums:
            if x-1 in s:
                continue
            else:
                l = 1
                i = 1
                while x+i in s:
                    l += 1
                    i += 1
                lmax = max(lmax,l)
        return lmax