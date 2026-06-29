class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}


        res = 0

        for i in range(len(nums)):
            if nums[i] in mp:
                continue

            leftSequence = mp.get(nums[i] - 1, 0)
            rightSequence = mp.get(nums[i] + 1, 0)
            consSequence = leftSequence + rightSequence + 1

            res = max(consSequence, res)

            mp[nums[i]] = consSequence
            mp[nums[i] + rightSequence] = consSequence
            mp[nums[i] - leftSequence] = consSequence

        return res