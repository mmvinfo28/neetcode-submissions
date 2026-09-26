class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        while left <= right:
            mid = (left + right) // 2
            summ = sum([math.ceil(x/mid) for x in piles])
            if summ <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left