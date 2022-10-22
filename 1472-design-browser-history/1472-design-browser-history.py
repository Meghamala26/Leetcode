class BrowserHistory:

    def __init__(self, homepage: str):
        self.history=[homepage]
        self.ptr=0

    def visit(self, url: str) -> None:
        self.history=self.history[0:self.ptr+1]
        self.history.append(url)
        self.ptr+=1
        

    def back(self, steps: int) -> str:
        if self.ptr<steps:
            self.ptr=0
            return self.history[0]
        else:
            self.ptr-=steps
            return self.history[self.ptr]
            
            
        
        

    def forward(self, steps: int) -> str:
        n=len(self.history)
        maxSteps=n-self.ptr-1
        
        if steps>maxSteps:
            self.ptr=n-1
            return self.history[self.ptr]
        else:
            self.ptr+=steps
            return self.history[self.ptr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)