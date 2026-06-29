class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs: #O(m) time
            s += str(len(string)) + "#" + string #O(m) space
        return s
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s): #O(m) time
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            strs.append(s[j + 1 : j + 1 + length]) #O(m) space for full string since you have to add each char for each string and  + O(n) space since its a list which is indxable so n pointers for n strings
            i = j + 1 + length
        return strs
