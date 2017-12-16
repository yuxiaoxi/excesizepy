# coding=utf-8
import urllib2
from bs4 import BeautifulSoup

site = 'http://blog.csdn.net/u014351782'
html = urllib2.urlopen(site)
soup = BeautifulSoup(html,'lxml')
soup.select('div #article_list .list_item div.article_title span.link_title')[0].text
for item in soup.select('div #article_list .list_item div.article_title span.link_title'):
    print str(item.text.encode('utf-8')).lstrip().rstrip()