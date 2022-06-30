# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)] # can't do [[]]*len(nums) bcz ref type
        counter = Counter(nums)
        res = []
        
        for num,count in counter.items():
            bucket[count].append(num)

        while len(res)<k and bucket:
            last = bucket.pop()
            for num in last:
                res.append(num)
                
        return res