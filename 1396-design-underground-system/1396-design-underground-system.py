class UndergroundSystem:

    def __init__(self):
    
        self.personCheckIn={}
        self.stationAvgTime={}
    

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        self.personCheckIn[id]=[stationName, t]
            

    
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
       
        startStation=self.personCheckIn[id][0]
        startTime=self.personCheckIn[id][1]
        key= startStation + ',' + stationName
        if key in self.stationAvgTime:
        
            val=self.stationAvgTime[key]
            totalSum=val[0]
            count=val[1]
            self.stationAvgTime[key]=[totalSum+t-startTime, count+1]
        else:
            self.stationAvgTime[key]=[t-startTime,1]
            
        
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key= startStation + ',' + endStation
        
        val= self.stationAvgTime[key]
        return val[0]/val[1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)