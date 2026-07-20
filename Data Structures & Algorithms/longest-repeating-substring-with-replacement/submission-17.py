class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l, res = 0, 0
        count = {}
        maxF = 0

        for r in range(len(s)): #O(n) time
            count[s[r]] = count.get(s[r], 0) + 1
            maxF = max(count[s[r]], maxF)
            while (r - l + 1) > k + maxF:
                count[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)

        return res