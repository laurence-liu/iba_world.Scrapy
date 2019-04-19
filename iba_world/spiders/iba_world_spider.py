from bs4 import BeautifulSoup
import scrapy


class CocktailsSpider(scrapy.Spider):
    name = "cocktails"
    start_urls = [
        'https://iba-world.com/iba-cocktails/',
        'https://iba-world.com/contemporary-classics/',
        'https://iba-world.com/new-era-drinks/',
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')

        cocktails = soup.find_all("div", class_="col-lg-7 col-md-6 col-sm-6")

        for cocktail in cocktails:
            title = cocktail.find("h3").get_text()
            try:
                pic = cocktail.find("div", class_="blog_text").find("p").find("a", href=True).get("href")
            except AttributeError:
                pic = ""
            link = cocktail.find("div", class_="button_wrapper").find("a").get("href")

            yield {
                'title': title,
                'pic': pic,
                'link': link,
            }

        # for cocktail in response.css('div.col-lg-7.col-md-6.col-sm-6'):
        #     yield {
        #         'title': cocktail.xpath('h3/text()').get(),
        #         'pic': cocktail.css('div.blog_text a::attr(href)').get(),
        #         'link': cocktail.css('div.button_wrapper a::attr(href)').get(),
        #     }
