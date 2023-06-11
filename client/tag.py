from client.client import Client


class TagClient:
    def __init__(self):
        self.client = Client()

    # todo
    def add(self, tag):
        method = "POST"
        url = "/v1/tag"
        self.client.request(method, url, tag)
    
    def delete(self, id):
        method = "DELETE"
        url = "/v1/tag/%s" % id
        self.client.request(method, url)
    
    def query(self, id):
        method = "GET"
        url = "/v1/tag/%s" % id
        self.client.request(method, url)
    
    # todo
    def update(self, id, tag):
        method = "PUT"
        url = "/v1/tag/%s" % id
        self.client.request(method, url, tag)
    
    @staticmethod
    def callback(args):
        print("tag: %s %s" % (args.operate, args.tag_id))
        tag_client = TagClient()
        op = args.operate
        id = args.tag_id
        if op == "add":
            tag = '{"name": "tool_test", "description": "tool_desc"}'
            # tag_client.add(tag)
        elif op == "delete":
            tag_client.delete(id)
        elif op == "query":
            tag_client.query(id)
        elif op == "update":
            tag = '{"id":"1", "name": "tool_test", "description": "tool_desc"}'
            # tag_client.update(id, tag)
        else:
            print("error operate")
