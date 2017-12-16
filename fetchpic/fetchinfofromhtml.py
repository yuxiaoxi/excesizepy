# coding=utf-8
# import urllib2
# from bs4 import BeautifulSoup
#
# site = 'http://www.pm25.com/shanghai.html'
# html = urllib2.urlopen(site)
# soup = BeautifulSoup(html, "lxml")
# city = soup.find(class_='bi_loaction_city')
# aqi = soup.find("a",{"class","bi_aqiarea_num"})
# quality = soup.select(".bi_aqiarea_right span")
# quality1 = soup.find("span",{"class","bi_aqiarea_wuran"})
# desc = soup.find("div",{"class","bi_aqiarea_bottom"})
# print city.text
# print aqi.text
# print quality[0].text
# print quality[1].text
# print quality1.text
# print desc.text

import urllib2
from bs4 import BeautifulSoup

class GetInfoFromHtml:

    def __init__(self):
        self.site = 'http://www.pm25.com/shanghai.html'


    def getWeatherInfo(self):
        html = urllib2.urlopen(self.site)
        soup = BeautifulSoup(html, 'lxml')
        city = soup.find(class_='bi_loaction_city').text
        aqi = soup.find("a", {"class", "bi_aqiarea_num"}).text
        quality = soup.select(".bi_aqiarea_right span")
        quality1 = soup.find("span", {"class", "bi_aqiarea_wuran"}).text
        desc = soup.find("div", {"class", "bi_aqiarea_bottom"}).text
        print city
        print aqi
        print quality[0].text
        print quality[1].text
        print quality1
        print desc


if __name__ == '__main__':
    weatherInfo = GetInfoFromHtml()
    weatherInfo.getWeatherInfo()
