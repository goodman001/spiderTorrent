# Scrapy settings for dirbot project

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.Website'

#ITEM_PIPELINES = {'dirbot.pipelines.FilterWordsPipeline': 1}
ITEM_PIPELINES = {
    #'dirbot.pipelines.RequiredFieldsPipeline':300,
    'dirbot.pipelines.FilterWordsPipeline':300,
    'dirbot.pipelines.MySQLStorePipeline':300,
}


# start MySQL database configure setting
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'co_dbbase'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'ua&%e978'
# end of MySQL database configure setting
LOG_LEVEL = 'WARNING'

# stop ban
DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = True
