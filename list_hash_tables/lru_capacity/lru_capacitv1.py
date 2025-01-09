class LRUCache:

    def __init__(self, capacity: int):
        # self.lru = None
        self.capacity = capacity
        self.lru_cache = {}

    def get(self, key: int) -> int:
        if key in self.lru_cache.keys():
            return self.lru_cache[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        priority = 0
        if key not in self.lru_cache.keys():
            # Check for capacity before adding
            if len(self.lru_cache.keys()) == self.capacity:
                # evict
                if self.capacity == 1:
                    lru_keys = [l_key for l_key in self.lru_cache.keys()]
                    self.lru_cache.pop(lru_keys[0])
                else:
                    max, pop_key = self.get_max_priority_and_key()
                    self.lru_cache.pop(pop_key)
                    priority = 0
                    # increase priority for all other items
                self.incr_priority_all_except_one(key)
            else:
                priority = 0
                if len(self.lru_cache.keys()) != 0:
                    for lru_key, val in self.lru_cache.items():
                        self.lru_cache[lru_key] = (val[0], val[1] + 1)
        else:
            if len(self.lru_cache.keys()) == 1:
                priority = 0
            else:
                priority = self.lru_cache[key][1] - 1  # Priority should decrease
            self.incr_priority_all_except_one(key)
        self.lru_cache[key] = (value, priority)

    def incr_priority_all_except_one(self, key):
        for lru_key, val in self.lru_cache.items():
            if lru_key != key:
                self.lru_cache[lru_key] = (val[0], val[1] + 1)

    def get_max_priority_and_key(self):
        max = None
        pop_key = None
        for ev_key, ev_value in self.lru_cache.items():
            if max is None:
                max = ev_value[1]
                pop_key = ev_key
            if max < ev_value[1]:
                max = ev_value[1]
                pop_key = ev_key
        return max, pop_key

    def get_max_method(self):
        max = None
        for ev_key, ev_value in self.lru_cache.items():
            if max is None:
                max = ev_value[1]
            if max < ev_value[1]:
                max = ev_value[1]
        return max


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

    # A second example from leet code
    # lru_cache.put(2, 1)
    # print(lru_cache.get(2))

    # A third example
    # lru_cache.put(2, 1)
    # lru_cache.get(2)
    # lru_cache.put(3, 2)
    # lru_cache.get(2)
    # lru_cache.get(3)

    # A fourth example
    # get_responses.append(lru_cache.put(2, 1))
    # get_responses.append(lru_cache.put(2, 2))
    # get_responses.append(lru_cache.get(2))
    # get_responses.append(lru_cache.put(1, 1))
    # get_responses.append(lru_cache.put(4, 1))
    # get_responses.append(lru_cache.get(2))
    # print(get_responses)
    # print([None,None,None,2,None,None,-1])
    # print([None,None,None,2,None,None,-1] == get_responses)

    # what about a case where something's updated at max cap
    # lru_cache.put(1, 1)  # expect p0
    # lru_cache.put(2, 1)  # expect p1
    # lru_cache.put(2, 3)

    print(lru_cache.lru_cache)
    # print(get_responses)

    # lru_cache.put(1, 1)
    # print(lru_cache.get(2))  # item not in list
    # lru_cache.put(2, 1)
    # print(lru_cache.get(1))  # item  in list
