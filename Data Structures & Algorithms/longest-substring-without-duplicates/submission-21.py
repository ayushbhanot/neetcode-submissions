class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxCount = 0

        for i in range(len(s)): #O(n) time
            seen = set()
            for j in range(i, len(s)): #O(m) time
                if s[j] in seen:
                    break
                seen.add(s[j]) #O(m) space
            maxCount = max(len(seen), maxCount)
        return maxCount
