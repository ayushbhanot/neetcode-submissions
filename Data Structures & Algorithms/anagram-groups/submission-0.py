class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countMap = {} #Creating hashmap to have counts of characters to word key-value connection as then you can group anagrams

        for word in strs: #O(n) time looping through all words in list
            count = [0] * 26 #Creating new list for 26 character count (Frequency Array)
            for c in word: #O(m) time looping through each individual word by character to get count values
                count[ord(c) - ord('a')] += 1 #Increment each character in a word is this O(n) space as you have to increment each value??
            key = tuple(count) #O(1) space??/ You have to make key immutable to access hashmap or even just for a hashmap??
            if key in countMap:
                countMap[key].append(word) #O(n) space?? It's just appending a value
            else:
                countMap[key] = [word] #O(n) space

        return list(countMap.values())