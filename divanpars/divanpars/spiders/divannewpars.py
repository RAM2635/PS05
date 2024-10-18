import scrapy


class LightingSpider(scrapy.Spider):
    name = "lightingspider"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/stavropol/category/svet"]

    def parse(self, response):
        lightings = response.css('div._Ud0k')  # Замените на актуальный CSS-селектор для раздела освещения
        for lighting in lightings:
            yield {
                'name': lighting.css('div.lsooF span::text').get(),
                # Замените селектор на соответствующий для названия освещения
                'price': lighting.css('div.pY3d2 span::text').get(),  # Замените селектор на соответствующий для цены
                'url': lighting.css('a').attrib['href']
            }
