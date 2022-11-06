from sortedcontainers import SortedDict
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo=collections.defaultdict(lambda x : 0)
        def getPower(num):
            if num==1:
                return 0
            power=0
            while(num!=1):
                if num in memo:
                    power+=memo[num]
                    return power
                
                if num%2==0:
                    num=num/2
                else:
                    num=3*num+1
                power+=1
            
            
            memo[num]=power
            return power
        
        powerMap=SortedDict()
        for num in range(lo,hi+1,1):
            numPower=getPower(num)
            if numPower in powerMap:
                powerMap[numPower].append(num)
            else:
                powerMap[numPower]=[num]
        
        count=0
        for power, numList in powerMap.items():
            if count+len(numList)>=k:
                numList=sorted(numList)
                return numList[k-count-1]
            else:
                count+=len(numList)
            
            
                
            
            
            
            
        