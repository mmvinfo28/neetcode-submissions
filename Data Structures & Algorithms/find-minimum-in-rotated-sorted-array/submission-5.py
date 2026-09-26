class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)
        k = 0 
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            print(left)
            print(right)
            if nums[-mid] > nums[-(mid%len(nums))-1]:
                if nums[-mid] <= nums[-1]:
                    left = mid + 1
                elif nums[-mid] > nums[-1]:
                    right = mid - 1
                elif nums[-mid ] <= nums[0]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                return nums[-mid]