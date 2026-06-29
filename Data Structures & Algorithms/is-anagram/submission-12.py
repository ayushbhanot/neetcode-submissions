class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #racecar                carrace
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t) #This actually can be used on strings since they are immutable and O(nlogn) time and O(n) space