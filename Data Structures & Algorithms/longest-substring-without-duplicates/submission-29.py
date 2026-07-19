class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0

        for i in range(len(s)): #O(n) time
            l = i - 1
            r = i + 1
            seen = set()
            seen.add(s[i])

            while 0 <= l < len(s) and s[l] not in seen:
                seen.add(s[l])
                l -= 1

            while 0 <= r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r += 1
            res = max(res, len(seen))
        
        return res