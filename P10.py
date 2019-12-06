import math
import sys
import threading
from urllib.request import Request, urlopen

class Downloader:
    def __init__ (self, url):
        self.url = url;
        self.size = int(urlopen(Request(url)).info()['Content-Length'])
    
    def download (self, name, n):
        with open(name, "w") as f:
            f.write("\0"*self.size)
        shift = math.ceil(self.size/n)
        start = -shift
        threades = []
        while True:
            start += shift
            end = start+shift
            if end > self.size: end = self.size
            t = threading.Thread(target=self.get_content, args=[name, start, end])
            t.start()
            threades.append(t)
            if end == self.size: break

        for t in threades:
            t.join()

    def get_content (self, name, start, end):
        req = Request(self.url)
        req.add_header('Range', 'bytes='+str(start)+'-'+str(end))
        res = urlopen(req).read()
        with open(name, "rb+") as fw:
            fw.seek(start,0)
            fw.write(bytearray(res))

if __name__ == "__main__":
    f1 = Downloader("https://images.unsplash.com/photo-1535498730771-e735b998cd64?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80")
    f1.download("res.jpg", 10)
    print("Downloaded!")
