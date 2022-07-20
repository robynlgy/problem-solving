# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

# Return the least number of units of times that the CPU will take to finish all the given tasks.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #time = O(n * m), where n = num of tasks, m is the idle time

        count = Counter(tasks) #O(n)
        # maxHeap = [(-val,key) for i,(key,val) in enumerate(count.items())]
        maxHeap = [-cnt for cnt in count.values()] #O(26) + O(26)
        heapq.heapify(maxHeap) #O(26)
        # print(maxHeap)

        time = 0
        queue = deque() # pairs of [-cnt,idleTime]

        while maxHeap or queue:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1    #O(log(26))
                # print("whats cnt",cnt)
                if cnt:
                    queue.append([cnt,time+n])
            if queue and (queue[0][1] == time):
                # cnt, time = queue.popleft()
                heapq.heappush(maxHeap,queue.popleft()[0]) #O(log(26))

        return time








#         #two hashmaps?
#         # hashmap 1 : Counter of all tasks O(n)
#         # hashmap 2: Cooldown of all tasks , each time it's done the value sb reset to n and on each iteration, reduce count n*O(k), where k is num of keys, and n is total ops
#         # so each time a task is done, unit +1, hashmap 1 - 1, hashmap 2 - 1, del from hashmap 1 if count is 0, if len of hashmap1 is done, return unit count
#         if n == 0:  return len(tasks)

#         rem_tasks = Counter(tasks)
#         cd_map = {}
#         res = 0


#         for task in rem_tasks.keys():
#                 cd_map[task] = 0

#         while rem_tasks:
#             res += 1
#             self.reduceCount(cd_map)
#             for task in rem_tasks:
#                 if cd_map[task] == 0:
#                     cd_map[task] = n+1
#                     rem_tasks[task] -= 1
#                     if rem_tasks[task] == 0:
#                         del rem_tasks[task]
#                     break

#         return res

#     def reduceCount(self,cd_map):
#         for i,(key,val) in enumerate(cd_map.items()):
#             if val:
#                 cd_map[key] -=1