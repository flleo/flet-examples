import datetime


class Category:
    def __init__(self, item: str):
        super().__init__()
        self.item = item
        self.last_updated = datetime.datetime.now(datetime.UTC)

    def __str__(self):
        return str(self.item + str(self.last_updated))

    def __dict__(self):
        dic = {'item': self.item, 'last_updated': self.last_updated}
        return dic

    def new(self):
        return self
