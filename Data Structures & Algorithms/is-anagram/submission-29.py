class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = [0] * 26

        if len(s) != len(t):
            return False
        
        for c in s:
            count[ord(c) - ord('a')] += 1

        for c in t:
            count[ord(c) - ord('a')] -= 1
            if count[ord(c) - ord('a')] < 0:
                return False

        for i in range(len(count)): #O(26) time => O(1) time
            if count[i] != 0:
                return False

        return True
        
        