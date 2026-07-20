class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0

        for i in range(len(s)): #O(n) time
            count = {}
            maxF = 0
            for j in range(i, len(s)): #O(n2) time
                count[s[j]] = count.get(s[j], 0) + 1
                maxF = maxF = max(count[s[j]], maxF)
                if (j - i + 1) > maxF + k:
                    continue
                res = max(res, j - i + 1)

            
        return res
