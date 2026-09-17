class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # WHat we can do is organize each string into its sorted version and map the strings to their sorted versions (If strings are anagrams they should have same sorted string)

        stringMap = {}

        for string in strs: #O(n) time
            sortedString = "".join(sorted(string)) #Reason im using "".join is becaue sorted on a string makes a list of single chars from string in sorted order and using sorted() over .sort() since we can't use .sort() (Strings are immutable)

            if sortedString not in stringMap: #have to quickluy check and initilaize key if it is not alr in hashmap to prevent error
                stringMap[sortedString] = [] 

            stringMap[sortedString].append(string)

            # Since we sorting inside a forloop it is m being max length of string O(n * mlogm) time and O(n * m) space

        res = []
        for strings in stringMap.values(): #O(n) time
            res.append(strings) #O(n) space

        return res