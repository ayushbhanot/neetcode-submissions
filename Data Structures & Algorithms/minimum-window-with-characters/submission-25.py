class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        countT = {}
        for c in t: #O(t) time
            countT[c] = countT.get(c, 0) + 1 #O(t) space
        
        res, resLen = [], float("infinity")
        need, have = len(countT), 0
        l = 0
        countS = {}
        for r in range(len(s)): #O(s) time
            if s[r] not in countT:
                continue
            
            countS[s[r]] = countS.get(s[r], 0) + 1 #O(t) space at most due to prev if statement
            
            if countS[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                if s[l] in countT:
                    countS[s[l]] -= 1
                    if countS[s[l]] < countT[s[l]]:
                        have -= 1
                l += 1

        if res:
            return s[res[0] : res[1] + 1] #O(s) space for output
        else:
            return ""