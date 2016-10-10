import scrapy

from tutorial.items import DoubanItem
from tutorial.items import DoubanBookItem


class BookSpider(scrapy.Spider):
    name = 'douban-book'
    allowed_domains = ['douban.com']
    start_urls = [
        'https://book.douban.com/top250'
    ]
    def parse(self, response):
        # request first page
		yield scrapy.Request(response.url, callback=self.parse_next)
		
		# request other page
		for page in response.xpath('//div[@class="paginator"]/a'): 
		    link = page.xpath('@href').extract()[0] 
		    yield scrapy.Request(link, callback=self.parse_next)
		
    def parse_next(self, response):
        for item in response.xpath('//tr[@class="item"]'):
            book = DoubanBookItem()
            book['name'] = item.xpath('td[2]/div[1]/a/@title').extract()[0]
            book['price'] = item.xpath('td[2]/p/text()').extract()[0]
            book['ratings'] = item.xpath('td[2]/div[2]/span[2]/text()').extract()[0]
            yield book
			

class DoubanSpider(scrapy.Spider):
	name = "Douban"
	allowed_domains = ["douban.com"]
	
def parse_with_cookie(self, response):
    file = codecs.open('page.html', 'w', encoding='utf-8')
    file.write(response.body)
    file.close()