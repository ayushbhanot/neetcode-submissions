class Solution:
    def isValid(self, s: str) -> bool:
        while "{}" in s or "()" in s or "[]" in s: #O(s) time
            s = s.replace("{}", "") #O(s2) time for replace operation and O(s) memory too
            s = s.replace("()", "")
            s = s.replace("[]", "")

        return s == ""