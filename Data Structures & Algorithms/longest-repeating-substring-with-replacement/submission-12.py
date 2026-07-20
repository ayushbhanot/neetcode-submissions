class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        count = {}
        res = 0
        maxF = 0

        for r in range(len(s)): #O(n) time
            count[s[r]] = count.get(s[r], 0) + 1 #O(26) space
            maxF = max(maxF, count[s[r]])
            while (r - l + 1) > maxF + k: 
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res