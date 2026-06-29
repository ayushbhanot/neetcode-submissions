class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #racecar                carrace
        if len(s) != len(t): #O(n) time
            return False

        count = [0] * 26 #O(1) * 26 time and space

        for i in range(len(s)): #O(n) time
            count[ord(s[i]) - ord('a')] += 1 #O(26) so O(1) time and space?
            count[ord(t[i]) - ord('a')] -= 1
            #These turns the count into a hashmap and we hash to get a value of 26 and the n make that key increment or decrement if they equal 0 at end means anagram as they balance out

        for val in count: #O(26) so O(1) time
            if val != 0:
                return False

        return True