# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxLen = 0

        for num in nums:
            if (num - 1) not in nums:
                length = 1
                while (num + 1) in nums:
                    length +=1
                    num += 1
                maxLen = max(maxLen,length)
        return maxLen