# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixes = [0]
        runningSum = 0

        for i in range(len(nums)):
            runningSum += nums[i]
            prefixes.append(runningSum)
        print(prefixes)
        for i in range(len(nums)):
            if prefixes[i] == prefixes[-1]-prefixes[i]-nums[i]:
                return i

        return -1