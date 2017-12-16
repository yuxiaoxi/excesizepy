# coding=utf-8

import urllib
import urllib2,cookielib
from bs4 import BeautifulSoup
import threadpool

class DownImage():
    def __init__(self):
        self.site = 'http://xxx.com';
        self.path = '/Users/yuzhuo/myfile/fetchpic/img/'
        self.imageList = []

    def getImageList(self):
        try:
            hdr = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}
            req = urllib2.Request(url=self.site, headers=hdr)
            html = urllib2.urlopen(req).read()
            # html = urllib2.urlopen(self.site)
            soup = BeautifulSoup(html,'lxml')
            # imgsp = soup.select('div #wp .wp div #ct .wp td.plc div.pct div.pcb div.t_fsz td.t_f img')
            imgsp = soup.select('div.pattl div.mbn img')
            print imgsp[0]
            print len(imgsp)
            for i in range(0,len(imgsp),1):
                print "http://cdn.taoy666.info/"+imgsp[i].attrs['zoomfile']
                self.imageList.append("http://cdn.taoy666.info/"+imgsp[i].attrs['zoomfile'])

        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print e.reason

    def downloadByPool(self):
        self.getImageList()
        dpool = threadpool.ThreadPool(10)
        requests = threadpool.makeRequests(self.downLoad, self.imageList)
        [dpool.putRequest(req) for req in requests]
        dpool.wait()

    def downLoad(self,imgurl):

        urllib.urlretrieve(imgurl, self.path + imgurl.split('/')[len(imgurl.split('/')) - 1])





if __name__ == '__main__':
    downimg = DownImage()
    downimg.downloadByPool()