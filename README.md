## python可以做什么呢？

### 1、桌面应用

我们一键生成app的脚手架就是例子

常用做界面的库有wx



### 2、游戏应用

不到300行的代码完成一个简易的飞机大战游戏：



### 3、web应用

作为一个脚本语言web应用是必须支持的，常见的web框架有django,flask

### 4、server

当然不在话下，作为一个月活超过5亿的app instagram 就是用python作server支撑的



### 5、爬虫

是最常见而且十分适合初学者学习的一个功能。

说的多不如动手写的多！

现在手把手来分享下一个简易的爬虫程序。

#### 粟子1：获取某天气网站的天气数据

天气和空气质量的网站:http://www.pm25.com/shanghai.html


```
site = 'http://www.pm25.com/shanghai.html'
html = urllib2.urlopen(site)
soup = BeautifulSoup(html, "lxml")
quality = soup.find("span",{"class","bi_aqiarea_wuran"})
city = soup.find(class_='bi_loaction_city')
aqi = soup.find("a",{"class","bi_aqiarea_num"})
desc = soup.find("div",{"class","bi_aqiarea_bottom"})
```

#### 粟子2：获取csdn xx用户首页的所有文章标题

xx用户的首页地址：http://blog.csdn.net/u014351782

```
soup.select('div #article_list .list_item div.article_title span.link_title')[0].text

for item in soup.select('div #article_list .list_item div.article_title span.link_title'):
print item.text
```
上面的还是比较简单的！下面来点有难度的粟子

#### 粟子3：豆瓣top250电影抓取

电影网址：https://movie.douban.com/top250?start=25&filter=

网页显示的html源码：使用浏览器工具
先观查html源码发现获取需要的字段的方法如下：
```
i = 1
print soup.select('ol.grid_view em.')[1*i].text #排名
print soup.select('ol.grid_view div.item div.pic img')[i].attrs['alt'] #标题
print str(soup.select('ol.grid_view div.info div.bd p.')[1*i].text.encode("utf-8")).lstrip().rstrip() #基本描述
print soup.select('ol.grid_view div.info div.bd span.rating_num')[1*i].text #评分
print soup.select('ol.grid_view div.info div.bd div.star span')[4*i +3].text #评论数
```
找到了后然后开始写完整代码。

首先需要个专门来存每部电影基本信息的实体类吧！MovieInfo
```
class MovieInfo:
def __init__(self,rank,title,desc,stars,commentcount):
self.rank = rank
self.title = title
self.desc = desc
self.stars = stars
self.commentcount = commentcount
```
然后再写个爬取电影的类。

有三个方法：构造方法__init__(self)，

获取每页soup的方法getPageData(self)，

获取电影的方法getMovie(self)，

写入文件的方法writeToFile(self)

执行方法main(self)。
```
# coding=utf-8
import urllib2
from bs4 import BeautifulSoup

class MovieInfo:
def __init__(self,rank,title,desc,stars,commentcount):
self.rank = rank
self.title = title
self.desc = desc
self.stars = stars
self.commentcount = commentcount

class Movie250:
def __init__(self):
self.start = 0
self.param = '&filter=&type='
self.movieList = []
self.pageNum = 0
self.filePath = '/Users/yuzhuo/myfile/fetchpic/movie/dbtop250.csv'
# self.filePath = 'dbtop250.csv'

def getPageData(self):
try:

site = 'https://movie.douban.com/top250?start='+str(self.start)+self.param
html = urllib2.urlopen(site)
soup = BeautifulSoup(html, "lxml")
self.pageNum = (self.start + 25)/25
print "抓取第" + str(self.pageNum) + "页数据"
self.start += 25
return soup
except urllib2.URLError, e:
if hasattr(e, 'reason'):
print e.reason
def getMovie(self):

while self.start <=225:
movieData = self.getPageData()
for i in range(0,25,1):
rank = movieData.select('ol.grid_view em.')[1 * i].text.encode("utf-8")
title = movieData.select('ol.grid_view div.item div.pic img')[i].attrs['alt'].encode("utf-8")
desc = str(movieData.select('ol.grid_view div.info div.bd p.')[1 * i].text.encode("utf-8")).replace("\n", "").lstrip().rstrip()
stars = movieData.select('ol.grid_view div.info div.bd span.rating_num')[1 * i].text.encode("utf-8")
commentcount = movieData.select('ol.grid_view div.info div.bd div.star span')[4 * i + 3].text.encode("utf-8")
self.movieList.append(MovieInfo(rank, title, desc, stars, commentcount))
return self.movieList

def writeToFile(self):
fo = open(self.filePath, "wb+")
fo.write("排名" + ',')
fo.write("电影名" + ',')
fo.write("描述" + ',')
fo.write("评分" + ',')
fo.write("总评论数" + '\n')
try:
for movieInfo in self.movieList:
fo.write(movieInfo.rank + ',')
fo.write(movieInfo.title + ',')
fo.write(movieInfo.desc + ',')
fo.write(movieInfo.stars + ',')
fo.write(movieInfo.commentcount + '\n')
print '文件写入成功！'

finally:
fo.close()
def main(self):
self.getMovie()
self.writeToFile()

if __name__ == '__main__':
dbmovie = Movie250()
dbmovie.main()
```
最后看下爬取的结果：



 

#### 粟子4：抓取xx网站的图片

http://www.nphoto.net/news/2012-02/20/b143d88f8f937f69.shtml

单线程下载图片
```
for imgurl in self.imageList:
self.download(imgurl)
```
多线程下载图片：

引入线程池方式threadpool
```
pool = threadpool.ThreadPool(10)
requests = threadpool.makeRequests(self.download, self.imageList)
[pool.putRequest(req) for req in requests]
pool.wait()
```
附录：

bs4 安装



推荐几个比较好的学习文档和网站：

廖雪峰的学习博客：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000

python的api中文文档http://www.runoob.com/python/python-tutorial.html
————————————————
版权声明：本文为CSDN博主「我用py」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/zhuod/article/details/78819421
