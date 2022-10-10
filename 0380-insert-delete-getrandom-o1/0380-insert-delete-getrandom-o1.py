import random
class RandomizedSet:

    def __init__(self):
        self.setMap=set()
        

    def insert(self, val: int) -> bool:
        if val not in self.setMap:
            self.setMap.add(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.setMap:
            self.setMap.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        num  =  random.sample(self.setMap, 1)
        return num[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()