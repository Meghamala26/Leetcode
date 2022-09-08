class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        letters="abcdefghijklmnopqrstuvwxyz0123456789"
        
        
        i=0
        j=len(s)-1
        
        s=s.lower()
        print(s)
        
        while(i<=j):
            if s[i] not in letters:
                i+=1
                continue
            if s[j] not in letters:
                j-=1
                continue
            
            if s[i] != s[j]:
                print(i)
                print(j)
                return False
            else:
                i+=1
                j-=1
        
        return True
                