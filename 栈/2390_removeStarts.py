class BrowserHistory:

    urls = []
    index = 0

    def __init__(self, homepage: str):
        self.urls.append(homepage)

    def visit(self, url: str) -> None:
        self.index += 1 
        del self.urls[self.index:]
        self.urls.append(url)
        print(url)

    def back(self, steps: int) -> str:
        if steps <= len(self.urls):
            self.index -= steps
        else:
            self.index = 0
        return self.urls[self.index]

    def forward(self, steps: int) -> str:
        if self.index + steps < len(self.urls):
            self.index += steps
        else:
            self.index = len(self.urls) - 1
        return self.urls[self.index]
    
t = BrowserHistory('leetcode.com')
t.visit('google.com')
t.visit('facebook.com')
t.visit('youtube.com')
print(t.back(1))
print(t.back(1))
print(t.forward(1))
t.visit('link')
print(t.forward(2))
print(t.back(2))
print(t.back(7))
