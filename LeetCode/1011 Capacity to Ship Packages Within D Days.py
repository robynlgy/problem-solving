# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # goal: find the minimum capacity needed to ship all wtihin x days
        # max capacity = sum(weights) , min capacity = max(weights)
        # helper that says if at this capacity, can it be done
            # hashmap of days, while its <= capacity, increase count
            #> don't need a hashmap since we're not returning the 'pairs', just need a currSum
            # if all can be put into bucket, it's valid
        # but max - min capcity can be huge, binarySearch
        # if mid is valid, is there a smaller one that's also valid -> we want the smallest
            # i want to look at a smaller capacity
            # r = mid
        # if mid is not valid, it's too small
            # l = l + 1
        # when l and r meet, that's the smallest avail
        # time = O( n * logm ) where m = max(weights)-sum(weights), we do binary search on it => O(logm), and each time we look through all weights => O(n) => O(nlogm)


        l,r = max(weights),sum(weights)

        def isValid(cap):
            currWeight = 0
            day = 1
            for weight in weights:
                if currWeight + weight <= cap:
                    currWeight += weight
                else:
                    if day == days:
                        return False
                    day += 1
                    currWeight = weight
            return True

        while l<r:
            m = (l+r)//2
            if isValid(m):
                r = m
            else:
                l = m + 1

        return l
