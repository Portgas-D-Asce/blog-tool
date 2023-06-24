import json
from client.client import Client


class TagClient:
    def __init__(self):
        self.client = Client()
        self.work_file = "tag.json"

    def add(self, tag):
        method = "POST"
        url = "/v1/tags"
        self.client.request(method, url, json.dumps(tag))
   
    def delete(self, id):
        method = "DELETE"
        url = "/v1/tags/%s" % id
        self.client.request(method, url)
    
    def query(self, id):
        method = "GET"
        url = "/v1/tags/%s" % id
        self.client.request(method, url)
    
    def update(self, id, tag):
        method = "PUT"
        url = "/v1/tags/%s" % id
        self.client.request(method, url, json.dumps(tag))
    
    @staticmethod
    def _find_tag_by_id(id):
        tags_path = "/Users/pk/Note/tags.json"
        with open(tags_path) as fp:
            tags = json.load(fp)

        res = None
        for tag in tags:
            if tag.get("id") == id:
                res = tag
                break
        
        return res
    
    @staticmethod
    def callback(args):
        print("tag: %s %s" % (args.operate, args.tag_id))
        tag_client = TagClient()
        op = args.operate
        id = args.tag_id
        if op == "add":
            tag = TagClient._find_tag_by_id(id)
            
            if tag == None:
                print("can't find tag with id: %s" % id)
                return
            
            print("find tag with id %s: %s" % (id, tag))
            tag_client.add(tag)
        elif op == "delete":
            tag_client.delete(id)
        elif op == "query":
            tag_client.query(id)
        elif op == "update":
            tag = TagClient._find_tag_by_id(id)

            if tag == None:
                print("can't find tag with id: %s" % id)
                return
            
            print("find tag with id %s: %s" % (id, tag))
            tag_client.update(id, tag)
        else:
            print("error operate")
