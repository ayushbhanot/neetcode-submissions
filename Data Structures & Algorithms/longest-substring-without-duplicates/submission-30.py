class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        res = 0
        
        for i in range(len(s)): #O(n) time
            seen = set()
            for j in range(i, len(s)): #O(n2) time
                if s[j] in seen:
                    res = max(res, len(seen))
                    break
                seen.add(s[j])
            res = max(res, len(seen))
        return res