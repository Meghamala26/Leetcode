class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courseMap={i:[] for i in range(numCourses)}
        
        for (a,b) in prerequisites:
            courseMap[a].append(b)
            
        def checkCycle(courseNo,visited):
            if courseMap[courseNo]==[]:
                return True
            if courseNo in visited:
                return False
            
            visited.add(courseNo)
            
            for c in courseMap[courseNo]:
                if not checkCycle(c,visited):
                    return False
            visited.pop()
            courseMap[courseNo]=[]
            return True
            
        
        
        for i in range(numCourses):
            if not checkCycle(i,set()):
                return False
        return True
                
        