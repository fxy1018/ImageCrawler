"""
crawler:  use image.baidu.com to search small pictures about specific query 
"""
'''
Created on Mar 7, 2017
@author: fanxueyi
'''
import re
import requests
import json
import csv
import time

class ImageWriter(object):
    def __init__(self, fileName):
        self.count = 0 
        self.imgFile = open(fileName, "a", encoding="utf-8")
        self.writer = csv.writer(self.imgFile)
        self.writer.writerow(["Id", "URL", "Restaurant_Id", "Restaurant"])
       
    def writeRow(self, urls, id, name):
        for url in urls:
            row = [self.count, url, id, name]
            self.count += 1
            self.writer.writerow(row)
    
    def closeFile(self):
        self.imgFile.close()
    
class ImageCrawler(object):
    def __init__(self, name, id,  location):
        self.restaurantName = name
        self.location = location
        self.restName= self.__convertRestName()
        self.searchItem = self.restName + "-" + self.location.lower()
        self.foodHtml= None
        self.resHtml = None
        self.pNum = None
        self.urls = []
        self.id = id
          
    def __convertRestName(self):
        name= re.sub(r'&amp;', " and ", self.restaurantName.lower())
        name= re.sub(r'’', ' ', name)
        name = re.sub(r"  ", " ", name)
        name = re.sub(r' ', '-', name)
        return(name)
    
    
        
    def __getRestHtml(self):
        restURL = "https://www.yelp.com/biz/" + self.searchItem + "?osq=Restaurants"
        self.restHtml = requests.get(restURL).text
    
    def __getFoodHtml(self):
        foodURL = "http://www.yelp.ca/biz_photos/" + self.searchItem + "?tab=food"
        self.foodHtml = requests.get(foodURL).text
        
    def crawlRestInfo(self):
        self.__getRestHtml()
        address = re.findall('"address": \{(.*?)\}', self.restHtml, re.S)
        self.address = json.loads("{" + address[0] + "}")
        locationFile = self.restName + "_name.txt"
        
        
        
    def crawlImage(self):
        self.__getFoodHtml()
        print(self.restName)
        pagesNum = re.findall('<div class=\"page-of-pages .*?\">\n\s*?Page.*?of\s([0-9]*?)\n.*?<\/div>', self.foodHtml, re.S)
        if len(pagesNum) == 0:
            self.pNum = 0
            file = open("no_page_num.txt", "a", encoding = "utf-8")
            file.write(self.id+"_"+self.restaurantName+"\n")
            file.close()
        else:
            self.pNum = int(pagesNum[0])
        
        for i in range(self.pNum):
            if i == 0:
                foodHtml = self.foodHtml
            else:
                foodURL = "http://www.yelp.ca/biz_photos/" + self.searchItem + "?start=" + str(i*30) + "&tab=food"
                foodHtml = requests.get(foodURL).text
             
            searchPattern = '<img alt=\"Photo of ' + self.restaurantName + '.*?\" src=\"(.*?)\" width=\"226\">'
            imgURLs  = re.findall(searchPattern, foodHtml, re.S)
            self.urls.extend(imgURLs)
#             if i >2 :
#                 break
            time.sleep(0.1)
                
        return(self.urls)

#     def __writeRow(self, url, writer):
#         print(url)
#         row = [self.count, url, self.id, self.restaurantName]
#         self.count += 1
#         writer.writerow(row)
        
                
#         count = 0
#         for url in imgURLs:
#             if count > 1:
#                 break
#             print("now downloading No." + str(count+1) + " picture, the address of picture is :" + str(url))
#      
#             try:
#                 imageResponse = requests.get(url, timeout=10)
#             except requests.exceptions.ConnectionError:
#                 print("ERROR: fail to download")
#                 continue
#      
#             imageName = 'Images/' + self.restName + "_" + str(count) + ".jpg"
#             imageFile = open(imageName, 'wb')
#             imageFile.write(imageResponse.content)
#             imageFile.close()
#             count += 1
#      
#         print("Finished, download " + str(count) + " pictures")
#         

# if __name__ == '__main__':
#      
#     restCrawler = ImageCrawler( name = "Fayuca" , location = "Vancouver")
#     urls = restCrawler.crawlImage()
         
