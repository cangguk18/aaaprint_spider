import scrapy

class aaaprintSpiderSpider(scrapy.Spider):
    name = 'aaaprint_spider'
    allowed_domains = ['aaa-print.net']
    start_urls = ['https://aaa-print.net']

    def parse(self, response):
        #for item_url in response.css('html body div#page div#main table tbody tr td div[align="center"] a ::attr(href)').extract():
        #for category_url in response.xpath('//a[contains(@href,"/87")]/@href').extract():
        for category_url in response.xpath('//div[@class="product-inner"]/a/@href').extract():
        #for category_url in response.xpath('///ul[@class="side-nav"]/li/a/@href').extract():     
            category_url = 'https://aaa-print.net' + category_url[0:]
            yield scrapy.Request(category_url, callback = self.parse_item)
        #next_page = response.xpath('//a[not(contains(@href,"page=1"))]/@href|'
                                  # '//ul[@class="page-numbers"]/li/a/@href').extract()
        category_url = response.xpath('//ul[@class="page-numbers"]/li/a//@href').extract()   
        for url1 in category_url:
           url_desc = response.urljoin(url1)
           yield scrapy.Request(url=url_desc, callback = self.parse)
 
    def parse_item(self, response):
        Url = response.url
        Model = response.xpath('//html/body/div/div[2]/div/div[2]/div/div[1]/main/div/div/div[2]/h1/text()').extract()
        #Description = response.xpath('//div[@class="std"]/ul/li[string-length(text()) > 0]/text()|'
                                    # '//div[@class="std"]/p/text()').extract()
        #Model = response.xpath('//*[@id="vmMainPage"]/table/tbody/tr/td[1]/div/table[1]/tbody/tr/td/h2/text()').extract()
        Description = response.xpath('//html/body/div/div[2]/div/div[2]/div/div[1]/main/div/div/div[2]/div[1]/p/text()').extract()
        #Description = response.css('#vmMainPage > table > tbody > tr > td:nth-child(1) > div > table:nth-child(2) > tbody > tr > td > h2 ::text').extract()
        yield {'description': Description,
               'model': Model,
               #'reference': Reference,
               #'price': Price,
               'url': Url}


