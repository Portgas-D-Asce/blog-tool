class Article:
    def __init__(self, name, description, cid, tags):
        self.name = name
        self.description = description
        self.cid = cid
        self.tags = tags
        self.client = None
    
    def delete(self):
        url = "xxx"
        self.client.request("DELETE", url)
