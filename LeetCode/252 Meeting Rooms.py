# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda i:i[0])

        for i in range(1,len(intervals)):
            if intervals[i][0]<intervals[i-1][1]:
                return False
        return True



#         without sort, O(n^2)
#         if len(intervals) == 0: return True

#         for i in range(len(intervals)):
#             start = intervals[i][0]
#             end = intervals[i][1]
#             for j in range(i+1,len(intervals)):
#                 #start before, end before first one starts
#                 if start <= intervals[j][0] and end <= intervals[j][0]:
#                     continue
#                 #start after, start after first one ends
#                 elif start >= intervals[j][0] and start >= intervals[j][1]:
#                     continue
#                 else:
#                     return False
#         return True
