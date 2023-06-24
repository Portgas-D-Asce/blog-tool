from client.client import Client


class ArticleClient:
    def __init__(self):
        self.client = Client()
        self.work_dir = "note"

    def add(self, article):
        method = "POST"
        url = "/v1/articles"
        data = {
            "cid": 3,
            "tags": "1,2,3,4,5,6,7,8",
            "description": "python tool test"
        }
        files=[('file',('深入理解变参函数.md',open('Note/C&C++/深入理解变参函数/深入理解变参函数.md','rb'),'application/octet-stream'))]
        self.client.request_with_file(method, url, files, data)
    
    def delete_by_id(self, id):
        method = "DELETE"
        url = "/v1/articles/%s" % id
        self.client.request(method, url)

    def delete_by_name(self, name):
        method = "DELETE"
        url = "/v1/articles?article_name=%s" % name 
        self.client.request(method, url)
    
    def query_all(self):
        method = "GET"
        url = "/v1/articles"
        self.client.request(method, url)
    
    def query_by_id(self, id):
        method = "GET"
        url = "/v1/articles/%s" % id
        self.client.request(method, url)
    
    def query_by_name(self, name):
        method = "GET"
        url = "/v1/articles?article_name=%s" % name
        self.client.request(method, url)

    def query_by_category_id(self, category_id):
        method = "GET"
        url = "/v1/articles?category_id=%s" % category_id
        self.client.request(method, url)

    def query_by_tag_id(self, tag_id):
        method = "GET"
        url = "/v1/articles?tag_id=%s" % tag_id
        self.client.request(method, url)

    def update(self, id, article):
        method = "PUT"
        url = "/v1/article/%s" % id
        self.client.request(method, url, article)
    
    @staticmethod
    def callback(args):
        op = args.operate
        name = args.article_name
        print("article: %s %s" % (op, id))
        article_client = ArticleClient()
        if op == "add":
            xxx = '{"name": "tool_test", "description": "tool_desc"}'
            article_client.add(xxx)
        elif op == "delete":
            article_client.delete_by_name(name)
        elif op == "query":
            article_client.query_by_name(name)
        elif op == "update":
            xxx = '{"id":"1", "name": "tool_test", "description": "tool_desc"}'
            article_client.update(xxx)
        else:
            print("error operate")

    

