class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles) + 1

        while l < r:
            m = l + (r - l) // 2

            if self.isValid(m, h, piles):
                r = m
            else:
                l = m + 1 #Binary Search approach O(log(max piles) * length of piles) time and O(1) space

        return r


    def isValid(self, speed, h, piles: List[int]) -> bool:

        hours = 0

        if speed == 0:
            return False

        for i in range(len(piles)): #O(n) time
            if piles[i] / speed > piles[i] // speed:
                hours += piles[i] // speed + 1
                continue
            hours += piles[i] // speed
        
        if hours <= h:
            return True
        else:
            return False