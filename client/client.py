import requests


class Client():
    def __init__(self, base=None):
        # self.base = base
        self.base = "http://localhost:8080/blog/api"
    
    def request(self, method, url, data=None):
        header = {
            "Content-type": "application/json"
        }
        url = self.base + url
        print("url: %s" % url)
        x = requests.request(method=method, url=url, data=data, headers=header)
        if(x.status_code != 200):
            print("request failed: %s." % x.content)
            return -1, None

        print("request succeeded: %s." % x.content.decode())
        return 0, x.content
        
            