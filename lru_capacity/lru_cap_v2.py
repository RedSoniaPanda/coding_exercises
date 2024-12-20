from typing import List


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        # self.lru = None
        self.capacity = capacity
        self.lru_cache = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        previous_node = node.prev
        next_node = node.next
        previous_node.next = next_node
        next_node.prev = previous_node

    def get(self, key: int) -> int:
        if key not in self.lru_cache.keys():
            return -1
        node = self.lru_cache[key]
        self.remove(node=node)
        self.add(node=node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # implement node
        pass


if __name__ == "__main__":
    lru_cache = LRUCache(2)
    get_responses = []
    get_responses.append(None)
    # One test example from leet code
    get_responses.append(lru_cache.put(1, 1))
    print(lru_cache.lru_cache)
    get_responses.append(lru_cache.put(2, 2))
    print(lru_cache.lru_cache)
    get_responses.append(lru_cache.get(1))
    get_responses.append(lru_cache.put(3, 3))
    print(lru_cache.lru_cache)
    get_responses.append(lru_cache.get(2))
    get_responses.append(lru_cache.put(4, 4))
    print(lru_cache.lru_cache)
    get_responses.append(lru_cache.get(1))
    get_responses.append(lru_cache.get(3))
    get_responses.append(lru_cache.get(4))
    print(get_responses)
    print([None,None,None,1,None,-1,None,-1,3,4])
    print([None,None,None,1,None,-1,None,-1,3,4] == get_responses)
