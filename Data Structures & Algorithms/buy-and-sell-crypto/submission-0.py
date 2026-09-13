class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        maxp = 0
        while r < len(prices):
            profit  = prices[r] - prices[l]
            if profit >= 0:
                maxp = max(maxp,profit)
            else:
                l = r
            r += 1
        return maxp
                