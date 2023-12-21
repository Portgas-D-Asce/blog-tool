import json
from client.client import Client


class CategoryClient():
    def __init__(self):
        self.client = Client()
    
    def add(self, pid, categories):
        method = "POST"
        url = "/v1/categories?pid=%s" % pid
        self.client.request(method, url, json.dumps(categories))
    
    def delete(self, id, recursively):
        method = "DELETE"
        url = "/v1/categories/%s?recursively=%s" % (id, recursively)
        self.client.request(method, url)
    
    def query(self, id, recursively):
        method = "GET"
        url = "/v1/categories/%s?recursively=%s" % (id, recursively)
        return self.client.request(method, url)

    @staticmethod
    def list(args):
        print("category: %s" % (args))
        client = CategoryClient()
        client.query(args.id, args.recursively)

    @staticmethod
    def create(args):
        print("category create: %s" % args)
        client = CategoryClient()
        client.add(args.pid, json.loads(args.categories))

    @staticmethod
    def destory(args):
        print("category destory: %s" % args)
        client = CategoryClient()
        client.delete(args.id, args.recursively)
