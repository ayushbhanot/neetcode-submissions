class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap, tMap = {}, {}

        for c in s: #O(s) time
            sMap[c] = sMap.get(c, 0) + 1 #O(s) space
        
        for c in t: #O(t) time
            tMap[c] = tMap.get(c, 0) + 1 #O(t) space

        return sMap == tMap