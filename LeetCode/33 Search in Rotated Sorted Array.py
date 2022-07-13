# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #actual O(log n)
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            # if in left portion
            if nums[m]>=nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
            # if in right portion (nums[m] <= nums[l])
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                elif target > nums[m]:
                    l = m + 1
        return -1




#         # time : O(2 log n) -> two binary searches ~> O(log n) , space: O(1)
#         #first find the largest num
#         #with the largest num index, identify the correct half to search in
#         #binary search on that half


#         if len(nums) == 1: return 0 if nums[0] == target else -1
#         if target == nums[-1]: return len(nums)-1
#         if target == nums[0]: return 0

#         # find max num
#         ml,mr = 0,len(nums)-1

#         while ml<mr:
#             m = (ml+mr)//2
#             if nums[m] > nums[-1]:
#                 ml = m + 1
#             else:
#                 mr = m

#         max_idx = ml - 1
#         if target > nums[max_idx]: return -1
#         if target == nums[max_idx]: return max_idx

#         # identify correct half to look at
#         if target < nums[-1]:
#             l,r = max_idx+1,len(nums)-1
#         elif target > nums[-1]:
#             l,r = 0, max_idx

#         # binary search
#         while l<=r:
#             m = (l+r)//2
#             if nums[m]>target:
#                 r = m - 1
#             elif nums[m]<target:
#                 l = m+1
#             else:
#                 return m

#         return -1
