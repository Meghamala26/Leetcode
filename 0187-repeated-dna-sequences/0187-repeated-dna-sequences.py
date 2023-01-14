class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited=set()
        start=0
        output=set()
        k=10
        while(start+k-1<len(s)):
            if s[start:start+k] in visited:
                output.add(s[start:start+k])
            else:
                visited.add(s[start:start+k])
            start+=1

        return output