class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countMap = {} #Creating a hashmap to store key-value pairs with count-words as pairs

        for word in strs: #O(number of words) time (O(m))
            key = ''.join(sorted(word))#This is another hashing function we can use that we have to use .join as sorted() returns a list so we need to convert to 1 string and sorted takes O(len(word)) space and O(nlogn) time (len(word) = n)
            if key in countMap:
                countMap[key].append(word)
            else:
                countMap[key] = [word]
            #Since we have to store each sorted key for anagram O(k) space and each word as a value O(n) space
        return list(countMap.values()) #O(nlogn*m) time and O(n*k) space
        #No frequency Array used