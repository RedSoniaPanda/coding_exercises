class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.tail = None
        self.head = None
        self.dict = {}

    def get(self, key: int) -> int:
        if key not in self.dict.keys():
            return -1

        # remove node from list
        node = self.dict[key]
        self.remove_node(node=node)
        # add it back to top priority
        self.add(node=node)
        return node.value

    def add(self, node: ListNode) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
            self.tail.prev = self.head
            self.tail.next = self.head
            self.head.prev = self.tail
            self.head.next = self.tail
        else:
            # New entry
            if self.head.next == self.tail:
                self.head = node
                self.tail.next = self.head
                self.tail.prev = self.head
                self.head.prev = self.tail
                self.head.next = self.tail
            else:
                head_tmp = self.head
                self.head = node
                self.head.next = head_tmp
                self.head.prev = self.tail
                self.tail.next = self.head

    def remove(self) -> None:
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        if self.head.next == self.tail:
            self.tail = self.head
            self.head.next = self.tail
            self.head.prev = self.tail
            self.tail.prev = self.head
            self.tail.next = self.head
        else:
            prev_node = self.tail.prev
            self.tail = prev_node
            self.tail.next = self.head
            self.head.prev = self.tail

    def remove_node(self, node: ListNode):
        if node == self.head and node.next == self.tail:
            self.head = self.tail
            self.head.next = self.tail
            self.head.prev = self.tail
            self.tail.next = self.head
            self.tail.prev = self.head
        elif node == self.tail and node.next == self.head:
            self.tail = self.head
            self.tail.prev = self.head
            self.tail.next = self.head
            self.head.next = self.tail
            self.head.prev = self.tail
        elif node == self.head:
            node_next = node.next
            self.head = node_next
            self.head.prev = self.tail
            self.tail.next = self.head
        elif node == self.tail:
            node_prev = node.prev
            self.tail = node_prev
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            prev_temp = node.prev
            next_temp = node.next
            prev_temp.next = next_temp
            next_temp.prev = prev_temp

    def put(self, key: int, value: int) -> None:
        # implement node
        node = ListNode(key, value)
        if len(self.dict.keys()) == self.capacity and key not in self.dict.keys():
            self.dict.pop(self.tail.key)
            self.remove()
        elif key in self.dict.keys():
            self.remove_node(self.dict[key])
        self.add(node=node)
        self.dict[key] = node

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
    expected_output = [None,-1,None,-1,None,None,2,6]
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

