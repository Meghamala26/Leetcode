from sortedcontainers import SortedDict
class Leaderboard:

    def __init__(self):
        
        self.leaderboardMap={}
        self.scoresMap=SortedDict()
        
    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.leaderboardMap:
            curScore = self.leaderboardMap[playerId]
            self.leaderboardMap[playerId]+=score
            self.scoresMap[-curScore]-=1
            if self.scoresMap[-curScore]==0:
                del self.scoresMap[-curScore]
            newScore= self.leaderboardMap[playerId]
            if -newScore in self.scoresMap:
                self.scoresMap[-newScore]+=1
            else:
                self.scoresMap[-newScore]=1
        else:
            self.leaderboardMap[playerId]=score
            if -score in self.scoresMap:
                self.scoresMap[-score]+=1
            else:
                self.scoresMap[-score]=1
                 
            
    def top(self, K: int) -> int:
        totalSum=0
        count=0
        for key, val in self.scoresMap.items():
            for i in range(val):
                totalSum+=-key
                count+=1
                if count==K:
                    break
            if count==K:
                break
                    
        return totalSum
            
                
        
        
        
       
        
        

    def reset(self, playerId: int) -> None:
        curScore = self.leaderboardMap[playerId]
        self.scoresMap[-curScore]-=1
        del self.leaderboardMap[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)