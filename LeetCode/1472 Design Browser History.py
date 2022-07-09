# You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

# Implement the BrowserHistory class:

# BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
# void visit(string url) Visits url from the current page. It clears up all the forward history.
# string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
# string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.


# ===================== Stacks Ver. =====================
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.future = []

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.future = []

    def back(self, steps: int) -> str:
        count = 0
        while len(self.history) > 1:
            last_visited = self.history.pop()
            self.future.append(last_visited)
            count += 1
            if count == steps:
                break
        return self.history[-1]

    def forward(self, steps: int) -> str:
        count = 0
        while len(self.future) > 0:
            next_visited = self.future.pop()
            self.history.append(next_visited)
            count += 1
            if count == steps:
                break
        return self.history[-1]




# ===================== Linked List Ver. =====================
# this stores nodes that are not used anymore when forward history should be cleared
# class Node:

#     def __init__(self,val = None):
#         self.val = val
#         self.prev = None
#         self.next = None

#     def __repr__(self):
#         return f'{self.val} - prev:{self.prev}, next:{self.next}'

# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.head = Node(homepage)
#         self.curr = self.head

#     def visit(self, url: str) -> None:
#         new_visit = Node(url)
#         self.curr.next = new_visit
#         new_visit.prev = self.curr
#         self.curr = new_visit

#     def back(self, steps: int) -> str:
#         count = 0
#         while self.curr.prev:
#             self.curr = self.curr.prev
#             count += 1
#             if count == steps:
#                 break
#         return self.curr.val


#     def forward(self, steps: int) -> str:
#         count = 0
#         while self.curr.next:
#             self.curr = self.curr.next
#             count += 1
#             if count == steps:
#                 break
#         return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)