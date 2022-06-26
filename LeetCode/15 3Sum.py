# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
#  such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        res = []

        for i in range(len(nums)-2):
            if i and nums[i]==nums[i-1]:
                continue

            l,r = i+1, len(nums)-1
            while l<r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum < 0:
                    l+=1
                elif threeSum > 0:
                    r -=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l +=1

        return res