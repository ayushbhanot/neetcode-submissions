class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, maxCount = 0, 0
        seen = set()

        for r in range(len(s)): #O(n) time
            if s[r] in seen:
                maxCount = max(maxCount, len(seen))
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r]) #O(m) space
        maxCount = max(maxCount, len(seen))

        return maxCount