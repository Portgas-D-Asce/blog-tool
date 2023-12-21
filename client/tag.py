import json
from client.client import Client


class TagClient:
    def __init__(self):
        self.client = Client()

    def add(self, tag):
        method = "POST"
        url = "/v1/tags"
        return self.client.request(method, url, json.dumps(tag))
   
    def delete(self, id):
        method = "DELETE"
        url = "/v1/tags"
        if id != "all":
            url += "/%s" % id
        return self.client.request(method, url)
    
    def query(self, id):
        method = "GET"
        url = "/v1/tags"
        if id != "all":
            url += "/%s" % id
        return self.client.request(method, url)
    
    def update(self, id, tag):
        method = "PUT"
        url = "/v1/tags/%s" % id
        return self.client.request(method, url, json.dumps(tag))
    
    @staticmethod
    def list(args):
        print("tag list: %s" % args)
        client = TagClient()
        client.query(args.id)

    @staticmethod
    def create(args):
        print("tag create: %s" % args)
        client = TagClient()
        client.add(json.loads(args.tags))

    @staticmethod
    def modify(args):
        print("tag update: %s" % args)
        client = TagClient()
        client.update(args.id, json.loads(args.tag))

    @staticmethod
    def destory(args):
        print("tag destory: %s" % args)
        client = TagClient()
        client.delete(args.id)
        
