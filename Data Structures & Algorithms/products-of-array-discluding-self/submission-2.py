class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preArray = [0] * n
        postArray = [0] * n
        preArray[0], postArray[n-1] = 1, 1
        res = [0] * n #O(3n) space -> O(n) space
        #[1,2,3,4]
        #[1,1,2,6]
        #[24,12,4,1]
        #[24,12,8,6]
        for i in range(1, n): #O(n) time
            preArray[i] = preArray[i-1]*nums[i-1]
    
        for i in range(n-2, -1, -1): #O(n) time
            postArray[i] = postArray[i+1] * nums[i+1]

        for i in range(n): #O(n) time
            res[i] = postArray[i] * preArray[i]

        return res

        