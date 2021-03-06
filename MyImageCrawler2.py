"""

crawler:  use image.baidu.com to search small pictures about specific query 

in order to make my crawler looks like human behavior, set http header (chrome browser) 
header:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36

"""
'''
Created on Mar 7, 2017

@author: fanxueyi
'''
import re
import requests
from bs4 import BeautifulSoup


class ImageCrawler(object):
    def __init__(self, searchItem):
        self.searchItem = searchItem
        self.resHtml = None
        
    def __getHtml(self):
        self.searchItem = re.sub(r" ", "+", self.searchItem)
        url = "https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=" + self.searchItem + "&ct=201326592&v=flip"
        session = requests.Session()
        headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
                  "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
        req = session.get(url, headers= headers)
        self.resHtml = requests.get(url).text
        
    def crawlImage(self):
        self.__getHtml()
        
        imgURL = re.findall('"objURL":"(.*?)",', self.resHtml, re.S)    
        
        count = 0
        print("the search key word: " + self.searchItem + ', downloading...')
        for i in imgURL:
            if count > 1:
                break
            print("now downloading No." + str(count+1) + " picture, the address of picture is :" + str(i))
            try:
                imageResponse = requests.get(i, timeout=10)
            except requests.exceptions.ConnectionError:
                print("ERROR: fail to download")
                continue
            
            searchItem = re.sub(r"\+", "_", self.searchItem) or self.searchItem
          
            imageName = 'Images/' + searchItem + "_" + str(count) + ".jpg"
             
            imageFile = open(imageName, 'wb')
            imageFile.write(imageResponse.content)
            imageFile.close()
            count += 1
        print("Finished, download " + str(count) + " pictures")
            
if __name__ == '__main__':
    searchItem = input("Please show you search word: ")
    myCrawler = ImageCrawler(searchItem = searchItem)
    myCrawler.crawlImage()
    
    
    
            
            
            
            
            
            
        