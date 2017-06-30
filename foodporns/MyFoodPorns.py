'''
Created on Jun 27, 2017

@author: fanxueyi
'''


import requests
import re
import csv 
import time
from _cffi_backend import string

class shopCrawler(object):
    def __init__(self, location, sort=""):
        self.location = location.lower()
        if sort == "rating" or sort == "review_count":
            self.sort = sort
        else:
            self.sort = ""
        self.pNum = None
        self.Html = None
        self.url = None
        self.records = set([])
       
    
    def __getHtml(self):
        #serach all vancouver resteraunts (4940), if sortby rating or most reviewed, only 40 stores
        # + "&sortby=rating"
        # + "&sortby=review_count"
        self.url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=" + self.location 
        
        if self.sort:
            self.url = self.url + "&sortby=" + self.sort 
            
        self.Html = requests.get(self.url).text
        pagesNum = re.findall('<div class=\"page-of-pages .*?\">\n\s*?Page.*?of\s([0-9]*?)\n.*?<\/div>', self.Html, re.S)
        self.pNum = int(pagesNum[0])
        
    
    def shopsCrawler(self):
        self.__getHtml()
        cityFileName = self.location + "_" + self.sort + "_restaurants.csv"
        cityFile = open(cityFileName, 'w', encoding='utf-8')
        writer = csv.writer(cityFile)
        writer.writerow(["Id", "Name","Rating", "Review Count", "Price", "Style", "Neighborhood", "Address", "Phone Number", "Link" ])
        count = 0
        for i in range(self.pNum):
            print("now fetching No." + str(count)+" picture")
            if i == 0:
                cityHtml = self.Html
            else:
                cityURL = self.url + "&start=" + str(i*10)
                cityHtml = requests.get(cityURL).text
             
            searchPattern = '<li class=\"regular-search-result\">(.*?<ul class=\"search-result_tags\">.*?<\/ul>.*?)<\/li>'
            restList = re.findall(searchPattern, cityHtml, re.S)
            for r in restList:
                restInfo = self.__getRestInfo(r)
                if len(restInfo) != 0:
                    infoList = [count] + restInfo
                    count += 1
                    writer.writerow(infoList)
            time.sleep(0.1)
            
                
        cityFile.close()
    
    def __getRestInfo(self, restaurant):
        address =  re.sub('<br>','#', re.findall('<address>(.*?)<\/address>', restaurant, re.S)[0].strip())
        if address in self.records:
            return([])
        else:
            self.records.add(address)
        
        
        name = self.__findallRex('<a class=\"biz-name.*?><span\s>(.*?)<\/span>', restaurant)
        
        tempRating = self.__findallRex('<div class=\"i-stars.*?title=\"(.*?)\">', restaurant)
        if tempRating != "Null":
            rating = tempRating.split(" ")[0]
        else:
            rating = tempRating
            
        reviewCount = self.__findallRex('<span class=\"review-count.*?>.*?([0-9]*?)\sreviews.*?<\/span>', restaurant)
        price = self.__findallRex('<span class=\"business-attribute\sprice-range\">(.*?)<\/span>', restaurant)
    
        tempStyle = self.__findallRex('<span class=\"category-str-list\">(.*?)<\/span>', restaurant)
        if tempStyle != "Null":
            style = "#".join(re.findall('<a.*?>(.*?)</a>', tempStyle, re.S))
        else:
            style = tempStyle
            
        tempNeighborhood = self.__findallRex('<span class=\"neighborhood-str-list\">(.*?)<\/span>', restaurant)
        if tempNeighborhood != "Null":
            neighborhood = re.findall('<span class=\"neighborhood-str-list\">(.*?)<\/span>', restaurant, re.S)[0].strip()
        else:
            neighborhood = tempNeighborhood
        phone = self.__findallRex('<span class=\"biz-phone">(.*?)<\/span>', restaurant).strip()
        
        link = self.__findallRex('<div class="main-attributes">.*?<div class="media-avatar">.*?<a href=\"(.*?)\".*?>', restaurant)
        
        return([name, rating, reviewCount, price, style, neighborhood, address, phone, link]) 
    
    def __findallRex(self, pattern, string):
        foundItems = re.findall(pattern, string, re.S)
        res = "Null"
        if len(foundItems) != 0:
            res = foundItems[0]
        return(res)
            

    
# if __name__ == '__main__':
#     url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=vancouver" 
#     cityHtml = requests.get(url).text
#     searchPattern = '<li class=\"regular-search-result\">(.*?<ul class=\"search-result_tags\">.*?<\/ul>.*?)<\/li>'
#     restList = re.findall(searchPattern, cityHtml, re.S)
#     
#     string = restList[0]
#         
#     link = re.findall('<div class="main-attributes">.*?<div class="media-avatar">.*?<a href=\"(.*?)\".*?>', string, re.S)
#     print(link)
#     
  
    
    