import scrapy
import logging
from scrapy.selector import Selector
from ..items import BookspiderItem
from ..settings import DEFAULT_REQUEST_HEADERS


class bookSpider(scrapy.Spider):
    name = 'bookScrapy'
    # start_urls = ['http://category.dangdang.com/pg%d-cp01.00.00.00.00.00-shlist.html'%i for i in range(1, 3)]
    start_page = 1
    finish_page = 1
    start_urls = ['http://category.dangdang.com/pg' + str(start_page) + '-cp01.00.00.00.00.00-shlist.html']

    def parse(self, response):
        sel = Selector(response)
        book_list = sel.css('ul#component_59').xpath('li')

        for book in book_list:
            item = BookspiderItem()
            item['name'] = self.check_data(book.css('p.name').xpath('a/text()').extract_first())
            item['author'] = self.check_data(book.css('p.search_book_author>span')[0].xpath('a/text()').extract_first())
            item['pub_date'] = self.check_data(book.css('p.search_book_author>span')[1].xpath('text()').extract_first()).replace(' /', '')
            item['press'] = self.check_data(book.css('p.search_book_author>span')[2].xpath('a/text()').extract_first())
            try:
                item['now_price'] = self.check_data(
                    book.css('p.price>span')[0].xpath('text()').extract_first()).replace(u'\xa5', u'')
                item['pre_price'] = self.check_data(
                    book.css('p.price>span')[1].xpath('text()').extract_first()).replace(u'\xa5', u'')
                item['discount'] = self.check_data(book.css('p.price>span')[2].xpath('text()').extract_first()).replace(
                    u'\xa0', u'').strip('(').replace(')', '')
            except:
                print()
            item['outline'] =self.check_data(book.css('p.detail').xpath('text()').extract_first())
            item['img_url'] = self.check_data(book.css('a.pic').xpath('img/@data-original').extract_first())
            item['link'] = self.check_data(book.css('p.name').xpath('a/@href').extract_first())

            yield scrapy.Request(callback=self.parse_book, meta={'item': item}, url=item['link'])

        if self.start_page <= self.finish_page:
            next_page = 'http://category.dangdang.com/pg' + str(self.start_page) + '-cp01.00.00.00.00.00-shlist.html'
            self.start_page += 1
            yield scrapy.Request(next_page, callback=self.parse)

    def check_data(self, data):
        temp = str(data)
        if temp is None:
            return '暂无'
        else:
            return data
	
    # 爬取图书详情页
    def parse_book(self, response):
        book = response.meta['item']

        book_detail = response.css('div#detail_describe>ul')
        book['size'] = book_detail.css('li')[0].xpath('text()').extract_first()
        book['paper'] = book_detail.css('li')[1].xpath('text()').extract_first()
        book['package'] = book_detail.css('li')[2].xpath('text()').extract_first()
        book['suit'] = book_detail.css('li')[3].xpath('text()').extract_first()
        book['isbn'] = book_detail.css('li')[4].xpath('text()').extract_first()
        book['category'] = book_detail.css('li#detail-category-path>span.lie').xpath('a/text()').extract()
        book['detail'] = response.css('div#detail>div#content>div.descrip').xpath('text()').extract_first()
        book['catalogue'] = response.css('div#detail>div#catalog>div.descrip').xpath('text()').extract_first()
        book['content'] = response.css('div#detail>div#extract>div.descrip').xpath('text()').extract_first()
        book['author_detail'] = response.css('div#detail>div#authorIntroduction>div.descrip').xpath('text()').extract_first()

        yield book

