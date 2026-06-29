class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []
        for num in nums:
            if num == val:
                continue
            else: tmp.append(num)
        nums[:] = tmp
        return len(nums)