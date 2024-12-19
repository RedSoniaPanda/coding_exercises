class LRUCache:

    def __init__(self, capacity: int):
        self.lru = None
        self.capacity = capacity
        self.lru_cache = {}

    def get(self, key: int) -> int:
        if key in lru_cache.keys():
            return key
        else:
            return -1

    def put(self, key: int, value: int) -> None:

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
