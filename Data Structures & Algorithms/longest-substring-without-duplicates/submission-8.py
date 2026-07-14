class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        maxCount, l, r = 0 , 0, 0

        while r < len(s): #O(n) time
            if s[r] in seen:
                maxCount = max(len(seen), maxCount)
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r]) #O(m) space m = number of possible unique characters
            r += 1
        maxCount = max(len(seen), maxCount)
        return maxCount


        