class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = [0] * 26

        for i in range(len(s)):
            hashmap[ord(s[i]) - ord('a')] += 1
            hashmap[ord(t[i]) - ord('a')] -= 1

        for val in hashmap:
            if val != 0:
                return False

        return True