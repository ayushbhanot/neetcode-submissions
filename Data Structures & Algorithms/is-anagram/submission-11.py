class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #racecar                carrace

        if len(s) != len(t):
            return False

        Map = [0] * 26 #Create table for all 26 characters O(1) space still

        for i in range(len(s)): #O(n) time
            Map[ord(s[i]) - ord('a')] += 1
            Map[ord(t[i]) - ord('a')] -= 1

        for num in Map:
            if num != 0:
                return False

        return True

        

        