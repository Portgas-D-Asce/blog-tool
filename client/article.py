import os
import json

from client.client import Client


class ArticleClient:
    def __init__(self):
        self.client = Client()

    def add(self, data, files):
        method = "POST"
        url = "/v1/articles"
        return self.client.request_with_file(method, url, files, data)
    
    def query_by_id(self, id):
        method = "GET"
        url = "/v1/articles/%s" % id
        return self.client.request(method, url)
    
    def query_by_name(self, name):
        method = "GET"
        url = "/v1/articles?article_name=%s" % name
        return self.client.request(method, url)
    
    def query_by_tid(self, tid):
        method = "GET"
        url = "/v1/articles?tag_id=%s" % tid
        return self.client.request(method, url)
    
    def query_by_cid(self, cid, recursively):
        method = "GET"
        url = "/v1/articles?category_id=%s&%s" % (cid, recursively)
        return self.client.request(method, url)
    
    def query_all(self):
        method = "GET"
        url = "/v1/articles"
        return self.client.request(method, url)

    def update(self, id, data, files):
        method = "PUT"
        url = "/v1/articles/%s" % id
        return self.client.request_with_file(method, url, files, data)
    
    def delete_by_id(self, id):
        method = "DELETE"
        url = "/v1/articles/%s" % id
        return self.client.request(method, url)
    
    def delete_by_tid(self, tid):
        method = "DELETE"
        url = "/v1/articles?tag_id=%s" % tid
        return self.client.request(method, url)
    
    def delete_by_cid(self, cid, recursively):
        method = "DELETE"
        url = "/v1/articles?category_id=%s&%s" % (cid, recursively)
        return self.client.request(method, url)
    
    def delete_all(self):
        method = "DELETE"
        url = "/v1/articles"
        return self.client.request(method, url)
    
    @staticmethod
    def _find_article_by_name(name):
        dir = "../note/%s" % name
        meta_path = "%s/meta.md" % dir
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
    def list(args):
        print("article list: %s" % args)
        client = ArticleClient()
        if args.name:
            client.query_by_name(args.name)
        elif args.cid:
            client.query_by_cid(args.cid, args.recursively)
        elif args.tid:
            client.query_by_tid(args.tid)
        else:
            client.query_all()
    
    @staticmethod
    def modify(args):
        print("article modify: %s" % args)
        client = ArticleClient()
        data, files = client._find_article_by_name(args.name)
        _, article = client.query_by_name(args.name)
        client.update(article.get("id"), data, files)

    @staticmethod
    def publish(args):
        print("article publish: %s" % args)
        client = ArticleClient()
        data, files = client._find_article_by_name(args.name)
        client.add(data, files)

    @staticmethod
    def unpublish(args):
        print("article unpublish: %s" % args)
        client = ArticleClient()
        if args.name:
            _, article = client.query_by_name(args.name)
            client.delete_by_id(article.get("id"))
        elif args.cid:
            client.delete_by_cid(args.cid, args.recursively)
        elif args.tid:
            client.delete_by_tid(args.tid)
        else:
            client.delete_all()
