# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList
from qsbk.items import QsbkItem

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['gushiwen.org']
    start_urls = ['https://www.gushiwen.org/default_1.aspx']
    base_domain = 'https://www.gushiwen.org'

    def parse(self, response):
        gushi_divs = response.xpath("//div[@class='main3']//div[@class='sons']")[0:-4]
        print('= ' * 30)
        for gushi_div in gushi_divs:
            name = gushi_div.xpath(".//p/a/b/text()").get()
            #print(name)
            year = gushi_div.xpath(".//p[@class='source']/a/text()").get()
            author = gushi_div.xpath(".//p[@class='source']/a[2]/text()").get()
            #print(year + " . " + author)
            content = gushi_div.xpath(".//div[@class='contson']//text()").getall()
            content = "".join(content).strip()
            #print(content)
            item = QsbkItem(name = name, year = year, author = author, content = content)
            
            yield item
            
        next_url = response.xpath("//a[@id='amore']/@href").get()
        
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_domain + next_url, callback = self.parse)
            
        print('= ' * 30)
