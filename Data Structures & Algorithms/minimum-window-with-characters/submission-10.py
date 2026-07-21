class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""
        
        countT = {}
        for c in t: #O(t) time
            countT[c] = countT.get(c, 0) + 1 #O(t) space

        res = []

        for i in range(len(s)): #O(s) time
            countS = {}
            need = set(t) #O(t) time and space
            for j in range(i, len(s)): #O(s2) time
                if s[j] in need:
                    countS[s[j]] = countS.get(s[j], 0) + 1
                    if countS[s[j]] >= countT[s[j]]:
                        need.remove(s[j])
                    if len(need) == 0:
                        res.append(s[i:j + 1])
        if res:
            minRes = res[0]
            for string in res:
                if len(string) < len(minRes):
                    minRes = string
            return minRes
        else:
            return ""
        


        