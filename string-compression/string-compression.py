class Solution:
    def compress(self, chars: List[str]) -> int:
        n=len(chars)
        if n==1:
            return 1
        
        curChar=chars[0]
        curLen=1
        
        i=0
        while(i<n):
            if i!=n-1 and chars[i+1]==curChar:
                curLen+=1
            if i==n-1 or chars[i+1]!=curChar:
                
                if curLen==1:
                    chars.append(curChar)
                elif curLen>1 and curLen<=9:
                    chars.append(curChar)
                    chars.append(str(curLen))
                else:
                    chars.append(curChar)
                    countList=list(str(curLen))
                    for x in countList:
                        chars.append(x)
                    
                curChar=chars[i+1]
                curLen=1
            i+=1
                    
        for i in range(n):
            chars.pop(0)
        return len(chars)
        