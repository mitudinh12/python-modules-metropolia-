# 11.2

import exercise_9


class ElectricCar(exercise_9.Car):
    def __init__(self, registration_number, max_speed, battery_capacity: float):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(exercise_9.Car):
    def __init__(self, registration_number, max_speed, tank_volume: float):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume


def main_program_task_2():
    e_car = ElectricCar("ABC-15", 180, 52.5)
    g_car = GasolineCar("ACD-123", 165, 32.3)

    e_car.accelerate(50)
    g_car.accelerate(80)

    e_car.drive(3)
    g_car.drive(3)

    print(e_car.travelled_distance)
    print(g_car.travelled_distance)


# 11.1
class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author: str, page_count: int):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def __str__(self):
        return (f"\nName of the book: {self.name}"
                f"\nAuthor: {self.author}"
                f"\nPage count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def __str__(self):
        return (f"\nName of the magazine: {self.name}"
                f"\nChief editor: {self.chief_editor}")


def main_program_task_1():
    magazine = Magazine("Donald Duck", "Aki Hyyppä")
    book = Book("Compartment No. 6", "Rosa Liksom", 192)

    print(magazine)
    print(book)
