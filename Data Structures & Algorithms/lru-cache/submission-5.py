class LRUNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.head = self.tail = None
    
    def insert(self, key: int, value: int):
        if self.head is None:
            self.head = self.tail = LRUNode(key, value)
        else:
            newNode = LRUNode(key, value)
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

        self.cache[key] = self.head
    
    def remove(self, target: LRUNode):
        if target == self.head:
            self.head = self.head.next
        
        if target == self.tail:
            self.tail = self.tail.prev
        
        if target.next is not None:
            target.next.prev = target.prev
        
        if target.prev is not None:
            target.prev.next = target.next
        
        del self.cache[target.key]
        del target

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key].val
            self.remove(self.cache[key])
            self.insert(key, value)

            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.insert(key, value)

        if len(self.cache) > self.capacity:
            self.remove(self.tail)