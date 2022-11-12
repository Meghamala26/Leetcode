class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        
        if s==goal:
            same=set()
            for x in s:
                if x in same:
                    return True
                same.add(x)
            return False
        
        mismatch=[]
        
        for i in range(len(s)):
            if s[i]!=goal[i]:
                if len(mismatch)>=2:
                    return False
                else:
                    mismatch.append((s[i],goal[i]))
            else:
                continue
                
        if len(mismatch)==2 and mismatch[0][0]==mismatch[1][1] and mismatch[0][1]==mismatch[1][0]:
            return True
        else:
            return False
        
            