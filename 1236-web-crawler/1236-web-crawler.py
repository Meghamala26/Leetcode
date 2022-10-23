# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        
        
        def getHostName(url):
            hostname=''
            i=0
            while(i<len(url)):
                hostname+=url[i]
                i+=1
                if hostname=='http://':
                    break
                
            hostname=''
            while(i<len(url)):
                if url[i] == '.' or url[i]=='-' or url[i] in "abcdefghijklmnopqrstuvwxyz" or url[i] in "0123456789":
                    hostname+=url[i]
                else:
                    break
                i+=1
            return hostname
                
        visited = set()
        q = [startUrl]
        visited.add(startUrl)
        res = []
        hostname=getHostName(startUrl)
        
        while q:
            url = q.pop(0)
            res.append(url)
            
            for n in htmlParser.getUrls(url):
                if getHostName(n) == hostname and n not in visited:
                    q.append(n)
                    visited.add(n)
        return res
            
