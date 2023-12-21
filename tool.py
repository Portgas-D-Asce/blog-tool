import argparse


from client.category import CategoryClient
from client.tag import TagClient
from client.article import ArticleClient


def main():
    parser = argparse.ArgumentParser(prog="blog_tool", description="tool for blog", epilog="end of the file")
    sub_parsers = parser.add_subparsers(title="subcommands", required=True)
    

    parser_category = sub_parsers.add_parser("category", help="subcommand category", description="subcommand category")
    sub_parsers_category = parser_category.add_subparsers(title="category subcommands", required = True)

    parser_category_list = sub_parsers_category.add_parser("list", help="list category tree", description="list category tree")
    parser_category_list.add_argument("--id", type=int, help="categoriey id", dest="id", required=True)
    parser_category_list.add_argument("-r", action="store_true", help="recursively", dest="recursively")
    parser_category_list.set_defaults(func=CategoryClient.list)

    parser_category_create = sub_parsers_category.add_parser("create", help="create category tree", description="create category tree")
    parser_category_create.add_argument("--pid", type=int, help="parent's id", dest="pid", required=True)
    parser_category_create.add_argument("--categories", help="categories", dest="categories", required=True)
    parser_category_create.set_defaults(func=CategoryClient.create)

    parser_category_destory = sub_parsers_category.add_parser("destory", help="destory categories", description="destory categories")
    parser_category_destory.add_argument("--id", type=int, help="categoriey id", dest="id", required=True)
    parser_category_destory.add_argument("-r", action="store_true", help="recursively", dest="recursively")
    parser_category_destory.set_defaults(func=CategoryClient.destory)


    parser_tag = sub_parsers.add_parser("tag", help="subcommand tag", description="subcommand tag")
    sub_parsers_tag = parser_tag.add_subparsers(title="tag subcommands", required = True)

    parser_tag_list = sub_parsers_tag.add_parser("list", help="list tags", description="list tags")
    parser_tag_list.add_argument("--id", help="tag id", dest="id", required=True)
    parser_tag_list.set_defaults(func=TagClient.list)

    parser_tag_create = sub_parsers_tag.add_parser("create", help="create tags", description="create tags")
    parser_tag_create.add_argument("--tags", help="tags", dest="tags", required=True)
    parser_tag_create.set_defaults(func=TagClient.create)

    parser_tag_update = sub_parsers_tag.add_parser("modify", help="update tag", description="update tag")
    parser_tag_update.add_argument("--id", help="tag id", dest="id", required=True)
    parser_tag_update.add_argument("--tag", help="tag", dest="tag", required=True)
    parser_tag_update.set_defaults(func=TagClient.modify)

    parser_tag_destory = sub_parsers_tag.add_parser("destory", help="destory tags", description="destory tags")
    parser_tag_destory.add_argument("--id", help="tag id", dest="id", required=True)
    parser_tag_destory.set_defaults(func=TagClient.destory)


    parser_article = sub_parsers.add_parser("article", help="subcommand article", description="subcommand artice")
    sub_parsers_article = parser_article.add_subparsers(title="tag subcommands", required = True)

    parser_article_list = sub_parsers_article.add_parser("list", help="list articles", description="list articles")
    parser_article_list.add_argument("--name", help="article name", dest="name")
    parser_article_list.add_argument("--cid", help="category id", dest="cid")
    parser_article_list.add_argument("-r", action="store_true", help="category recursively", dest="recursively")
    parser_article_list.add_argument("--tid", help="tag id", dest="tid")
    parser_article_list.set_defaults(func=ArticleClient.list)

    parser_article_publish = sub_parsers_article.add_parser("publish", help="publish article", description="publish article")
    parser_article_publish.add_argument("--name", help="article name", dest="name", required=True)
    parser_article_publish.set_defaults(func=ArticleClient.publish)

    parser_article_modify = sub_parsers_article.add_parser("modify", help="modify article", description="modify article")
    parser_article_modify.add_argument("--name", help="article name", dest="name", required=True)
    parser_article_modify.set_defaults(func=ArticleClient.modify)

    parser_article_unpublish = sub_parsers_article.add_parser("unpublish", help="delete articles", description="delete articles")
    parser_article_unpublish.add_argument("--name", help="article name", dest="name")
    parser_article_unpublish.add_argument("--cid", help="category id", dest="cid")
    parser_article_unpublish.add_argument("-r", action="store_true", help="category recursively", dest="recursively")
    parser_article_unpublish.add_argument("--tid", help="tag id", dest="tid")
    parser_article_unpublish.set_defaults(func=ArticleClient.unpublish)

    
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
