if __name__ == "__main__":
    # Write your solution here
    pass


class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def __str__(self):
        return f"Транспорт {self.model}, год {self.year}"

    def __repr__(self):
        return f"Транспорт('{self.model}', {self.year})"


class Car(Vehicle):
    def __init__(self, model, year, color):
        super().__init__(model, year)
        self.color = color

    def __str__(self):
        return f"Автомобиль {self.model}, год {self.year}, цвет {self.color}"

    def __repr__(self):
        return f"Автомобиль('{self.model}', {self.year}, '{self.color}')"

    def drive(self):
        return f"Вождение {self.model} автомобиля"

    def refuel(self):
        return "Заправка автомобиля"

    def __eq__(self, other):
        return self.model == other.model and self.year == other.year

    def accelerate(self, speed):
        """Разгоняет автомобиль до заданной скорости.

        Аргументы:
            speed (int): Желаемая скорость.

        Возвращает:
            str: Сообщение указывающее скорость автомобиля.

        ошибка:
            ValueError: Если заданная скорость отрицательна.
        """
        if speed < 0:
            raise ValueError("Скорость должна быть положительной")
        return f" {self.model} автомобиль разгоняется до {speed} км в час"


class Truck(Vehicle):
    def __init__(self, model, year, cargo_capacity):
        super().__init__(model, year)
        self.cargo_capacity = cargo_capacity

    def __str__(self):
        return f"Грузовик {self.model}, год {self.year}, грузоподъемность {self.cargo_capacity} тонн"

    def __repr__(self):
        return f"Грузовик('{self.model}', {self.year}, {self.cargo_capacity})"

    def drive(self):
        return f"Вождение {self.model} грузовика"

    def refuel(self):
        return "Заправка грузовика"

    def load_cargo(self, cargo):
        """Загрузка груза в грузовик.

        Аргументы:
            cargo (str): Груз, который нао загрузить.

        Возвращает:
            str: Сообщение, указывающее на загруженный груз.
        """
        return f"Загрузка {cargo} в {self.model} грузовик"

    def __lt__(self, other):
        return self.cargo_capacity < other.cargo_capacity

    def unload_cargo(self):
        """Выгрузка груза из грузовика.

        Возвращает:
            str: Сообщение, указывающее на выгруженный груз.
        """
        return f"Выгрузка груза из {self.model} грузовика"

    