# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import os


class SpiderdangdangPipeline(object):

    def __init__(self):
        # csv文件的位置,无需事先创建
        store_file = os.path.dirname(__file__) + '/spiders/qtw.csv'
        # 打开(创建)文件
        self.file = open(store_file, 'wb', encoding='utf-8')
        # csv写法
        self.writer = csv.writer(self.file)

    def process_item(self, item, spider):
        if item['name']:
            self.writer.writerow((item['name'], item['author'], item['press'], item['pub_date'],
                                  item['now_price'], item['pre_price'], item['discount'], item['outline'],
                                  item['img_url'], item['size'], item['paper'], item['package'], item['suit'],
                                  item['isbn'], item['category'], item['detail'], item['catalogue'], item['content'],
                                  item['author_detail']))
        return item

    def close_spider(self, spider):
        # 关闭爬虫时顺便将文件保存退出
        self.file.close()
