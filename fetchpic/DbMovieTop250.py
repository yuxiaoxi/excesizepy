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
                rank =  movieData.select('ol.grid_view em.')[1 * i].text.encode("utf-8")
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

