from random import choice
class RandomizedSet:

    def __init__(self):
        self.setMap={}
        self.setList=[]
        
        

    def insert(self, val: int) -> bool:
        if val not in self.setMap:
            self.setMap[val]=len(self.setList)
            self.setList.append(val)
            return True
        
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.setMap:
            i=self.setMap[val]
            self.setMap[self.setList[-1]]=i
            self.setList[i], self.setList[-1]= self.setList[-1], self.setList[i]
            
            self.setList.pop()
            self.setMap.pop(val) 
            return True
        
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.setList)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()