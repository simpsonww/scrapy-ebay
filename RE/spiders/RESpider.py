# -*- coding: utf-8 -*-
import Queue
import csv

import scrapy
# from scrapy.contrib.spiders import Rule
# Setup for scrapy spider
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy.utils.project import get_project_settings
from tika import parser

# Importing the item class and pipeline that we defined
from RE.items import ReItem


class RESpiderSpider(scrapy.Spider):
    settings = get_project_settings()

    name = settings.get('SPIDER_NAME')
    allowed_domains = settings.get('ALLOWED_DOMAINS')
    start_urls = []
    set_allowed_domains = settings.get('SET_ALLOWED_DOMAINS')

    rules = (Rule(LinkExtractor(allow=('.*'), deny=('\.exe', '\.zip')), callback='parse_item', follow=True, ),)
    # TODO: Figure out how to read a list of .csv files, as oppose to only specifying one at a time.
    # TODO: write conditional statement to let us decide whether or not we want to have allowed domains. (set domain variable in settings)

    #csv_file_to_read = ['/home/scrapy/osboxes/files/csvFileTests/startUrls.csv']

    # Specify from settings where desired .csv file is located

    if len(start_urls) < 1 :
        resultFyle = open('C:/Users/Scott/PycharmProjects/scrapy-ebay/csvFileTests/startUrls.csv', 'rb')
        reader = csv.reader(resultFyle)
        for row in reader:
            tmpString = row[0]
            tmpString = tmpString.replace("\\", '')
            row = tmpString
            start_urls.append(str(row))

    # TODO: read from a .csv file, then read from a database that was populated by a web page. (domains allowed)

    # This creates a Queue within the RAM memory
    TO_DO = Queue.Queue()



    # TODO: Use xpath instead of response.css use .hsx (hopefully this will get rid of the "no css in response  error"
    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            yield Request(
                url=response.urljoin(href),
                callback=self.parse_item
            )

    def parse_item(self, response):
        item = ReItem()
        item['files_urls'] = response.url
        item['files'] = response.body
        self.tika_item(item)

    def tika_item(self, item):
        filename = item['files_urls'].rsplit('/', 1)[-1]
        parsed = parser.from_file('/home/osboxes/files/' + filename)
        with open("/home/osboxes/files/textmetadata/" + filename + ".txt", "w") as text_file:
            text_file.write(str(parsed["metadata"]))
        with open("/home/osboxes/files/textcontent/" + filename + ".txt", "w") as text_file:
            text_file.write(parsed["content"].encode(
                'utf8'))  # without the encode utf8 cannot process bullet points in some .docx files.
            return item

            # item['files'] = response.name
            # filelist = item['files_urls']
            # filename = response.url.rsplit('/', 1)[-1]
            # parsed = parser.from_file('/home/osboxes/files/' + filename)
            # with open("/home/osboxes/files/textcontent/" + filename + ".txt", "w") as text_file:
            #     text_file.write(parsed["content"].encode(
            #         'utf8'))  # without the encode utf8 cannot process bullet points in some .docx files.






    # for i in filelist:
    #     filename = i.rsplit('/', 1)[-1]

