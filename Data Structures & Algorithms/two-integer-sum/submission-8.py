class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: return next([i, j] for i, x in enumerate(nums) for j, y in enumerate(nums) if i < j and x + y == target)