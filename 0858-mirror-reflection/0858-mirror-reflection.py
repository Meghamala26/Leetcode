class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if p==q:
            return 1
        up, right=True, False
        height=q
        while True:
            
            if height+q==p:
                if up and right:
                    return 1
                elif up and not right:
                    return 2
                else:
                    return 0
                
            elif height+q<p:
                height+=q
                right = not right
                
            else:
                height+=q-p
                right = not right
                up = not up
                

        