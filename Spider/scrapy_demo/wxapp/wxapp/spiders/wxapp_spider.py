# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxapp.items import WxappItem

class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=1&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=1&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+article-.+\.html'), callback='parse_detail', follow=False)
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='ph']/text()").get()
        author_p = response.xpath("//p[@class='authors']")
        author = author_p.xpath(".//a/text()").get()
        pub_time = author_p.xpath(".//span/text()").get()
        #print('author:%s/pub_time:%s' % (author, pub_time))
        
        article_content = response.xpath("//td[@id = 'article_content']//text()").getall()
        content = "".join(article_content).strip()
        
        item = WxappItem(title = title, author = author, pub_time = pub_time, content = content)
        yield item
        #print(article_content)
        #print('\n' + '* ' * 30)
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        #return item
