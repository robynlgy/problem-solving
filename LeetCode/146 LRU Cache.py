# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

class ListNode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'{self.key}-{self.value} -> {self.next}'

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.tail = ListNode()
        self.hash = {}

    def get(self, key: int) -> int:
        node = self.hash.get(key,None)
        if not node: return -1
        if self.tail != node:
            self._latest(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # if key exists, update value
        if key in self.hash:
            node = self.hash[key]
            node.value = value
            if self.tail != node:
                self._latest(node)
            return

        # if num keys exceed capacity, evict LRU
        if len(self.hash) == self.capacity:
            remove = self.head.next
            # print("removing:",remove.key)
            self.hash.pop(remove.key,None)
            self.head.next = remove.next
            if remove.next:
                remove.next.prev = self.head


        new = ListNode(key,value)
        # if first node
        if not self.head.next:
            self.head.next = new
            self.tail = new
            new.prev = self.head
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        self.hash[key] = new
        # print("HM length:",len(self.hash))
        # print("HM:",self.hash.keys())
        # print("LL....",self.head.next)

    def _latest(self, node: ListNode) -> None:
        prev1, next1 = node.prev, node.next
        prev1.next, next1.prev = next1, prev1
        self.tail.next = node
        node.prev, node.next = self.tail, None
        self.tail = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)