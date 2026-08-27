class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sortedMap = {}
        for string in strs:
            hashedString = self.hashString(string)
            if hashedString not in sortedMap:
                sortedMap[hashedString] = []
            sortedMap[hashedString].append(string)

        return list(sortedMap.values())

    def hashString(self, string):
        count = [0] * 26
        for c in string:
            count[ord(c) - ord('a')] += 1
        return str(count)