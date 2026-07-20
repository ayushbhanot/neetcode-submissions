class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count1 = [0] * 26
        for c in s1:
            count1[ord(c) - ord('a')] += 1

        l = 0
        for r in range(len(s1), len(s2) + 1): #O(n) time
            count2 = [0] * 26
            for c in s2[l : r]: #O(s1) time
                count2[ord(c) - ord('a')] += 1
            if count2 == count1:
                return True
            l += 1
        return False
