# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#DP -> bottom-up

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-2,-1,-1):
            one, two = one + two, one

        return one