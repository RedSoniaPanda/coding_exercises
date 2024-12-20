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
                    max = None
                    pop_key = None
                    for ev_key, ev_value in self.lru_cache.items():
                        if max is None:
                            max = ev_value[1]
                            pop_key = ev_key
                        if max < ev_value[1]:
                            max = ev_value[1]
                            pop_key = ev_key
                    self.lru_cache.pop(pop_key)
                    priority = 0
                    # increase priority for all other items
                for lru_key in self.lru_cache.keys():
                    self.lru_cache[lru_key] = (self.lru_cache[lru_key][0], self.lru_cache[lru_key][1] + 1)
            else:
                if len(self.lru_cache.keys()) == 0:
                    priority = 0
                else:
                    max = None
                    for ev_key, ev_value in self.lru_cache.items():
                        if max is None:
                            max = ev_value[1]
                        if max < ev_value[1]:
                            max = ev_value[1]
                    priority = max + 1
        else:
            # Decrease priority instead? - Set to 0 and decrease other priority
            max = None
            # pop_key = None
            for ev_key, ev_value in self.lru_cache.items():
                if max is None:
                    max = ev_value[1]
                    # pop_key = ev_key
                if max < ev_value[1]:
                    max = ev_value[1]
                    # pop_key = ev_key
            priority = max + 1 if ev_key != key else self.lru_cache[key][1]
        self.lru_cache[key] = (value, priority)


if __name__ == "__main__":
    lru_cache = LRUCache(2)
    get_responses = []

    # One test example from leet code
    # lru_cache.put(1, 1)
    # lru_cache.put(2, 2)
    # get_responses.append(lru_cache.get(1))
    # lru_cache.put(3, 3)
    # get_responses.append(lru_cache.get(2))
    # lru_cache.put(4, 4)
    # get_responses.append(lru_cache.get(1))
    # get_responses.append(lru_cache.get(3))
    # get_responses.append(lru_cache.get(4))

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
    lru_cache.put(2, 1)
    lru_cache.put(2, 2)
    lru_cache.get(2)
    lru_cache.put(1, 1)
    lru_cache.put(4, 1)
    lru_cache.get(2)


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
