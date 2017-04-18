# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



from twisted.enterprise import adbapi
from scrapy import log
import MySQLdb
import MySQLdb.cursors

class MySQLPipeline(object):
    """ 将抓取到的数据存入mysql数据中 """

    def __init__(self):
        self.dbpool=adbapi.ConnectionPool('MySQLdb',
            host = '127.0.0.1',
            db = 'jwc',
            user = 'root',
            passwd = 'root',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = False
                                          )

    def process_item(self,item,spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self, tb, item):
        # tablename 你的表名
        tb.execute("insert into jwcinfo (title,body,url,releasetime) values (%s,%s,%s,%s)", (item["title"],item["body"], item["url"],item["releasetime"]))

        log.msg("Item data in db: %s" % item, level=log.DEBUG)

    def handle_error(self, e):
        log.err(e)
