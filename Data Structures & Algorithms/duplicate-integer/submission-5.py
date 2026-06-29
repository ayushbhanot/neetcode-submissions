class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set() #Use a Hash set as its just a set of hashmap keys which all have to be unique values

        for num in nums: #Iterating over nums O(n) time
            if num in duplicates: #Hashmap has O(1) Look up
                return True #Returns True for the whole function not just the for loop right?

            duplicates.add(num) #.add is set syntax
        return False #If we haven't hit a True yet than no duplicates return False