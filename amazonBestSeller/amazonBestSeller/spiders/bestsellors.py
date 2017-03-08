# -*- coding: utf-8 -*-
import scrapy
from amazonBestSeller.items import AmazonbestsellerItem
import time
import re
from asyncio.coroutines import iscoroutine
from email.generator import UNDERSCORE

class BestsellorsSpider(scrapy.Spider):
    name = "bestsellors"
#     allowed_domains = ["https://www.amazon.com/gp/bestsellers/books/283155/ref=s9_acsd_ri_bw_clnk?pf_rd_m=ATVPDKIKX0DER"]
    start_urls = ['https://www.amazon.com/gp/bestsellers/books/283155/ref=s9_acsd_ri_bw_clnk?pf_rd_m=ATVPDKIKX0DER/',]
        
    def parse(self, response):
        selector = scrapy.Selector(response)
    
        item_dict = AmazonbestsellerItem()
        selector = scrapy.Selector(response)
        books = selector.xpath('//div[@class="zg_itemImmersion"]')
        for book in books:
            rank = book.xpath('div[@class="zg_rankDiv"]/span/text()').extract()[0]
            title = book.xpath('div[@class="zg_itemWrapper"]/div/a/div[@class="p13n-sc-truncate p13n-sc-truncated-hyphen p13n-sc-line-clamp-1"]/text()').extract()[0]
            author_temp = book.xpath('div[@class="zg_itemWrapper"]/div/div[@class="a-row a-size-small"]/a/text()').extract()
            if author_temp:
                author = author_temp[0]
            else:
                author = book.xpath('div[@class="zg_itemWrapper"]/div/div[@class="a-row a-size-small"]/span/text()').extract()[0]
            score = book.xpath('div[@class="zg_itemWrapper"]/div/div[@class="a-icon-row a-spacing-none"]/a[@class="a-link-normal"]/i/span/text()').extract()
            if score:
                score = score[0]
            else:
                score = "Null"
        
            reviews = book.xpath('div[@class="zg_itemWrapper"]/div/div[@class="a-icon-row a-spacing-none"]/a[@class="a-size-small a-link-normal"]/text()').extract()
            if reviews:
                reviews = reviews[0]
            else:
                reviews = "Null"
            
            
            editiontype = book.xpath('div[@class="zg_itemWrapper"]/div/div[@class="a-row a-size-small"]/span/text()').extract()[0]
                
            price = book.xpath('div[@class="zg_itemWrapper"]/div/div[@class="a-row"]/span/span/text()').extract()
            
            if price:
                price = price[0]
            else:
                price = "Null"

            item_dict['rank'] = rank.replace(' ','').replace('\n', '')
            item_dict['title'] = title.replace(' ','').replace('\n', '')
            item_dict['author'] = author.replace(' ','').replace('\n', '')
            item_dict['score'] = score.replace(' ','').replace('\n', '').replace('outof5stars', '')
            item_dict['reviews'] = reviews.replace(' ','').replace('\n', '')
            item_dict['editiontype'] = editiontype.replace(' ','').replace('\n', '')
            item_dict['price'] = price.replace(' ','').replace('\n', '')
            yield item_dict 
                
        page = selector.xpath('//li[@class="zg_page zg_selected"]/a/@href').extract()[0]
        pageIndex = re.search(r'.+?pg=(\d)', page, re.S).group(1)
        if int(pageIndex) < 5:
            nextPage = re.search('(.+?pg=)\d', page).group(1) + str(int(pageIndex)+1)
            print(nextPage)
            time.sleep(2)
            yield scrapy.http.Request(nextPage,callback=self.parse)

            
            #如果页面中又下一页的link， 可以使用以下代码：
#             nextPage = selector.xpath('//span[@class="next"]/link/@href').extract()
#             if nextPage:
#                 next = nextPage[0]
#                 print next
#                 yield scrapy.http.Request(next,callback=self.parse)


        