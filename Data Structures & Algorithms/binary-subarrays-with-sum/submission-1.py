class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        curr = 0
        n = len(nums)
        d = defaultdict(int)
        cnt = 0
        d[0] = 1
        for i in range(n):
            curr += nums[i]
            print(curr)
            cnt += d[curr-goal]
            d[curr] += 1
        print(d)
        return cnt