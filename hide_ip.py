'''
Created on Mar 7, 2017

@author: fanxueyi

'''


"""

crawler:  use image.baidu.com to search small pictures about specific query 

in order to make my crawler looks like human behavior, set http header (chrome browser) 
header:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36

hide IP to collect data

other useful package
selenium : 最初是一个为网站自动化测试开发的工具, 它能直接控制浏览器的行为, 可模拟用户的各种操作, 比如键盘输入, 鼠标点击等. 这就为在爬虫里执行JavaScript代码提供了可能.
phantomjs : 是无头的(headless)浏览器, 它会将网站加载到内存并执行页面上的JavaScript代码, 但不会向用户展示图形界面, 即你看不到实体的浏览器

set agency:  
packages: Tor,  PysSocks



"""
'''
Created on Mar 7, 2017

@author: fanxueyi
'''

#can't run unless you have install Tor
import socks
import socket
 
from urllib.request import urlopen
 
socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket
print(urlopen("http://icanhazip.com").read())



#example to use selenium + phantomjs
from selenium import webdriver
import time

# 将webdriver.PhantomJS()改成webdriver.Chrome(), 就打开了一个Chrome浏览器
driver = webdriver.Chrome(executable_path='modify/the/path')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")  # 打开url
time.sleep(3)  # 延迟3s. 该动态网页使用ajax设置了一个2s的延迟, 2s之后页面会发生变化
print(driver.find_element_by_id('content').text)
driver.close()

 




