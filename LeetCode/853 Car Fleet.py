# There are n cars going to the same destination along a one-lane road. The destination is target miles away.

# You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

# A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

# A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

# If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

# Return the number of car fleets that will arrive at the destination.

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in zip(position,speed)]
        maxTime = 0
        count = 0

        for p,s in sorted(pairs)[::-1]:
            time = (target - p)/s
            if time > maxTime:
                maxTime = time
                count += 1

        return count


#         pos = []
#         stack = []

#         for i in range(len(position)):
#             pos.append((position[i],speed[i]))

#         pos.sort(key=lambda x:x[0],reverse=True)
#         print(pos)

#         for p,s in pos:
#             steps = (target-p)/s
#             if stack and steps <= stack[-1]:
#                 continue
#             stack.append(steps)

#         return len(stack)