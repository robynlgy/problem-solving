class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            nums = sorted(nums)

            idx1 = 0
            idx2 = len(nums)-1

            while idx2>idx1:
                sum = nums[idx1]+nums[idx2]

                if sum != target:
                    if (sum > target):
                        idx2 --
                    else:
                        idx1 ++
                return [idx1,idx2]
