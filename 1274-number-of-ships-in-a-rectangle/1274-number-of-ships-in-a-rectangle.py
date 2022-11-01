# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        
        #divide and conquer
        #divide the space into quadrants and check hasShips for each quadrant.                   #Recursively divide and check till returns false
        
        count=[0]
        
        def findCount(bottomLeft,topRight):
            if count[0]==10:
                return
            if bottomLeft.x>topRight.x or bottomLeft.y>topRight.y:
                return
            if not sea.hasShips(topRight,bottomLeft):
                return
            
            if topRight.x==bottomLeft.x and topRight.y==bottomLeft.y:
                count[0]+=1
                return
            
            tx,ty=topRight.x, topRight.y
            bx,by=bottomLeft.x, bottomLeft.y
            halfx=(tx-bx)//2
            halfy=(ty-by)//2
            
            
            findCount(bottomLeft,Point(bx+halfx,by+halfy))
            findCount(Point(bx,by+halfy+1),Point(bx+halfx,ty))
            findCount(Point(bx+halfx+1,by),Point(tx,by+halfy))
            findCount(Point(bx+halfx+1,by+halfy+1),topRight)
            
            return
            
            
        
        
        
        findCount(bottomLeft,topRight)
        return count[0]
        
        
        
        