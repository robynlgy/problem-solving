# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0]*len(temps)
        stack = []  # (temp,idx)
        
        for i,t in enumerate(temps):
            while stack and t > stack[-1][0]:
                temp, tempIdx = stack.pop()
                res[tempIdx] = (i-tempIdx)
            stack.append([t,i])
        
        return res
        
       
# brute force
#         res = []
        
#         for i in range(len(temps)):
#             count = 0
#             found = False
#             for j in range(i+1,len(temps)):
#                 count += 1
#                 if temps[j] > temps[i]:
#                     found = True
#                     break
#             res.append(count) if found else res.append(0)
        
#         return res
