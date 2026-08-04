class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 0, max(piles) + 1
        minRate = float('inf')
        while l < r:
            m = l + (r - l) // 2

            if not (self.isValid(m, h, piles)):
                l = m + 1
            elif self.isValid(m, h, piles):
                minRate = min(minRate, m)
                r = m

        return minRate

    def isValid(self, speed: int, h: int, piles: List[int]) -> bool:

        if speed == 0:
            return False
        
        hours = 0
        for i in range(len(piles)):
            if (piles[i] / speed) > piles[i] // speed:
                hours += piles[i] // speed + 1
            else:
                hours += piles[i] // speed

        if hours <= h:
            return True
        else:
            return False