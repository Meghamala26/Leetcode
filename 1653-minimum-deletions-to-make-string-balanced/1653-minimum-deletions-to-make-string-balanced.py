class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        numB=0
        delB=0
        
        for ch in s:
            if ch =='a':
                delB=min(numB,delB+1)   
            else:
                numB+=1
                
        return delB
        