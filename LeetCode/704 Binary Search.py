# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1

        while l <= r:
            med = (l+r)//2
            if nums[med] < target:
                l = med + 1
            elif nums[med] > target:
                r = med - 1
            else:
                return med

        return -1
