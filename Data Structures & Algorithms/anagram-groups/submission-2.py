class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countMap = {} #Hashmap to store counts-word as key-values

        for word in strs: #O(words) time
            hashing = [0] * 26 #Lets create a frequency harray to make a hashing function
            for c in word: #O(character in each word) time
                hashing[ord(c) - ord('a')] += 1 #Hashing so each character is 0 indexed
                #hashing = [1,2,3]
            if tuple(hashing) not in countMap:
                countMap[tuple(hashing)] = [word] #O(words) space for both if and else combined cuz either wauy you have to append or add each word?
            else:
                countMap[tuple(hashing)].append(word)
            
        return list(countMap.values())