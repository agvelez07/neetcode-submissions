class Url:
    def __init__(self, url=None):
        self.url  = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur   = Url(homepage)

    def visit(self, url: str) -> None:
        new_visit = Url(url)

        self.cur.next = new_visit
        new_visit.prev = self.cur

        self.cur = new_visit

    def back(self, steps: int) -> str:
        if self.cur == None:
            return
 
        cur = self.cur

        while cur.prev and steps > 0:
            if self.cur.prev == None:
                break
            cur = cur.prev
            steps -= 1

        self.cur = cur
        if cur:
            return cur.url
        else:
            return 'No History'


    def forward(self, steps: int) -> str:
        if self.cur == None:
            return
        cur = self.cur
         
        while cur.next and steps > 0:
            if self.cur.next == None:
                break
            cur = cur.next 
            steps -= 1
        self.cur = cur

        if cur:
            return cur.url

        else:
            return 'No History'




# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
 