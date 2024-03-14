import datetime
from bson import ObjectId


class Product:
    def __init__(self, activo: bool, category_id: ObjectId, carro: [], description: str, favorites: [], img: [],
                 price: float, stock: int, title: str):
        super().__init__()
        self.activo = activo
        self.carro = carro
        self.category_id = category_id
        self.description = description
        self.favorites = favorites
        self.img = img
        self.price = price
        self.stock = stock
        self.title = title
        self.last_updated = datetime.datetime.now(datetime.UTC)

    def __str__(self):
        return (self.description + ', ' + str(
            self.img) + ', ' + str(self.price) + ', ' + str(self.stock) + ', ' + self.title + ', ' +
                str(self.favorites) + ', ' + str(self.carro) + ', ' + str(self.activo) + str(self.last_updated))

    def to_dictionary(self):
        dic = {'activo': self.activo, 'carro': self.carro, 'category_id': self.category_id,
               'description': self.description, 'favorites': self.favorites,
               'img': self.img, 'price': self.price, 'stock': self.stock, 'title': self.title,
               'last_update': self.last_updated}
        return dic

    def new(self):
        return self
