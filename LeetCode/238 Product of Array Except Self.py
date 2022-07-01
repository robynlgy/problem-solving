# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prefix, postfix = 1,1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

# this sol uses extra space to store prefix/suffix
#         prefix, postfix = [1] , [1]
#         pre,post = 1,1
#         res = []

#         for i in range(len(nums)-1):
#             pre = pre * nums[i]
#             prefix.append(pre)

#         for i in range(len(nums)-1,0,-1):
#             post = post * nums[i]
#             postfix.append(post)

#         # print("prefix",prefix)
#         # print("postfix",postfix)

#         for i in range(len(nums)):
#             res.append(prefix[i]*postfix[len(nums)-i-1])

#         return res