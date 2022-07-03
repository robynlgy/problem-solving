# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        runningSum = 0

        for num in nums:
            runningSum += num
            res.append(runningSum)

        return res