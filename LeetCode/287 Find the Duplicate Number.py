# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            # print(slow,fast)
            if slow == fast:
                break

        # print(slow)
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            # print(slow,slow2)
            if slow == slow2:
                return slow



        #O(nlogn) time, modifies array / O(n) space
        # sort -> same as next

        # O(n) time, O(n) space
#         seen = set()

#         for num in nums:
#             if num in seen:
#                 return num
#             seen.add(num)

        #brute-force n^2 time, constant space
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return nums[i]

