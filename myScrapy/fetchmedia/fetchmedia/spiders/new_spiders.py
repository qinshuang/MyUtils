# /usr/bin/python
# -*- coding:utf-8 -*-
"""
    Created by qinshuang on 6/30/16.
"""
import scrapy

from scrapy.http import Request
import json
import urllib2


class DmozSpider(scrapy.Spider):
    name = "ygdy8"
    start_urls = [
        "http://gaoqing.la/",
    ]

    def parse(self, response):
        _urls = response.xpath('//div[contains(@class,"mainleft")]//div[contains(@class,"article")]//a')[:1]
        for a in _urls:
            url = a.xpath('@href').extract()[0]
            yield Request(url, callback=self.sub_content)

    def sub_content(self, response):
        print response.url
        urls = response.xpath('//div[contains(@class,"article_container row  box")]//p//a')
        for item in urls:
            url = item.xpath('@href').extract()[0]
            text = item.xpath('./descendant::text()').extract()[0]
            print text
            print url

            jsonreq = json.dumps({ 'id': 'qwer',
                                  'method': 'aria2.addUri',
                                  'params': [[url]]})
            c = urllib2.urlopen('http://localhost:6800/jsonrpc', jsonreq)
