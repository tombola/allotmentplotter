from django.core.management.base import BaseCommand, CommandError

from urllib.request import Request, urlopen
import pandas as pd
from rich import print

SITEMAP_URL = "https://vitalseeds.co.uk/product-sitemap.xml"


class Command(BaseCommand):
    # help = ""

    # def add_arguments(self, parser):
    # Positional arguments
    # parser.add_argument('ids', nargs='+', type=int)

    # Named (optional) arguments
    # parser.add_argument(
    #     '--verbose',
    #     action='store_true',
    #     # help=""
    # )

    def user_agent_request(self, url):
        req = Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
        )
        return urlopen(req).read()

    def get_product_urls(self):
        sitemap = self.user_agent_request(SITEMAP_URL)
        df = pd.read_xml(sitemap)
        products = df[df["loc"].str.contains("/product/")]
        return list(products["loc"])

    def get_product_details(self, url):
        product_page = self.user_agent_request(url)
        dfs = pd.read_html(product_page)
        print(url)
        print(dfs)
        # oh dear, the sow/transplant/harvest are css styles

    def handle(self, *args, **options):
        product_urls = self.get_product_urls()
        # for product_page in product_urls:
        self.get_product_details(product_urls[3])

        # self.stdout.write(self.style.SUCCESS('Success for id "%s"' % id))
        # raise CommandError("message")
