class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        res = []

        for num in nums:
            count[num] = nums.count(num)
        
        arr = []
        for num, freq in count.items():
            arr.append([freq, num])
        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])
        return res
