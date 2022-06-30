# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # on average, (similar to quick sort), this is O(n).
        # but worst case is O(n^2) if the pivot always ends up at the end of the list each time, ie. one element is swapped each time quicksort is called
        # this algo is called quick select

        k = len(nums)-k

        def quickSort(l,r):
            pivot, pointer = r, l   # using last num as pivot, could be anything within range
            for i in range(l,r):
                if nums[i] < nums[pivot]:
                    nums[i],nums[pointer] = nums[pointer],nums[i]
                    pointer += 1
            nums[pointer], nums[pivot] = nums[pivot], nums[pointer]

            if pointer < k: return quickSort(pointer+1, r)
            elif pointer > k: return quickSort(l,pointer-1)
            else: return nums[pointer]

        return quickSort(0,len(nums)-1)




        # solving with heap is O(nlogk?), slightly better than O(nlogn) depending on what k is
        # heap = []
        # heapq.heapify(heap)
        # for num in nums:
        #     if len(heap) < k:
        #         heapq.heappush(heap,num)
        #     else:
        #         heapq.heappushpop(heap,num)
        # return heap[0]
