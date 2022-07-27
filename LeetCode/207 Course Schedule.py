# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        # make a graph where key -> next class
        # for each key we haven't seen yet, continue to the next class, keeping track of all the classes seen in this path so far, if I see a class already in my path, there's a cycle ie. cant do all classes
        # after I look at my neighbors, remove myself from the path bcz one node could have diff
        # paths that lead to the same node, but doesn't mean there's a cycle

        graph = self.make_graph(numCourses, prereq)
        seen = set()

        def dfs(key,path):
            if key in seen:
                return True
            if key in path:
                return False

            path.add(key)
            for neighbor in graph[key]:
                if not dfs(neighbor,path):
                    return False

            path.remove(key)
            seen.add(key)
            return True


        for key in graph:
            if not dfs(key,set()):
                return False

        return True

    def make_graph(self, numCourses, prereq):
        graph = {}

        for i in range(numCourses):
            graph[i]= []

        for (a,b) in prereq:
            graph[b].append(a)

        return graph
