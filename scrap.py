import requests
from bs4 import BeautifulSoup as bs
import csv

tagFile = open('tagsData.csv', mode='w', newline='')
tagFileWriter = csv.writer(tagFile, delimiter=',', quotechar='"')


def getInfo(url):
    content = requests.get(url)
    soup = bs(content.content, 'lxml')
    for tag in soup.select('div.tag-cell'):
        l = []
        l.append(tag.select_one('a.post-tag').text)
        l.append(tag.select_one('span.item-multiplier-count').text)
        todayAsked = tag.select_one('div.stats-row>a')
        l.append(todayAsked.text.replace(' asked today', '') if todayAsked and todayAsked.text.find(
            ' asked today') > 0 else 0)
        weekAsked = tag.select_one('div.stats-row>a+a')
        l.append(weekAsked.text.replace(' this week', '') if weekAsked and weekAsked.text.find(' this week') > 0 else 0)
        tagFileWriter.writerow(l)


for i in range(1, 11):
    getInfo("https://stackoverflow.com/tags?page=" + str(i) + "&tab=popular")
    print(i, "done")

tagFile.close()
