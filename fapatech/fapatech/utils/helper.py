import requests
import re
from urls import SITEMAPS_LIST

TSOFT_COMPANIES = ("direnc", "robotistan")
INFOTEK_COMPANIES = ("motorobit")


class Parser:

    def __init__(self):
        self.tsoft_xml_pattern = r"(http|https):\/\/www.(\w+).(net|com)\/(.*?).xml"
        self.url_content_pattern = r"<loc>(.*?)<\/loc>"
        self.motorobit_xml_pattern = r"(http|https):\/\/www.(.*?).(com|net)\/xml\/(sitemap_product_[\d+?]).*"

    def sitemap_extractor(self, regex_pattern, companies_list: list, sitemap: str):
        company = re.search(regex_pattern, sitemap).groups()[1]
        if company in companies_list:
            content = requests.get(sitemap).text
            url = re.findall(self.url_content_pattern, content)
            print(url)
        return url


class XMLParser(Parser):

    def __init__(self, sitemaps: list):
        super().__init__()

        self.sitemaps = sitemaps

    def get_sitemaps(self):
        return self.sitemaps

    def show_sitemaps(self):
        print("List sitemaps = ", self.get_sitemaps())

    def xml_extractor(self, ecommerce: str):
        for sitemap in self.get_sitemaps():
            if ecommerce == "tsoft":
                url = self.sitemap_extractor(regex_pattern=self.tsoft_xml_pattern, companies_list=TSOFT_COMPANIES, sitemap=sitemap)

            if ecommerce == "infotek":
                url = self.sitemap_extractor(regex_pattern=self.motorobit_xml_pattern, companies_list=INFOTEK_COMPANIES, sitemap=sitemap)

        return url


class URLParser(Parser):

    def __init__(self):
        super().__init__()

    def url_extractor(self, urls: list):
        url_list = list()

        for url in urls:
            content = requests.get(url).text
            url = self.extractor(content)

            url_list.append(url)

        flat_list = [item for sublist in url_list for item in sublist]

        return flat_list


def get_company_urls(company_name: str, ecommerce: str):
    xml_response = XMLParser(SITEMAPS_LIST).xml_extractor(ecommerce=ecommerce)

    urls = URLParser().url_extractor(xml_response)
    pattern = r"^(http|https):\/\/(www).(.*?).(net|com)\/(.*?)$"
    url_list = list()

    for url in urls:
        company = re.search(pattern, url).groups()[2]

        if company_name == company:
            url_list.append(url)
    return url_list

get_company_urls("motorobit", "infotek")
