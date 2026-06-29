class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = []
        for i in range(len(nums)):
            freq.append([])

        count = {}

        for num in nums:
            count[num] = count.get(num, -1) + 1

        for key, value in count.items():
            freq[value].append(key)


        res = []
        for i in range(len(freq) - 1, -1, -1):
            for key in freq[i]:
                res.append(key)
                if len(res) == k:
                    return res