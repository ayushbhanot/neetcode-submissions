class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""

        for c in s: #O(n) time
            if c.isalnum() == False:
                continue
            newString += c.lower() #O(n) space and time

        return newString == newString[:: -1] #O(n) space and time again for reverse string