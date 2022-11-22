class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1Map=Counter(nums1)
        nums2Map=Counter(nums2)
        
        if len(nums1)<=len(nums2):
            search=nums2Map
            choose=nums1Map
        else:
            search=nums1Map
            choose=nums2Map
        res=[]    
        for key,val in choose.items():
            if key in search:
                for i in range(min(search[key], val)):
                    res.append(key)
        return res