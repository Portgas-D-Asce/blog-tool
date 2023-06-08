from client import Client


class Category():
    def __init__(self, id, name, description, children=None):
        self.id = id
        self.name = name
        self.description = description
        self.children = children
        self.client = Client()
    
    def query(self):
        method = "GET"
        url = "/v1/category/0/tree"
        self.client.request(method, url)