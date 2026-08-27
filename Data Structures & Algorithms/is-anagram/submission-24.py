class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) #O(slogs) + O(tlogt) and O(s) + O(t) space