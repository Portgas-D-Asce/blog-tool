from client.client import Client


class CategoryClient():
    def __init__(self):
        self.client = Client()
    
    def add(self, categroy_tree):
        method = "POST"
        url = "/v1/category"
        self.client.request(method, url, categroy_tree)
    
    def delete(self, id):
        print("category add to be achieved.")
        method = "DELETE"
        url = "/v1/category/%s" % id
        self.client.request(method, url)
    
    def query(self, id=0):
        print("category delete to be achieved")
        method = "GET"
        url = "/v1/category/%s?recursion=true" % id
        self.client.request(method, url)
    
    def update(self, id, category_tree):
        print("category delete to be achieved")
        method = "PUT"
        url = "/v1/category/%s" % id
        self.client.request(method, url, category_tree)
        

    @staticmethod
    def callback(args):
        print("category: %s %s" % (args.operate, args.category_id))
        category_client = CategoryClient()
        op = args.operate
        id = args.category_id
        if op == "add":
            category_client.add("xxx")
        elif op == "delete":
            category_client.delete(id)
        elif op == "query":
            category_client.query(id)
        elif op == "update":
            category_client.update(id, "xxx")
        else:
            print("error operate")