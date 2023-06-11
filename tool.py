import argparse


from client.category import CategoryClient
from client.tag import TagClient
from client.article import ArticleClient


def main():
    parser = argparse.ArgumentParser(prog="blog_tool", description="tool for blog", epilog="end of the file")
    sub_parsers = parser.add_subparsers(title="subcommands", required=True)
    
    parser_category = sub_parsers.add_parser("category", help="sub command category", description="sub command category")
    parser_category.add_argument(
        "--operate", choices=["add", "delete", "query", "update"],
        help="operate type", dest="operate", required=True)
    parser_category.add_argument("category_id", type=int)
    parser_category.set_defaults(func=CategoryClient.callback)

    parser_tag = sub_parsers.add_parser("tag", help="sub command tag", description="sub command tag")
    parser_tag.add_argument(
        "--operate", choices=["add", "delete", "query", "update"],
        help="operate type", dest="operate", required=True)
    parser_tag.add_argument("tag_id", type=int)
    parser_tag.set_defaults(func=TagClient.callback)

    parser_article = sub_parsers.add_parser("article", help="sub command article", description="sub command article")
    parser_article.add_argument(
        "--operate", choices=["add", "delete", "query", "update"],
        help="operate type", dest="operate", required=True)
    parser_article.add_argument("article_name")
    parser_article.set_defaults(func=ArticleClient.callback)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
