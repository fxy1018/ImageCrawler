"""
practices are according to voidsky's blog
http://www.jianshu.com/p/74b94eadae15

"""

'''
Created on Mar 7, 2017

@author: fanxueyi
'''

#easy use case for requests
import requests

# url = 'http://www.northeastern.edu'
# html = requests.get(url)
# print(html.text)

# url = 'https://www.google.com'
# html = requests.get(url)
# print(html.text)





#regular expression

import re
# text = html.text
# urls = re.findall(r'<a href=(.*?)>', text, re.S)
# for i in urls:
#     print(i)
    
# print(re.search('<nav>(.*?)</nav>', text, re.S))


#change page number using regular expression
pages = 'http://tieba.baidu.com/p/4342201077?pn=1'
# for i in range(10):
#     print(re.sub('pn=\d', 'pn=%d'%i, pages))
#     
    
#XPath    
# from lxml import etree
# html='''
# <div id="test1">content1</div>
# <div id="test2">content2</div>
# <div id="test3">content3</div>
# '''
# 
# selector = etree.HTML(html)
# content = selector.xpath('//div[start-with(@id,"test")]/text()')
# for each in content:
#     print(each)


url2 = 'https://s-media-cache-ak0.pinimg.com/736x/80/d3/64/80d364e09d31fcba8af274926d4332ff.jpg'
picture = requests.get(url2)

f1 = open("file1.jpg", 'wb')
f1.write(picture.content)

   
    
    
    