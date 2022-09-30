class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_map={}
        
        for x in strs:
            t=tuple(sorted(x))
            if t not in words_map:
                words_map[t]=[x]
            else:
                words_map[t].append(x)
        res=[]       
        for val in words_map.values():
            res.append(val)
            
        return res
            
        