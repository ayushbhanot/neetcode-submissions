class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Ok so a bottle neck was we were taking up time and space due to having to use sorted() so instead maybe we can build a custom hashfunction to find out how many letters and what type of letters in the string

        stringMap = {}

        for string in strs: #O(n) time

            hashedString = [0] * 26 #This will represent number of characters O(1) space since it is fixed size

            for c in string: #O(m) time m being length of max string
                hashedString[ord(c) - ord('a')] += 1
            
            hashedString = tuple(hashedString) #Have to convert to tuple since we can't use mutable collection as key in hashmap (Is tuple a collection?)

            if hashedString not in stringMap:
                stringMap[hashedString] = [] #Initilaizoing incase we never seen that type of anagram before
            
            stringMap[hashedString].append(string) #O(n) space

        res = []
        
        for strings in stringMap.values(): #O(n) time
            res.append(strings) #O(n) space

        return res
            
