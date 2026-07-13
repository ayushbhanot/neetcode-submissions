class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxCount = 0

        for i in range(len(s)): #O(n) time
            seen = set()
            count = 0
            for j in range(i, len(s)): #O(n2) time
                if s[j] in seen:
                    break
                seen.add(s[j]) #O(n) space
                count += 1
            maxCount = max(count, maxCount)

        return maxCount