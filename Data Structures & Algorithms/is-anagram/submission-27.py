# An anagram is where Two strings have to be the same as each other in terms of characters and number of characters

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of both strings don't match we know they can't be anagram so easy exit case is this called base case when we return false no right?
        if len(s) != len(t):
            return False
        
        # We can use hashmaps yto store the letters and how many times they appear and then compare at end
        countS, countT = {}, {}
        for c in s: #O(s) time
            countS[c] = countS.get(c, 0) + 1 #O(s) space

        for c in t: #O(t) time
            countT[c] = countT.get(c, 0) + 1 #O(t) space

        return countS == countT #O(s/t) time and space