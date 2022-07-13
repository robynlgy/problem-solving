# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

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
                count += math.ceil(pile / speed)
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