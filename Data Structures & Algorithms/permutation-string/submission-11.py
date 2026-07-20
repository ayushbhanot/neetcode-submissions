class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        countS1 = {}

        for c in s1: #O(s1) time
            countS1[c] = countS1.get(c, 0) + 1 #O(s1) space

        for i in range(len(s2)): #O(s2) time
            countS2 = {}
            for j in range(i, len(s2)): #O(s2^2) time
                countS2[s2[j]] = countS2.get(s2[j], 0) + 1 #O(s2) space
                if countS1.get(s2[j], 0) < countS2[s2[j]]:
                    break
                if countS2 == countS1:
                    return True

        return False
