# Scrapy settings for Domz project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'Domz'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['Domz.spiders']
NEWSPIDER_MODULE = 'Domz.spiders'
DEFAULT_ITEM_CLASS = 'Domz.items.DomzItem'
ITEM_PIPELINES=['Domz.pipelines.DomzPipeline']
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

