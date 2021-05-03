# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import RE.settings
import scrapy

def _mocked_download_func(request, info):
    response = request.meta.get('response')  # type: object
    return response() if callable(response) else response

class RePipeline(object):
    # def setUp(self):
    #     self.spider = scrapy.Spider('re')
    #     #self.pipe = self.pipeline_class(download_func=_mocked_download_func)
    #     #self.pipe.open_spider(self.spider)
    #     #self.info = self.pipe.spiderinfo[self.spider]

    def process_item(self, item, spider):
        #self.get_path(item['files_urls'])
        localPath = '/home/osboxes/files/'  # type: str
        path = localPath + str(item['files_urls'].split('/')[-1])
        with open(path, "wb") as f:
            f.write(item['files'])
        # # remove body and add path as reference
        # del item['body']
        # item['path'] = path
        # let item be processed by other pipelines. ie. db store
        return item


# This code will save the HTML of something to a single file.
    # def process_item(self, item, path, spider):
    #     with open(path, 'wb') as f:
    #         f.write(item['files'])
    #     return item
