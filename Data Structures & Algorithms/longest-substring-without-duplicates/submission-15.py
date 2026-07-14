class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxCount = 0

        for i in range(len(s)): #O(n) time
            seen = set()
            for j in range(i, len(s)): #O(m) time, with m being number of unique chars (ASC2 is constant number so O(1) techincally)
                if s[j] in seen:
                    break
                seen.add(s[j]) #O(m) space
            maxCount = max(maxCount, len(seen))
        
        return maxCount