class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #racecar            carrace
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)): #O(n) time
            countS[s[i]] = countS.get(s[i] , 0) + 1 #O(1) insert max 26 inserts so O(1)
            countT[t[i]] = countT.get(t[i], 0) + 1

        return countS == countT #O(n) time