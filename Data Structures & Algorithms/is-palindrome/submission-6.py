class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newString = ""

        for c in s: #O(n) time
            if c.isalnum() == False:
                continue
            newString += c.lower() #O(n) space and time

        return newString == newString[::-1] #O(n) time for '==' and O(n) space and time for [::-1]