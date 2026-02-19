import random
class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val not in self.d:
            self.values.append(val)
            self.d[val] = len(self.d)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.d:
            removed = self.d.pop(val)
            self.values.pop(removed)
            for k,v in self.d.items():
                if v > removed:
                    self.d[k] = v -1
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
if __name__ == "__main__":
    s = RandomizedSet()
    print(s.insert(2),s.insert(2),s.getRandom(),s.values)
    print(s.insert(1),s.remove(2),s.insert(2),s.getRandom(),s.remove(1),s.insert(2),s.getRandom())