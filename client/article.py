import os
import json

from client.client import Client


class ArticleClient:
    def __init__(self):
        self.client = Client()
        self.work_dir = "note"

    def add(self, data, files):
        method = "POST"
        url = "/v1/articles"
        return self.client.request_with_file(method, url, files, data)
    
    def delete(self, id):
        method = "DELETE"
        url = "/v1/articles/%s" % id 
        return self.client.request(method, url)
    
    def query_by_name(self, name):
        method = "GET"
        url = "/v1/articles?article_name=%s" % name
        return self.client.request(method, url)

    def update(self, id, data, files):
        method = "PUT"
        url = "/v1/articles/%s" % id
        return self.client.request_with_file(method, url, files, data)
    
    @staticmethod
    def _find_article_by_name(name):
        dir = "/Users/pk/Note/%s" % name

        meta_path = "%s/meta.json" % dir
        print(meta_path)
        with open(meta_path) as fp:
            data = json.load(fp)

        name += ".md"
        article_path = "%s/%s" % (dir, name)
        files = [('article', (name, open(article_path, 'rb'), 'application/octet-stream'))]

        image_dir = "%s/images" % dir
        image_names = os.listdir(image_dir)
        for image_name in image_names:
            if image_name.startswith("."):
                continue
            image_path = "%s/%s" % (image_dir, image_name)
            files.append(('images', (image_name, open(image_path, 'rb'), 'application/octet-stream')))

        return data, files

    @staticmethod
    def callback(args):
        op = args.operate
        name = args.article_name
        print("article: %s %s" % (op, id))
        article_client = ArticleClient()
        if op == "add":
            data, files = ArticleClient._find_article_by_name(name)
            article_client.add(data, files)
        elif op == "delete":
            _, data = article_client.query_by_name(name)
            article_client.delete(data.get("id"))
        elif op == "query":
            _, data = article_client.query_by_name(name)
        elif op == "update":
            data, files = ArticleClient._find_article_by_name(name)
            _, articles = article_client.query_by_name(name)
            article_client.update(articles.get("id"), data, files)
        else:
            print("error operate")

    

