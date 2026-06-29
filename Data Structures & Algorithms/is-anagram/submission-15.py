class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #racecar            carrace

        return sorted(s) == sorted(t) #O(nlogn+mlogm) time O(n+m) space