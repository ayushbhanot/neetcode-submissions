class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) # t = max(len(s), len(t)) O(tlogt) and O(t) space worst case reason we have to use sorted() is this creates a new array / string in space because we can't use .sort() since strings are immutable