class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        seen = set()
        res = 0

        for r in range(len(s)): #O(n) time
            while s[r] in seen:
                res = max(res, len(seen))
                seen.remove(s[l])
                l += 1
            seen.add(s[r]) #O(m) space
        res = max(res, len(seen))

        return res
