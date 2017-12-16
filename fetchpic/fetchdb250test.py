# coding=utf-8

import urllib2
from bs4 import BeautifulSoup

site = 'https://movie.douban.com/top250?start=0&filter=&type='
html = urllib2.urlopen(site)
soup = BeautifulSoup(html,"lxml")
i = 1
print soup.select('ol.grid_view em.')[1*i].text
print soup.select('ol.grid_view div.item div.pic img')[i].attrs['alt']
print str(soup.select('ol.grid_view div.info div.bd p.')[1*i].text.encode("utf-8")).lstrip().rstrip()
print soup.select('ol.grid_view div.info div.bd span.rating_num')[1*i].text
print soup.select('ol.grid_view div.info div.bd div.star span')[4*i +3].text