import random


# 9.1
class Car:
    def __init__(self, registration_number, max_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    # 9.2
    def accelerate(self, speed):
        self.current_speed = min(max(self.current_speed + speed, 0), self.max_speed)

    # 9.3
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

    def __str__(self):
        return (f"Registration number: {self.registration_number}, Max speed: {self.max_speed} km/h, "
                f"current speed: {self.current_speed} km/h, travelled distance: {self.travelled_distance} km")

def main_program_task_1():
    car1 = Car("ABC-123", 142, 0)
    print(car1)

    car1.accelerate(30)
    car1.drive(1.5)


# 9.4
def main_program_task_4():
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        car = Car(f"ABC-{i}", max_speed)
        cars.append(car)

    first_car_distance = 0

    while first_car_distance < 10000:
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
            if car.travelled_distance > first_car_distance:
                first_car_distance = car.travelled_distance
            if first_car_distance >= 10000:
                print(f"The winning car is: {car}.\nThe info of all cars raced: ")
                for i in cars:
                    print(i)
                break

main_program_task_4()
