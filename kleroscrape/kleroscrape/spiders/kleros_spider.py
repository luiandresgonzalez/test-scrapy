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
        page = response.url.split("/")[-2]
        filename = f'kleros-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
