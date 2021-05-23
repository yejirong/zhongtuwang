# -*- coding: utf-8 -*-
import scrapy
from ..items import ZhongtuwangItem


class BookSpider(scrapy.Spider):
    name = 'book'
    # allowed_domains = ['bookschina.com']
    start_urls = ['http://www.bookschina.com/kinder/14000000/']  # 小说

    # start_urls = ['http://www.bookschina.com/kinder/46000000_0_0_11_0_1_1_0_0_/']  # 文学
    def parse(self, response):
        urls = response.xpath('//div[@class="bookList"]/ul/li/div/a/@href').extract()  # 爬取详细页链接
        for url in urls:
            yield scrapy.Request(url='http://www.bookschina.com/' + url, callback=self.parse_detaile)  # 导入详细页链接
        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first('')  # 爬取下一页的链接
        if next_page:
            yield scrapy.Request(url='http://www.bookschina.com/' + next_page, callback=self.parse)  # 导入下一页的链接

    def parse_detaile(self, response):  # 爬取每本书详细页的内容
        item = ZhongtuwangItem()  # item
        names = response.xpath('//div[@class="padLeft10"]/h1/text()').extract_first('').strip()  # 书名
        author = response.xpath('//div[@class="author"]/a/text()').extract_first('').strip()  # 作者
        publisher = response.xpath('//div[@class="publisher"]/a/text()').extract_first('').strip()  # 出版社
        out_data = response.xpath('//div[@class="publisher"]/i/text()').extract_first('').strip()  # 出版时间
        price = response.xpath('//span[@class="sellPrice"]/text()').extract_first('').strip()  # 价格（折后）
        price1 = response.xpath('//del[@class="price"]/text()').extract_first('').strip()  # 原价
        beat = response.xpath('//span[@class="discount"]/text()').extract_first('').strip()  # 打折数
        commnet = response.xpath('//div[@class="startWrap"]/a/text()').extract_first('').strip()  # 评论数
        collection = response.xpath('//div[@class="startWrap"]/em/text()').extract_first('').strip()  # 读者评分
        paper = response.xpath('//div[@class="otherInfor"]/i/text()').extract_first('').strip()  # 页数
        pack = response.xpath('//div[@class="copyrightInfor"]/ul/li[3]/text()').extract_first('').strip()  # 包装
        isbn = response.xpath('//div[@class="copyrightInfor"]/ul/li[1]/text()').extract_first('').strip()  # isbn
        item['names'] = names  # 书名
        item['author'] = author  # 作者
        item['publisher'] = publisher  # 出版社
        item['out_data'] = out_data  # 出版时间
        item['price'] = price  # 价格（折后）
        item['price1'] = price1.replace('¥', '')  # 原价
        item['beat'] = beat.replace('折', '').replace('(', '').replace(')', '')  # 打折数
        item['commnet'] = commnet.replace('条评论', '')  # 评论数
        item['collection'] = collection.replace('分', '')  # 读者评分
        item['paper'] = paper.replace('页', '')  # 页数
        item['pack'] = pack.replace('装帧：', '')  # 包装
        item['isbn'] = isbn.replace('ISBN：', '')  # isbn
        yield item
