class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        poz = {}
        curr = 0
        for index,i in enumerate(nums):
            if target - i in poz:
                return [poz[target-i],index]
            if i not in poz:
                poz[i] = index
        return []