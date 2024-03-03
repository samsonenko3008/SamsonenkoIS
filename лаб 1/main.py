# TODO Написать 3 класса с документацией и аннотацией типов

class Table:
    def __init__(self):
        self.material = "дерево"
        self.size = "200*300"

    def get_self(self):
        return self


class Flower:
    def __init__(self):
        self.species = "суккуленты"
        self.age = "2 года"


class Sweater:
    def __init__(self):
        self.material = "шерсть"
        self.size = "44"


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
