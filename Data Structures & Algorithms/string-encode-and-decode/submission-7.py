class Solution:
    #[COOL, OK]
    def encode(self, strs: List[str]) -> str:
        
        encodedString = ""
        for string in strs: #O(n) time
            encodedString += f"{len(string)}#{string}"
        return encodedString

    # 4#COOL2#OK
    def decode(self, s: str) -> List[str]:
        strings = []
        i, j = 0, 0
        while i < len(s): #O(c) time
            if s[j] == "#":
                length = int(s[i : j])
                i = j + 1
                strings.append(s[i : i + length])
                i, j = i + length, i + length
            else:
                j += 1
        return strings