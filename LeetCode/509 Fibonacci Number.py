# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

class Solution:
    def fib(self, n: int) -> int:
        #rec with memoization
        def rec(n,memo={}):
            if n in memo:
                return memo[n]
            if n <= 1:
                return n
            res = rec(n-1)+rec(n-2)
            memo[n]=res
            return res

        return rec(n)

          #rec
#         if n <= 1: return n

#         return self.fib(n-1)+ self.fib(n-2)


#         F = [None]*(n+1)
#         F[0],F[1] = 0,1

#         for i in range(2,n+1):
#             F[i] = F[i-1] + F[i-2]
#         return F[n]




