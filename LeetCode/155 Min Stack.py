# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack =[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# here I created a separate Node class to store the min at each val instead, but not as clean
# class Node:

#     def __init__(self,val:int):
#         self.val = val;
#         self.min = val;
#

# class MinStack:

#     def __init__(self):
#         self.stack = []

#     def push(self, val: int) -> None:
#         new = Node(val);
#         if self.stack:
#             new.min = min(self.stack[-1].min,val)
#         self.stack.append(new)

#     def pop(self) -> None:
#         self.stack.pop()


#     def top(self) -> int:
#         return self.stack[-1].val


#     def getMin(self) -> int:
#         return self.stack[-1].min



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()