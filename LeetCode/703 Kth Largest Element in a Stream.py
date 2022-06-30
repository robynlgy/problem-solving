# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Implement KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums= nums
        self.k = k
        heapq.heapify(nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums)<self.k:
            heapq.heappush(self.nums,val)
        else:
            heapq.heappushpop(self.nums,val)        # should be slightly faster then separate push then pop

        # while len(self.nums) > self.k:
        #     heapq.heappop(self.nums)

        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
