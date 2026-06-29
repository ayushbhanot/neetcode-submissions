class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:#O(n) time
            sortedVersion = ''.join(sorted(word))
            if sortedVersion in result:
                result[sortedVersion].append(word) #O(mlogm) time
            else:
                result[sortedVersion] = [word] #O(m) space

        return list(result.values())