class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxCount, l, r = 0, 0, 0
        seen = set()

        while r < len(s): #O(n) time
            while s[r] in seen:
                maxCount = max(maxCount, len(seen))
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            r += 1
        maxCount = max(maxCount, len(seen))

        return maxCount