class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min bananas/hour to finish all bananas within h hours
        # max bananas = max(piles) min = 1
        # binary search to find the smallest possible speed, if 5 ok, then 10 ok
        # helper fx to find if at a certain speed, can she finish it all
            # have a counter
            # for each num, add num // speed + 1 to counter
            # if counter exceeds h, return false
        # if speed x is valid, i want to find if theres an even lower speed
            # r =  m
        # if speed is invalid, i need more time
            # l = l + 1

        l ,  r = 1, max(piles)

        def isValid(speed):
            count = 0
            for pile in piles:
                count += ((pile-1)//speed)+1 # <== faster than math.ceil
                # count += math.ceil(pile / speed)
                if count > h:
                    return False
            return True

        while l < r:
            m = (l+r)//2
            if isValid(m):
                r = m
            else:
                l = m + 1

        return l
# class Solution:
#     def minEatingSpeed(self, piles: List[int], H: int) -> int:
#         l, r = 1, max(piles)
#         k = 0

#         while l <= r:
#             m = (l + r) // 2

#             totalTime = 0
#             for p in piles:
#                 totalTime += ((p-1)//m) + 1
#             if totalTime <= H:
#                 k = m
#                 r = m - 1
#             else:
#                 l = m + 1
#         return k