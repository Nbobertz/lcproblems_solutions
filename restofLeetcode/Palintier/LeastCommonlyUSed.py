#here we are given a request to build a class that can handle a least commonly used caching system. The idea here is that we are given a requet and if it is in the cache we return it and then move all others acordingly. If the cache is siez 3 and the only 3 requests are 1 then when we get a 2 we pop one out of it.
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)

        self.dic[key] = value
        if len(self.dic) > self.capacity:
            self.dic.popitem(False)