class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #If not same length that means that 
            return False

        return sorted(s) == sorted(t) #each sorted() takes Onlogn time and On memory but we don't count constants cant use .sort() cuz it doesnt return anything and we don't count contants so we got #O(nlogn) time and O(n) space