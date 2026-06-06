class MyHashSet:

    def __init__(self):
        self.data = set([])
    def add(self, key: int) -> None:
        self.data.add(key)
    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)
        else: None
    def contains(self, key: int) -> bool:
        if key in self.data:
            return True
        else: return False