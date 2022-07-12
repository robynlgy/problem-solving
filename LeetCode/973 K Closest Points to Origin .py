# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min heap, stores all distance values and pops k times
        # time complx: O(n + k log n)
        # storing all distance and heapify ==> O(n)
        # popping from heap k times = O(k*logn)

#         res = []

#         for i in range(len(points)):
#             x, y = points[i]
#             distance = x**2 + y**2
#             points[i] = (distance,points[i])

#         heapq.heapify(points)
#         for i in range(k):
#             largest = heapq.heappop(points)
#             res.append(largest[1])

#         return res


        # max-heap, keeps heap size of k

            heap = []

            for (x,y) in points:
                dist = -(x*x + y*y)
                if len(heap) == k:
                    heapq.heappushpop(heap,(dist,x,y))
                else:
                    heapq.heappush(heap,(dist,x,y))

            return [(x,y) for (dist,x,y) in heap]