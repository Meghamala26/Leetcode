class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s)==1:
            return s
        word=''
        words=[]
        s=s+' '
        for ch in s:
            if ch==' ':
                if word!='':
                    words.append(word)
                    word=''
                else:
                    continue
            else:
                word+=ch
                
        print(words)
        
        res=''
        for i in range(len(words)-1,-1,-1):
            if i==0:
                res+=words[i]
            else: 
                res+=words[i]+' '
        return res
                
            
            
        