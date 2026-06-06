class MyHashMap(object):

    def __init__(self):
        self.myhashmap = {}
    def put(self, key, value):
        self.myhashmap[key] = value
    def get(self, key):
        if key in self.myhashmap:
            return self.myhashmap[key]
        else: return -1
    def remove(self, key):
        if key in self.myhashmap:
            self.myhashmap.pop(key)
        else: pass
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)