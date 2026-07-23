class Solution:
    def isValid(self, s: str) -> bool:
        
        while "[]" in s or "{}" in s or "()" in s: #O(s) time
            s = s.replace("{}", "")
            s = s.replace("[]", "")
            s = s.replace("()", "") #O(s2) time and #O(s) space
        
        return s == ""