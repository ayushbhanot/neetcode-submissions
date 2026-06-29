class Solution:

    def encode(self, strs: List[str]) -> str:
        #[rc, xd]
        s = "" 
        for string in strs: #O(n) time
            s += str(len(string)) + "#" + string #this techincall makes it O(n2) because it copys strings and exponentially makes bigger strings but for sake we'll keep it O(n) time (strings in python are immutable)
        return s #Also O(m) space
    
    def decode(self, s: str) -> List[str]:
        res = [] #O(m) space
        i = 0
        while i < len(s): #O(m) time
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            #   [we, say]
            #   2#we3#say
            res.append(s[j + 1 : j + 1 + length]) #O(m + n) space with m being total characters and n being numebr of string splits in array
            i = j + 1 + length
        return res
            