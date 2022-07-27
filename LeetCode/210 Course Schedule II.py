# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

# Example 2:
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

# Example 3:
# Input: numCourses = 1, prerequisites = []
# Output: [0]

class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        # create an adjacency list of relationship form 0 to n-1 --> O(n)
        #    {course A : prereq course to course A }
        # for courses with an empty list --> {a:[]} --> this means it has no prereq and can be taken any time
        # as we loop over all the courses, courses w no prereq would be our base case,  --> O(p+n) where p = prereq,n is # of courses, bcz at worst case we have to travel each edge twice
        # and we wanted to add that to our res list, as we return, we'll append ourselves to the res
        # visited set --> tracks current path, if curr key is already in it, that means there's a cycle
        # seen set --> only purpose is to save time but takes up space, used for look ups to return early if seen before
        # O(n) time O(n) space

        res = []
        graph = {i:[]for i in range(numCourses)}
        for (a,b) in prereq:
            graph[a].append(b)

        visiting = set()
        seen = set()
        # doing look ups so need a set for O(1), but need a list for res bcz of ordering
        def dfs(key):
            if key in visiting:
                return False
            if key in seen:
                return True
            # if graph[key] == []: <-- don't need this part! if no neighbors you'll just add at the end anywyas
            #     res.append(key)
            #     seen.add(key)
            #     return True

            visiting.add(key)
            for neighbor in graph[key]:
                if not dfs(neighbor):
                    return False
            visiting.remove(key)

            res.append(key)
            seen.add(key)
            return True

        for key in graph:
            if not dfs(key):
                return []

        return res
