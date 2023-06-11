from client.client import Client


class ArticleClient:
    def __init__(self):
        self.client = Client()

    def add(self, article):
        method = "POST"
        url = "/v1/article"
        self.client.request(method, url, article)
    
    def delete(self, id):
        method = "DELETE"
        url = "/v1/article/%s" % id
        self.client.request(method, url)
    
    def query(self, id):
        method = "GET"
        url = "/v1/article?category_id=104&tag_id=3"
        self.client.request(method, url)
    
    def update(self, id, article):
        method = "PUT"
        url = "/v1/article/%s" % id
        self.client.request(method, url, article)
    
    @staticmethod
    def callback(args):
        op = args.operate
        name = args.article_name
        print("tag: %s %s" % (op, id))
        article_client = ArticleClient()
        if op == "add":
            xxx = '{"name": "tool_test", "description": "tool_desc"}'
            article_client.add(xxx)
        elif op == "delete":
            article_client.delete(name)
        elif op == "query":
            article_client.query(name)
        elif op == "update":
            xxx = '{"id":"1", "name": "tool_test", "description": "tool_desc"}'
            article_client.update(xxx)
        else:
            print("error operate")

    

