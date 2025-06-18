# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu_spider.items import ArticleItem


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='_1RuRku']/text()").get()
        #avatar = response.xpath("//div[@class='_2mYfmT']/a[@class='_1OhGeD']/img/@src").get()
        author = response.xpath("//span[@class='_22gUMi']/text()").get()
        pub_time = response.xpath("//div[@class='s-dsoj']/time/text()").get()
        url = response.url
        article_id = url.split("/")[-1]
        #content = response.xpath("//div[@class='_gp-ck']").get()
        
        word_count = response.xpath("//div[@class='s-dsoj']/span[2]/text()").get()
        comment_count = response.xpath("////span[@class='_2R7vBo']/text()").get()
        read_count = response.xpath("//div[@class='s-dsoj']/span[3]/text()").get()
        like_count = response.xpath("//span[@class='_1LOh_5']/text()").get()
        
        subjects = ",".join(response.xpath("//div[@class='_2Nttfz']/a//text()").getall())
        
        
        item = ArticleItem(
            title=title,
            #avatar=avatar,
            author=author,
            pub_time=pub_time,
            #origin_url=origin_url,
            #content=content,
            article_id=article_id,
            subjects = subjects,
            word_count = word_count,
            comment_count = comment_count,
            read_count = read_count,
            like_count = like_count
        )
        yield item
        