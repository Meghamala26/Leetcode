class Solution:
    def reverse(self, s, start, end):
            while(start<end):
                temp=s[start]
                s[start]=s[end]
                s[end]=temp
                start+=1
                end-=1
                
    def reverseWord(self, s):
        start=0
        for i in range(len(s)):
            if s[i]==' ':
                self.reverse(s, start, i-1)
                
            elif i==len(s)-1:
                self.reverse(s,start, i)
            else:
                continue
            
            start=i+1

                
                
                
                
                
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
  
        self.reverse(s,0,len(s)-1)
        self.reverseWord(s)
        
        
                    
        
        