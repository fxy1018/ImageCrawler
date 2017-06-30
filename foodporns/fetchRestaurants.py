'''
Created on Jun 29, 2017

@author: fanxueyi
'''


from foodporns import MyFoodPorns
from foodporns import MyImageCrawler
import csv
import re


if __name__ == '__main__':
#get restaurants list
    print("now fetching the restaurant......")
    myCrawler = MyFoodPorns.shopCrawler("Vancouver")
    myCrawler.shopsCrawler()

#get image URLs

#read csv file
#     fileName = "Vancouver__restaurants.csv"
# 
#     storeList = open(fileName, "r", encoding="utf-8")
#     reader = csv.reader(storeList)
#     header = next(reader)
#     count = 0
#     mywriter = MyImageCrawler.ImageWriter("Vancouver__restaurant_urls.csv")
#     
#     for r in reader:
#         if count > 46:
#             
#             restId = r[0]
#             restName = r[1]
#             print(restName)
#             restCrawler = MyImageCrawler.ImageCrawler( name = restName , id = restId, location = "Vancouver")
#             urls = restCrawler.crawlImage()
#             
#             mywriter.writeRow(urls, restId)
#         
#         count += 1
# #         if count > 2:
# #             break
#     mywriter.closeFile()