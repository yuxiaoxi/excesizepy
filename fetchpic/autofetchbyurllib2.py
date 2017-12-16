# coding=utf-8
import urllib2
import urllib
import time
import threading
from datetime import datetime
from bs4 import BeautifulSoup
import threadpool

path = "/Users/yuzhuo/myfile/fetchpic/img"


class FetchImage():
    def __init__(self):
        self.picsite = 'http://www.nphoto.net/news/2012-02/20/b143d88f8f937f69'
        self.page = 1
        self.suffix = '.shtml'
        self.imageList = []
    def getImageUrls(self):
        try:
            for i in range(1,10,1):
                if i ==1:
                    html = urllib2.urlopen(self.picsite+self.suffix)
                else:
                    html = urllib2.urlopen(self.picsite+str(i)+self.suffix)
                print "抓取第" + str(i) + "页数据"
                soup = BeautifulSoup(html,'lxml')
                soup.select('p img')
                imgsp = soup.select('p img')
                print len(imgsp)
                for i in range(0,len(imgsp),1):
                    print imgsp[i].attrs['src']
                    self.imageList.append(imgsp[i].attrs['src'])
        except urllib2.urlopen, e:
            if hasattr(e,'reason'):
                print e.reason

    def downloadImage(self):

        self.getImageUrls()
        pool = threadpool.ThreadPool(10)
        requests = threadpool.makeRequests(self.download, self.imageList)
        [pool.putRequest(req) for req in requests]
        pool.wait()
        # for imgurl in self.imageList:
        #     self.download(imgurl)

    def getTimeStamp(self):
        daytimestr = datetime.strftime(datetime.today(), '%a %b %d %H:%M:%S %Y')
        daystamp = str(time.mktime(time.strptime(daytimestr, "%a %b %d %H:%M:%S %Y"))).split('.')[0]
        return daystamp

    def download(self,imgurl):
        urllib.urlretrieve(imgurl, path + imgurl.split('/')[len(imgurl.split('/')) - 1])



if __name__ == '__main__':
    imageobj = FetchImage()
    imageobj.downloadImage()