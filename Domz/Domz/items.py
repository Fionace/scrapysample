# Definthere the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DomzItem(Item):
    # define the fields for your item here like:
    # name = Field()
    title=Field()
    link=Field()
    desc=Field()
