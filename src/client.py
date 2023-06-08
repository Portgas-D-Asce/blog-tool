import requests


class Client():
    def __init__(self, base=None):
        # self.base = base
        self.base = "http://localhost:8080/blog/api"
    
    def request(self, method, url, data=None):
        url = self.base + url
        print("url: %s" % url)
        x = requests.request(method=method, url=url, data=data)
        if(x.status_code != 200):
            print("request failed: %s." % x.content)
            return -1, None

        print("request succeeded: %s." % x.content)
        return 0, x.content
        
            