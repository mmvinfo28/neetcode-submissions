class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        c = [(heights[i],names[i]) for i in range(len(names))]
        c = sorted(c, reverse = True)
        return [i[1] for i in c]