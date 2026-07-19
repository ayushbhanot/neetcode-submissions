class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        res = 0
        
        for i in range(len(s)): #O(n) time
            seen = set()
            for j in range(i, len(s)): #O(m) time
                if s[j] in seen:
                    res = max(res, len(seen))
                    break
                seen.add(s[j]) #O(m) space
            res = max(res, len(seen))
        return res