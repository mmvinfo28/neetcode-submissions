class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = [] #index
        out = [0] * len(temperatures)
        r = 0
        while r in range(len(temperatures)):
            while s and temperatures[s[-1]] < temperatures[r]:
                out[s[-1]] = r - s[-1]
                s.pop()
            s.append(r)
            r += 1
        while s:
            out[s[-1]] = 0
            s.pop()
        return out