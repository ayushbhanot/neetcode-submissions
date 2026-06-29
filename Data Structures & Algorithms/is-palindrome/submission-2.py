class Solution:
    def isPalindrome(self, s: str) -> bool:
        array = []
        for c in s:
            if c == ' ':
                continue
            if c.isalpha() or c in '0123456789':
                array.append(c.lower())
            else:
                continue
        reversearray = []
        for c in range(len(array) - 1, -1, -1):
            reversearray.append(array[c].lower())

        for i in range(len(array)):
            if array[i] != reversearray[i]:
                return False
        return True
        #O(n) time O(1) space