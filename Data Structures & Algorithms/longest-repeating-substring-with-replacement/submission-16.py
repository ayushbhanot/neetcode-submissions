class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l, res = 0, 0
        count = {}

        for r in range(len(s)): #O(n) time
            count[s[r]] = count.get(s[r], 0) + 1
            while (r - l + 1) > k + max(count.values()):
                count[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)

        return res