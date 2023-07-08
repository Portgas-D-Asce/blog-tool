import json
import requests


class Client():
    def __init__(self, base=None):
        self.base = "https://175.178.25.102:8080/blog/api"
    
    def request(self, method, url, data=None):
        header = {
            "Content-type": "application/json",
            "token": "1234567890"
        }
        url = self.base + url
        print("url: %s" % url)
        x = requests.request(method=method, url=url, data=data, headers=header, verify=False)
        print("status: %s." % x.status_code)
        data = x.content.decode()
        if data != "":
            data = json.loads(data)
        if x.status_code < 200 or x.status_code >= 300:
            print("request failed: %s." % data)
            return -1, data

        print("request succeeded: %s." % data)
        return 0, data

    def request_with_file(self, method, url, files, data=None):
        url = self.base + url
        print("url: %s" % url)
        header = {
            "token": "1234567890"
        }
        x = requests.request(headers=header, method=method, url=url, files=files, data=data, verify=False)
        print("status: %s." % x.status_code)
        data = x.content.decode()
        if data != "":
            data = json.loads(data)
        if x.status_code < 200 or x.status_code >= 300:
            print("request failed: %s." % data)
            return -1, data

        print("request succeeded: %s." % data)
        return 0, data
 