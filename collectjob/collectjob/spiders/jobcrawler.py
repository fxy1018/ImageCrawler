# -*- coding: utf-8 -*-
import scrapy


class JobcrawlerSpider(scrapy.Spider):
    name = "jobcrawler"
#     allowed_domains = ["www.lagou.com/zhaopin"]
    start_urls = ['http://www.lagou.com/zhaopin/']

    def parse(self, response):
        with open("lagou.html", 'wb') as f1:
            f1.write(response.body)
        print(response.body)
        pass
