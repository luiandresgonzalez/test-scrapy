import scrapy


class KlerosSpider(scrapy.Spider):
    name = "kleros"

    def start_requests(self):
        urls = [
            'http://klerosboard.com/court/?id=23',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        address = response.xpath('/html/body/div/div[6]/table').getall()
    for a in address[1:]:
       item = AddressJurados()
       item['hol'] = product.xpath('td[1]//text()').extract_first()
       item['first'] = product.xpath('td[2]//text()').extract_first()
       item['last'] = product.xpath('td[3]//text()').extract_first()
       yield item
