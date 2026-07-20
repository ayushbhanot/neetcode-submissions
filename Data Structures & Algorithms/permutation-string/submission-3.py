class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        countS1 = {}
        for c in s1:
            countS1[c] = countS1.get(c, 0) + 1
        sortedS1 = sorted(s1)
        
        for i in range(len(s2)):
            l = i - len(s1) + 1
            if 0 <= l < len(s2) and sorted(s2[l : i + 1]) == sortedS1:
                return True
            r = i + len(s1)
            if 0 <= r < len(s2) and sorted(s2[i : r + 1]) == sortedS1:
                return True
        return False
