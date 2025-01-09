class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)

        node = ListNode(key, value)
        self.dic[key] = node
        self.add(node)

        if len(self.dic) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]

    def add(self, node):
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def print_list(self):
        print("Adding a new node and printing list")
        node = self.head
        while node is not self.tail:
            print(node.key)
            node = node.next
        print(self.tail.key)


def print_results(get_responses: list, expected_output: list):
    print(get_responses)
    print(f"Expected {expected_output}")
    print(f"Actual {get_responses}")
    print(expected_output == get_responses)

def leet_code_test_1():
    lru_cache = LRUCache(2)
    get_responses = []
    get_responses.append(None)
    expected_output = [None, None, None, 1, None, -1, None, -1, 3, 4]
    get_responses.append(lru_cache.put(1, 1))
    get_responses.append(lru_cache.put(2, 2))
    lru_cache.print_list()
    print(lru_cache.dict)
    get_responses.append(lru_cache.get(1))
    lru_cache.print_list()
    get_responses.append(lru_cache.put(3, 3))
    lru_cache.print_list()
    print(lru_cache.dict)
    get_responses.append(lru_cache.get(2))
    get_responses.append(lru_cache.put(4, 4))
    lru_cache.print_list()
    print(lru_cache.dict)
    get_responses.append(lru_cache.get(1))
    get_responses.append(lru_cache.get(3))
    get_responses.append(lru_cache.get(4))
    print_results(get_responses, expected_output)

def leet_code_test_2():
    lru_cache = LRUCache(2)
    get_responses = []
    get_responses.append(None)
    expected_output = [None, -1, None, -1, None, None, 2, 6]
    get_responses.append(lru_cache.get(2))
    get_responses.append(lru_cache.put(2, 6))
    get_responses.append(lru_cache.get(1))
    get_responses.append(lru_cache.put(1, 5))
    get_responses.append(lru_cache.put(1, 2))
    get_responses.append(lru_cache.get(1))
    get_responses.append(lru_cache.get(2))
    # lru_cache.print_list()
    # print(lru_cache.dict)
    print_results(get_responses, expected_output)

if __name__ == "__main__":
    # One test example from leet code
    leet_code_test_2()

