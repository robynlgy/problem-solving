# Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

# Write an algorithm to minimize the largest sum among these m subarrays.

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        #minimize largest SUM among split arrays
        # min = max(nums)// max = sum(nums) (not actual max, bcz this assumes only 1 split arr, so actual max sb lower)
        # helper -> is it possible to split in m and make min <= X
        # time: O(n * log m) -> n = len(nums) ,  m = r - l

        l , r = max(nums), sum(nums)

        def isValid(minN):

            count = 1       ## be careful of this count!!!!
            currSum = 0
            for num in nums:
                if currSum + num <= minN:
                    currSum += num
                else:
                    if count == m:
                        return False
                    count += 1
                    currSum = num
            return True


        while l < r:
            med = (l + r)//2        # dont name this m
            if isValid(med):
                r = med
            else:
                l = med + 1

        return l



            # if it's a valid min, we're going to look at a smaller min
            #   if we found one, we'll look for an even smaller one
            #   if it's not valid, we want to look at a range that starts at the next larger one















# dis for m = 2 only
#         numL = nums[0]
#         numR = sum(nums[1:])
#         currMax = numR
#         p = 1

#         while numL<numR:
#             # print(numL,numR)
#             numR -= nums[p]
#             numL += nums[p]
#             p += 1
#             if numR>numL:
#                 currMax = numR

#         return min(numL,currMax)
