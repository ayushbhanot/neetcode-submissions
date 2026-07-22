class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""
        
        countT = {}
        for c in t: #O(t) time
            countT[c] = countT.get(c, 0) + 1 #O(t) space

        res = []
        resLen = float("infinity")

        for i in range(len(s)): #O(s) time
            need = len(countT)
            have = 0
            countS = {}
            for j in range(i, len(s)): #O(s2) time
                if s[j] in countT:
                    countS[s[j]] = countS.get(s[j], 0) + 1 #O(s2) space
                    if countS[s[j]] == countT[s[j]]:
                        have += 1
                    if have == need and (j - i + 1) < resLen:
                        res = [i, j + 1]
                        resLen = j - i + 1
                        break

        if res:
            return s[res[0] : res[1]]
        return "" #Total = O(s2) time and space?