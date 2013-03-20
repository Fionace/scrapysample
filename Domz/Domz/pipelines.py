# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from Domz.items import DomzItem
#from spiders.DomzSpider import item
from spiders import DomzSpider

class DomzPipeline(object):
    def process_item(self, item, spider):
        self.file=open('itemcon.txt','wa')
        self.file.write(str(item['title'])+'\n')
