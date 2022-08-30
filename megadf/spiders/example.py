import scrapy

url = 'https://www.megamaisdistribuidora.com.br/informatica'

class MegaDf(scrapy.Spider):
    name = 'megadf'
    start_urls = [url]

    def parse(self, response):
        for link in response.css('li.product a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_categoria)

    def parse_categoria(self, response):
        nome = response.css('.product-name ::text').get()
        marca = response.xpath(
            '//span[contains(text(), "Marca")]/following::strong/text()').get()
        modelo = response.xpath(
            '//span[contains(text(), "Modelo")]/following::strong/text()').get()
        ref = response.xpath(
            '//span[contains(text(), "Referência")]/following::strong/text()').get()
        valor = response.xpath('//*[@id="variacaoPreco"]/text()').get()
        link = response.url

        yield{
            'nome': nome,
            'marca': marca,
            'modelo': modelo,
            'ref': ref,
            'link': link,
            'valor': valor
        }
