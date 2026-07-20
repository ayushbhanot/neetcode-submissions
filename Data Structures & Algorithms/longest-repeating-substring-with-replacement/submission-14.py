class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0

        for i in range(len(s)): #O(n) time
            count = {}
            for j in range(i, len(s)): #O(n2) time
                count[s[j]] = count.get(s[j], 0) + 1
                if (j - i + 1) > max(count.values()) + k:
                    break
                res = max(res, j - i + 1)
        
        return res