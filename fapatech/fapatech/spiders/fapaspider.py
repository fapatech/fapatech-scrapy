from fapatech.utils.helper import get_company_urls
import scrapy

res = get_company_urls("direnc", "tsoft")
print(res)

class DirencSpider(scrapy.Spider):
    name = "direnc"
    start_urls = get_company_urls(name, "tsoft")

    def parse(self, response):
        for products in response.css('div#productRight'):
            try:
                yield {
                    'name': products.css('h1#productName::text').get(),
                    'brand': products.css('a#productBrandText::text').get(),
                    'stock_code': products.css('span.subprobarcod::text').get(),
                    'price': products.css('span.product-price::text').get(),
                    'price_vat_included': products.css('span.product-price-tl::text').get(),
                }
            except:
                yield {
                    
                }

class RobotistanSpider(scrapy.Spider):
    name = "robotistan"
    start_urls = get_company_urls(name, "tsoft")

    def parse(self, response):
        for products in response.css('div#productRight'):
            try:
                yield {
                    'name': products.css('h1#productName::text').get(),
                    'brand': products.css('a#productBrandText::text').get(),
                    'stock_code': products.css('span.subprobarcod::text').get(),
                    'price': products.css('span.product-price::text').get(),
                    'price_vat_included': products.css('span.product-price-tl::text').get(),
                }
            except:
                yield {
                    
                }