# -*- coding: utf-8 -*- 
from scrapy.exceptions import DropItem
from scrapy import signals
import MySQLdb
import MySQLdb.cursors
import codecs
import sys

from datetime import datetime
from hashlib import md5
from scrapy import log
from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi


class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    '''words_to_filter = ['politics', 'religion']'''
    def process_item(self, item, spider):
        #print "++++++++++++++"
        #print item
        #print "dataend"
        '''
        for word in self.words_to_filter:
            desc = item.get('description') or ''
            if word in desc.lower():
                raise DropItem("Contains forbidden word: %s" % word)
        else:
            return item'''
        return item
class RequiredFieldsPipeline(object):
    """A pipeline to ensure the item have the required fields."""

    required_fields = ('name', 'description', 'url')

    def process_item(self, item, spider):
        for field in self.required_fields:
            if not item.get(field):
                raise DropItem("Field '%s' missing: %r" % (field, item))
        return item

class MySQLStorePipeline(object):
    """A pipeline to store the item in a MySQL database.
    This implementation uses Twisted's asynchronous database API.
    """

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        # run db query in the thread pool
        d = self.dbpool.runInteraction(self._do_upsert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        # at the end return the item in case of success or failure
        d.addBoth(lambda _: item)
        # return the deferred instead the item. This makes the engine to
        # process next item (according to CONCURRENT_ITEMS setting) after this
        # operation (deferred) has finished.
        return d

    def _do_upsert(self, conn, item, spider):
        """Perform an insert or update."""
        ret = ""
        if item["zone"] == 1:
            conn.execute("""SELECT EXISTS(
            	SELECT 1 FROM co_movie WHERE url_id = %s
            )""", (item["url_id"], ))
            ret = conn.fetchone()[0]
        elif item["zone"] == 2:
	    conn.execute("""SELECT EXISTS(
                SELECT 1 FROM co_pics WHERE url_id = %s
            )""", (item["url_id"], ))
            ret = conn.fetchone()[0]
        elif item["zone"] == 3:
            conn.execute("""SELECT EXISTS(
                SELECT 1 FROM co_txts WHERE url_id = %s
            )""", (item["url_id"], ))
            ret = conn.fetchone()[0]
	#ret = False
        if ret:
	    print "[*]warning!!!" + str(item["url_id"]) + "have record in db!"
            '''conn.execute("""
                UPDATE website
                SET name=%s, description=%s, url=%s, updated=%s
                WHERE guid=%s
            """, (item['name'], item['description'], item['url'], now, guid))
            spider.log("Item updated in db: %s %r" % (guid, item))'''
            pass
        else:
            #print "start insert"
            if item["zone"] == 1:	    
                conn.execute("""
                     INSERT INTO co_movie (url_id,title,xflink,divcontent,topimg,kind,create_time)
                     VALUES (%s,%s,%s,%s,%s,%s,%s)
                """, (item["url_id"],item["title"],item["xflink"],item["divcontent"],item["topimg"],item["kind"],item["create_time"]))
                print "[*] info: " + str(item["url_id"]) +  " insert success!"
                spider.log("Item stored in db")
            elif item["zone"] == 2:
                conn.execute("""
                     INSERT INTO co_pics (url_id,title,divcontent,kind,create_time)
                     VALUES (%s,%s,%s,%s,%s)
                """, (item["url_id"],item["title"],item["divcontent"],item["kind"],item["create_time"]))
                print "[*] info: " + str(item["url_id"]) +  " insert success!"
                spider.log("Item stored in db")
            elif item["zone"] == 3:
                conn.execute("""
                     INSERT INTO co_txts (url_id,title,divcontent,kind,create_time)
                     VALUES (%s,%s,%s,%s,%s)
                """, (item["url_id"],item["title"],item["divcontent"],item["kind"],item["create_time"]))
                print "[*] info: " + str(item["url_id"]) +  " insert success!"
                spider.log("Item stored in db")
    def _handle_error(self, failure, item, spider):
        """Handle occurred on db interaction."""
        # do nothing, just log
        log.err(failure)

	
