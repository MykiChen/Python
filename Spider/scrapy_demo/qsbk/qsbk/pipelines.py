# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

"""
from scrapy.exporters import JsonItemExporter, JsonLinesItemExporter

class QsbkPipeline(object):
    def __init__(self):
        self.fp = open("gushi.json", 'wb')
        self.exporter = JsonItemExporter(self.fp, ensure_ascii = False, encoding = 'utf-8')
        self.exporter.start_exporting()
    
    def open_spider(self, spider):
        print('爬虫开始......')
        pass
    
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.fp.close()
        print("爬虫结束")
"""
        
from scrapy.exporters import JsonLinesItemExporter

class QsbkPipeline(object):
    def __init__(self):
        self.fp = open('gushi.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii = False, encoding = 'utf-8')
        
    def open_spider(self, spider):
        print('爬虫开始....')
        
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    
    def close_spider(self, spider):
        self.fp.close()
        print('爬虫结束！')
        
        