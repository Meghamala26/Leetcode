class FileSystem:

    def __init__(self):
        self.pathMap={}
        
        
    def getParentPath(self,path:str)-> str:
        
        i=len(path)-1
        while(i>=0):
            if path[i]=="/":
                
                break
            i-=1
        
        return path[0:i]
            
        
        
    def createPath(self, path: str, value: int) -> bool:
        if path in self.pathMap:
            return False
        else:
            parentPath=self.getParentPath(path)
            #print(parentPath)
            if parentPath!='' and parentPath not in self.pathMap:
                return False
            else:
                self.pathMap[path]=value
                return True
                
            
        
        

    def get(self, path: str) -> int:
        if path in self.pathMap:
            return self.pathMap[path]
        return -1
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)