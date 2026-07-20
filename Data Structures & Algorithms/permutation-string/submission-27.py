class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        countS1 = {}
        for c in s1: #O(s1) time
            countS1[c] = countS1.get(c, 0) + 1 #O(26) space
        
        for i in range(len(s2)): #O(s2) time
            countS2 = {}
            for j in range(i, len(s2)): #O(s2^2) time
                if (j - i + 1) > len(s1):
                    break
                countS2[s2[j]] = countS2.get(s2[j], 0) + 1 #O(26) space
                if countS2 == countS1:
                    return True
        
        return False
