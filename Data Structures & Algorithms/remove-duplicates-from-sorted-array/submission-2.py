class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set(nums) #Set removes dupliactes but doesnt preserve order
                            #O(n) time to create and assign a set as it has to go through all values of array 
                            #O(n) space also as it has to copy all values into set

        nums[:] = sorted(unique) #Sorting library is O(nlogn) time
        return len(nums)

