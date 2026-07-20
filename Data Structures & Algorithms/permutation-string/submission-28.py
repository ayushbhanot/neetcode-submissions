class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False
        
        count1, count2 = [0] * 26, [0] * 26
        for c in s1: #O(s1) time
            count1[ord(c) - ord('a')] += 1
        
        l = 0
        for r in range(len(s2)): #O(s2) time
            count2[ord(s2[r]) - ord('a')] += 1
            if (r - l + 1) == len(s1):
                if count2 == count1:
                    return True
                count2[ord(s2[l]) - ord('a')] -= 1
                l += 1
        return False 
