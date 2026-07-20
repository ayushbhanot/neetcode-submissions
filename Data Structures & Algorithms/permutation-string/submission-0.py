class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        countS1 = {}
        for c in s1:
            countS1[c] = countS1.get(c, 0) + 1
            
        l = 0

        for i in range(len(s2)): #O(n) time
            countS2 = {}
            for j in range(i, len(s2)): #O(n2) time
                countS2[s2[j]] = countS2.get(s2[j], 0) + 1
                if countS2 == countS1:
                    return True

        return False


