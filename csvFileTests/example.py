# -*- coding: utf-8 -*-
import scrapy
import csv
import Queue

from scrapy.http import Request
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings
# from scrapy.contrib.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class ExampleSpider(scrapy.Spider):
    settings = get_project_settings()

    # name = settings.get('SPIDER_NAME')
    name = "example"
    # allowed_domains = settings.get('ALLOWED_DOMAINS')
    allowed_domains = ['utahcounty.gov']
    start_urls = ['http://www.utahcounty.gov/LandRecords/BookPage.asp?av_book=52&av_page=694']

    # set_allowed_domains = settings.get('SET_ALLOWED_DOMAINS')

    # rules = (Rule(LinkExtractor(allow=('.*'), deny=('\.exe', '\.zip')), callback='parse_item', follow=True, ),)
    # rule = response.xpath('//table/tr[*]/td[1]/text()').extract()
    # Define Data
    def parse(self, response):
        for sel in response.xpath('//table/tr[*]/td[1]'):
            owners = sel.xpath('/text()').extract()
            # link = sel.xpath('a/@href').extract()
            # desc = sel.xpath('text()').extract()
            print owners

    # RESULTS = ['https://le.utah.gov/xcode/Title57/Chapter11/57-11.html?v=C57-11_1800010118000101', 'https://commerce.utah.gov/', 'https://realestate.utah.gov/realestate/re-company.html']

    # Open File
    # resultFyle = open("/home/scrapy/osboxes/files/csvFileTests/startUrls.csv", 'w')

    # Write data to file
    # for r in RESULTS:
    #   resultFyle.write(r + "\n")
    # resultFyle.close()

    if len(start_urls) < 1:
        resultFyle = open("/home/scrapy/osboxes/files/csvFileTests/startUrls.csv", 'rb')
        reader = csv.reader(resultFyle)
        for row in reader:
            tmpString = row[0]
            tmpString = tmpString.replace("\\", '')
            row = tmpString
            start_urls.append(str(row))
            print row

    # This creates a Queue within the RAM memory
    # TO_DO = Queue.Queue()

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            yield Request(
                url=response.urljoin(href),
                callback=self.parse_item
            )
