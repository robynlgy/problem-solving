# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:
#         # two pointer l,r = 0,len(height)-1
#         # calculate distance = r-l-1
#         # calculate area = shorter pointer * distance
#         # maxArea = max(area,maxArea)
#         # if l<r, move l , else move r
#         # if l = r
#         ## if equal, doesn't matter which one u shift, bcz the only way the area is going to be higher is if BOTH left and right are higher, so for whichever side first sees a higher one, the other one will then have to shift and ALSO find a higher one for it to matter, so at the end you will end up at the same point

        l,r = 0, len(height)-1
        maxArea = 0

        while l<r:
            distance = r-l
            area = distance * min(height[r],height[l])
            maxArea = max(maxArea,area)
            if height[l] < height[r]:
                l +=1
            else:
                r -= 1
        return maxArea