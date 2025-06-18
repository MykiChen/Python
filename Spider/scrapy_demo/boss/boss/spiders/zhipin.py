# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from boss.items import BossItem

class ZhipinSpider(CrawlSpider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101010100/?query=python&page=1']

    rules = (
        #
        Rule(LinkExtractor(allow=r'.+\?query=python&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+\/job_detail/.+.html'), callback = 'parse_job', follow=False)
    )

    def parse_job(self, response):
        name = response.xpath("//div[@class='info-primary']/div[@class='name']/h1/text()").get().strip()
        salary = response.xpath("//div[@class='info-primary']/div[@class='name']/span/text()").get().strip()
        job_info = response.xpath("//div[@class='info-primary']/p[1]/text()")
        city = job_info[1]
        work_years = job_info[2]
        education = job_info[3]
        company = response.xpath("//div[@class='company-info']/a[2]/text()").get()
        
        item = BossItem(anme = name, salary = salary, city = city, work_years = work_years, company = company)
        yield item
