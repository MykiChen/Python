# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors

class JianshuSpiderPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1', 
            'port': 3306,
            'user': 'root', 
            'password': 'root', 
            'database': 'jianshu', 
            'charset':'utf8'
        }
        
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None
    
    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (item['title'], item['content'], item['author'], item['article_id']))
        
        self.conn.commit()
        return item
    
    
    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into article(title, content, author, article_id) values (%s, %s, %s, %s) 
            """
            return self._sql
        return self._sql

    
#异步处理
class JianshuTwistedPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1', 
            'port': 3306,
            'user': 'root', 
            'password': 'root', 
            'database': 'jianshu', 
            'charset':'utf8',
            'cursorclass': cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        self._sql = None
        
        
    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into article(title, author, pub_time, article_id, read_count, like_count, word_count, comment_count, subjects) values (%s, %s, %s, %s, %s, %s, %s, %s, %s) 
            """
            return self._sql
        return self._sql
        
    def process_item(self, item, spider):
        defer = self.dbpool.runInteraction(self.insert_item, item)
        defer.addErrback(self.handle_error, item, spider)
            
            
    def insert_item(self, cursor, item):
        cursor.execute(self.sql, (item['title'], item['author'], item['pub_time'], item['article_id'], item['read_count'], item['like_count'], item['word_count'], item['comment_count'], item['subjects']))
            
        
    def handle_error(self, error, item, spider):
        print('* ' * 10 + 'error' + '* ' * 30)
        print(error)
        print('* ' * 10 + 'error' + '* ' * 30)
        