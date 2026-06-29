class Solution:

    def encode(self, strs: List[str]) -> str:
        res =  ""
        for i, string in enumerate(strs):
            length = len(string)
            res += f"{length}#{string}"
        #   4#neet4#code
        return res
        
        #size = [4, 4, 4, 3]

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res