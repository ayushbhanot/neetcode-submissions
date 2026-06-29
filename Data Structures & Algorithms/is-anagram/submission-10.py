class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #racecar            carrace
        if len(s) != len(t):    #O(1) time and space
            return False

        countS, countT = {}, {} #O(1) time and space

        for i in range(len(s)): #O(n) time
            countS[s[i]] = countS.get(s[i], 0) + 1 #Get the valiue for specific character if it doesnt exit set it to 0 and add 1
            countT[t[i]] = countT.get(t[i], 0) + 1 #O(1) insert but n times twice for each so O(n) spcae

        return countS == countT#26 diff charecates so max keys can be 26 so O(1) spcae