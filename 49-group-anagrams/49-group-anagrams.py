class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group={}
        
        for i in range(len(strs)):
            key=''.join(sorted(strs[i]))
            if key not in group:
                group[key] =[strs[i]]
            else:
                group[key].append(strs[i])
                
        res=[]
                
        for key,val in group.items():
            res.append(val)
        
        return res
            
                
            
        