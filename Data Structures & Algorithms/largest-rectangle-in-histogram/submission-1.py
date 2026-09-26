class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        s = [(heights[0],0)]
        maxarea = 0
        for r in range(1,len(heights)):
            minindex = r
            while s and heights[r] <= s[-1][0]:
                h, i = s[-1]
                maxarea = max(maxarea,(r - i) * h)
                minindex = min(minindex,i)
                s.pop()
            s.append((heights[r],minindex))
        return maxarea
            
