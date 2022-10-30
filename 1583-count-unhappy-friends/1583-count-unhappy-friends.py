class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pairsMap={}
        for x in pairs:
            pairsMap[x[0]]=x[1]
            pairsMap[x[1]]=x[0]
        
        preferencesMap={}
        for person,prefer in enumerate(preferences):
            preferencesMap[person]=[]
            for like in prefer:
                if like!=pairsMap[person]:
                    preferencesMap[person].append(like)
                else:
                    break
        unhappy=set()
        
        print(preferencesMap)
        
        for person in pairsMap.keys():
            print(person)
            
            for like in preferencesMap[person]:
                if person in preferencesMap[like]:
                    unhappy.add(like)
                    unhappy.add(person)
                    break
                        
        #print(unhappy)
        return len(unhappy)
        
        
                    
        