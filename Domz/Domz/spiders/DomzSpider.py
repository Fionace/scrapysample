from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
from Domz.items import DomzItem

items=[]
item=DomzItem()

class DomzSpider(BaseSpider):
    name='Exper'
    start_urls=['http://www.baidu.com/']
#'http://doc.scrapy.org/en/0.16/index.html']
    def parse(self,response):
        hxs=HtmlXPathSelector(response)
        titcon=hxs.select('//title/text()').extract()
        item['title']=titcon
        #for url in hxs.select('//a/@href').extract():
        
        #    Request(url,callback=self.parse)
        return items
