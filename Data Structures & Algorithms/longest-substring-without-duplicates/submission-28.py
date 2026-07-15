class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r, maxCount = 0, 0, 0
        mp = {}

        while r < len(s): #O(n) time
            if s[r] in mp and mp[s[r]] >= l:
                maxCount = max(r - l, maxCount)
                l = mp[s[r]] + 1
            mp[s[r]] = r
            r += 1
        maxCount = max(r - l, maxCount)

        return maxCount