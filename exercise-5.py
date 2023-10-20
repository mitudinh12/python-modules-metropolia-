import random
#5.1
def task_1():
    dices = int(input("How many dices do you want to roll? "))
    sum_value = 0
    for i in range(dices):
        value = random.randint(1,6)
        sum_value += value
    print(sum_value)

#5.2
def task_2():
    number_list = []
    number = input("Enter a number: ")
    while number != "":
        number_list.append(int(number))
        number = input("Enter a number: ")
    sorted_list = sorted(number_list, reverse=True)
    print(sorted_list[0:5])

#5.3
def task_3():
    number = int(input("Give a number: "))
    number_to_compare = number + 1
    for i in range(2, number_to_compare):
        if number % i == 0 and i != number:
            print("Not a prime number")
            break
        elif i == number or number == 2:
            print("Prime number")

#5.4
def task_4():
    cities = []
    for i in range(5):
        city = input("Enter a city name: ")
        cities.append(city)

    for city in cities:
        print(city, end='\n')


