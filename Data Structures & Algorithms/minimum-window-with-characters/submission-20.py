class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        countT = {}
        for c in t: #O(t) time
            countT[c] = countT.get(c, 0) + 1 #O(t) space

        resLen, res = float("infinity"), []
        need, have = len(countT), 0
        window = {}
        l = 0
        for r in range(len(s)): #O(s) time
            
            if s[r] in countT:
                window[s[r]] = window.get(s[r], 0) + 1 #O(t) space

                if window[s[r]] == countT[s[r]]:
                    have += 1

                    while have == need:
                        if (r - l + 1) < resLen:
                            res = [l, r]
                            resLen = (r - l + 1)
                        if s[l] in countT:
                            window[s[l]] -= 1
                            if window[s[l]] < countT[s[l]]:
                                have -= 1
                        l += 1
        if res:
            return s[res[0] : res[1] + 1] #O(s) time and space for output?
        else:
            return ""
                        