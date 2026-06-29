class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            s += str(len(string)) + "#" + string
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            strs.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
            #2#dc1#d
            #0123456
        return strs