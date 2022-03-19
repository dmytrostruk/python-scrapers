from bs4 import BeautifulSoup
from bs4 import Tag
from models.product import Product
import requests


class EbayScraper:
    EBAY_URL = 'https://www.ebay.com/sch/i.html?_nkw='

    def printJSON(self, searchString):
      data = self.getData(searchString)
      
      for item in data:
        print(item.toJSON())

    def getData(self, searchString):
        html = self.__getHtml(searchString)
        soup = self.__parse(html)
        data = list(map(lambda item:
                        self.__getProduct(item),
                        self.__getItems(soup)))

        return data

    def __parse(self, html):
        return BeautifulSoup(html, 'html.parser')

    def __getHtml(self, searchString):
        str = '+'.join(searchString.split(' '))
        response = requests.get(self.EBAY_URL + str)
        return response.text

    def __getItems(self, soup):
        return soup.select_one('.srp-results').select(".s-item__pl-on-bottom")

    def __getProduct(self, item: Tag):
        title = item.select_one('.s-item__title').text
        image = item.select_one('.s-item__image-img').get('src')
        price = item.select_one('.s-item__price').text
        countryOfOrigin = self.__getCountryOfOrigin(item)
        url = item.select_one('.s-item__link').get('href')

        return Product(title, image, price, countryOfOrigin, url)

    def __getCountryOfOrigin(self, item):
        return " ".join(item.select_one('.s-item__location').text.split(' ')[1:])
