class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        poz = {}
        count = Counter(nums)
        rez = set()
        curr = 0
        for x in nums:
            target = -x
            for index,i in enumerate(nums):
                aux = tuple(sorted([x,i,target-i]))
                if target - i in poz and aux not in rez :
                    count[x] -= 1
                    count[target - i] -= 1
                    count[i] -= 1
                    if count[x] >=0 and count[target - i] >= 0 and count[i] >= 0:
                        rez.add(aux)
                    count[x] += 1
                    count[target - i] += 1
                    count[i] += 1
                if i not in poz:
                    poz[i] = index
        return list(rez)