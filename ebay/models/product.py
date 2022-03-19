import json

class Product:
    def __init__(self, title, image, price, countryOfOrigin, url):
        self.title = title
        self.image = image
        self.price = price
        self.countryOfOrigin = countryOfOrigin
        self.url = url

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
