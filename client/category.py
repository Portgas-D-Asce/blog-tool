import json
import queue
from client.client import Client


class CategoryClient():
    def __init__(self):
        self.client = Client()
    
    def add(self, categories):
        method = "POST"
        url = "/v1/categories"
        self.client.request(method, url, json.dumps(categories))
    
    def delete(self, id):
        method = "DELETE"
        url = "/v1/categories/%s?recursion=true" % id
        self.client.request(method, url)
    
    def query(self, id):
        method = "GET"
        url = "/v1/categories/%s?recursion=true" % id
        self.client.request(method, url)
    
    def update(self, id, category):
        print("category update to be achieved")
        # method = "PUT"
        # url = "/v1/categories/%s" % id
        # self.client.request(method, url, category)
        
    @staticmethod
    def _find_category_by_id(id):
        categories_path = "/Users/pk/Note/categories.json"
        with open(categories_path) as fp:
            root = json.load(fp)

        res = None
        que = queue.Queue()
        que.put(root)
        while not que.empty():
            category = que.get()
            if category.get("id") == id:
                res = category
                break
            for item in category.get("children", []):
                que.put(item)
        
        return res

    @staticmethod
    def callback(args):
        print("category: %s %s" % (args.operate, args.category_id))
        category_client = CategoryClient()
        op = args.operate
        id = args.category_id
        if op == "add":
            category = CategoryClient._find_category_by_id(id)

            if category == None:
                print("can't find a category with id: %s" % id)
                return

            print("find a category with id %s: %s" % (id, category))
            category_client.add(category)
        elif op == "delete":
            category_client.delete(id)
        elif op == "query":
            category_client.query(id)
        elif op == "update":
            category = CategoryClient._find_category_by_id(id)

            if category == None:
                print("can't find a category with id: %s" % id)
                return

            print("find a category with id %s: %s" % (id, category))
            category_client.update(id, category)
        else:
            print("error operate")