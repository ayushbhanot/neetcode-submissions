class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = []

        l = 0
        while l < len(temperatures):
            r = l
            while temperatures[r] <= temperatures[l]:
                r += 1
                if r == len(temperatures):
                    res.append(0)
                    break
            if r < len(temperatures) and temperatures[r] > temperatures[l]:
                res.append(r - l)
            l += 1

        return res