class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Sort then use 2 pointer appraoch we have to sort to ensure the numbers are in numerical order but first we have to make it in tuple preferred since tuples are immutable so we can remmeber what was original index for each number

        numbers = []

        for i in range(len(nums)): #O(n) time
            numbers.append((nums[i], i)) #O(n) space

        numbers.sort() #O(nlogn) time and O(n) space due to Pythons built in sorting algorithm (Timsort)

        l, r = 0, len(numbers) - 1

        while l < r: #O(n) time
            total = numbers[l][0] + numbers[r][0]

            if total == target:
                return [min(numbers[l][1], numbers[r][1]), max(numbers[l][1], numbers[r][1])]    

            elif total < target:
                l += 1

            else:
                r -= 1

        return []   # Worst case O(nlogn) time and O(n) space 