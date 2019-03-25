import scrapy

class CocktailsSpider(scrapy.Spider):
    name = "cocktails"
    start_urls = [
        'https://iba-world.com/iba-cocktails/',
        'https://iba-world.com/contemporary-classics/',
        'https://iba-world.com/new-era-drinks/',
    ]

    def parse(self, response):
        for cocktail in response.css('div.col-lg-7.col-md-6.col-sm-6'):
            yield {
                'title': cocktail.xpath('h3/text()').get(),
                'pic': cocktail.css('div.blog_text a::attr(href)').get(), 
                'link': cocktail.css('div.button_wrapper a::attr(href)').get(),
            }