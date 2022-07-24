# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#DP -> bottom-up

class Solution:
    def climbStairs(self, n: int) -> int:
        #DP - bottom up approach
        # if we draw a decision tree, we'll see that there are a lot of repeated steps
        # one way to optimize is through memoization
        # another way is DP bottom up, where we look at:
        # eg. n = 5
        # how many ways are there to reach 5 from:
        # 5 -> 1  // 4 -> 1
        # at 3,we know we go to 4/5, to which we know how many ways there are to get to 5 at those two points. So # at 3 would be # at 4 and 5 ie. 1+1 = 2
        # we continue this pattern until we reach 0, and we only really need to store 2 values instead of full array

        one, two = 1, 1

        for i in range(n-2,-1,-1):
            one, two = one + two, one

        return one